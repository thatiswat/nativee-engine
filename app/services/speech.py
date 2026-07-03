from app.providers.groq import GroqProvider


class SpeechService:

    def __init__(self):
        self.provider = GroqProvider()

    async def transcribe(
        self,
        audio_path: str,
    ) -> str:

        return await self.provider.transcribe(
            audio_path,
        )


speech_service = SpeechService()