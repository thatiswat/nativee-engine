from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.core.config import UPLOAD_DIR

router = APIRouter(
    prefix="/audio",
    tags=["Audio"],
)


@router.get("/{filename}")
async def audio(
    filename: str,
):
    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Audio not found.",
        )

    return FileResponse(
        path=file_path,
        media_type="audio/mpeg",
        filename=filename,
    )