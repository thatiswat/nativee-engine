import time
from abc import ABC, abstractmethod

from fastapi import HTTPException
from groq import Groq

from app.core.config import GROQ_API_KEY
from app.core.logger import logger


class STTProvider(ABC):
    @abstractmethod
    async def transcribe(
        self,
        audio_path: str,
    ) -> str:
        """
        Convert speech to text.
        """
        raise NotImplementedError


class GroqProvider(STTProvider):
    MODEL = "whisper-large-v3"

    def __init__(self) -> None:
        self.client = Groq(api_key=GROQ_API_KEY)

    async def transcribe(
        self,
        audio_path: str,
    ) -> str:
        """
        Convert speech to text using Groq Whisper.
        """

        start = time.perf_counter()

        try:
            with open(audio_path, "rb") as audio_file:
                result = self.client.audio.transcriptions.create(
                    model=self.MODEL,
                    file=audio_file,
                    response_format="json",
                    temperature=0,
                )

            elapsed = (
                time.perf_counter()
                - start
            )

            logger.info(
                "Groq STT %.3fs",
                elapsed,
            )

            transcript = result.text.strip()

            if not transcript:
                raise HTTPException(
                    status_code=400,
                    detail="No speech detected.",
                )

            return transcript

        except HTTPException:
            raise

        except Exception as exc:
            logger.exception(
                "Groq STT failed"
            )

            raise HTTPException(
                status_code=500,
                detail=f"Speech recognition failed: {exc}",
            )