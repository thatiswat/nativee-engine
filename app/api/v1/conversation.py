from pathlib import Path
import uuid

import aiofiles
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import StreamingResponse

from app.core.config import UPLOAD_DIR
from app.engine.orchestrator import orchestrator
from app.speech.service import speech_service
from app.translation.service import translation_service
from app.voice.service import synthesis_service

router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"],
)


@router.post("")
async def conversation(
    audio: UploadFile = File(...),
    source_language: str = Form(...),
    target_language: str = Form(...),
):
    extension = (
        Path(audio.filename or "audio.m4a").suffix
        or ".m4a"
    )

    audio_path = (
        UPLOAD_DIR
        / f"{uuid.uuid4()}{extension}"
    )

    async with aiofiles.open(
        audio_path,
        "wb",
    ) as out_file:
        while chunk := await audio.read(1024 * 1024):
            await out_file.write(chunk)

    try:
        return await orchestrator.run(
            audio_path=str(audio_path),
            source_language=source_language,
            target_language=target_language,
            request_id=uuid.uuid4().hex,
        )

    finally:
        audio_path.unlink(
            missing_ok=True,
        )


@router.post("/stream")
async def conversation_stream(
    audio: UploadFile = File(...),
    source_language: str = Form(...),
    target_language: str = Form(...),
):
    extension = (
        Path(audio.filename or "audio.m4a").suffix
        or ".m4a"
    )

    audio_path = (
        UPLOAD_DIR
        / f"{uuid.uuid4()}{extension}"
    )

    async with aiofiles.open(
        audio_path,
        "wb",
    ) as out_file:
        while chunk := await audio.read(1024 * 1024):
            await out_file.write(chunk)

    try:

        # ---------------------------------------
        # Speech
        # ---------------------------------------

        original = await speech_service.transcribe(
            str(audio_path),
        )

        # ---------------------------------------
        # Translation
        # ---------------------------------------

        translation = await translation_service.translate(
            text=original,
            source_language=source_language,
            target_language=target_language,
        )

        # ---------------------------------------
        # Voice Streaming
        # ---------------------------------------

        return StreamingResponse(
            synthesis_service.stream(
                translation["translated"],
                target_language,
            ),
            media_type="audio/mpeg",
            headers={
                "Cache-Control": "no-cache",
                "Transfer-Encoding": "chunked",
            },
        )

    finally:
        audio_path.unlink(
            missing_ok=True,
        )