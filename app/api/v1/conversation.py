from pathlib import Path
import uuid

import aiofiles
from fastapi import APIRouter, File, Form, UploadFile

from app.core.config import UPLOAD_DIR
from app.engine.orchestrator import orchestrator
from app.runtime.context import RequestContext

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

        while chunk := await audio.read(
            1024 * 1024
        ):
            await out_file.write(chunk)

    context = RequestContext(
        source_language=source_language,
        target_language=target_language,
    )

    try:

        return await orchestrator.run(
            context=context,
            audio_path=str(audio_path),
        )

    finally:

        audio_path.unlink(
            missing_ok=True,
        )