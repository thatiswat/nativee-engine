from pathlib import Path
import uuid

import aiofiles

from app.core.config import (
    GENERATED_DIR,
    UPLOAD_DIR,
)


class StorageService:

    async def save_upload(
        self,
        upload,
    ) -> Path:

        extension = (
            Path(
                upload.filename
                or "audio.m4a"
            ).suffix
            or ".m4a"
        )

        destination = (
            UPLOAD_DIR
            / f"{uuid.uuid4()}{extension}"
        )

        async with aiofiles.open(
            destination,
            "wb",
        ) as file:

            while chunk := await upload.read(
                1024 * 1024
            ):
                await file.write(chunk)

        return destination

    def remove(
        self,
        path: str | Path,
    ):

        Path(path).unlink(
            missing_ok=True,
        )


storage_service = StorageService()