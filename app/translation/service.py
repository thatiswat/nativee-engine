from app.core.config import TRANSLATION_PROVIDER

from app.providers.google import GoogleProvider


class TranslationService:

    def __init__(self):

        self.providers = {
            "google": GoogleProvider(),
        }

    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ):

        provider = self.providers[
            TRANSLATION_PROVIDER
        ]

        translated = await provider.translate(
            text=text,
            source_language=source_language,
            target_language=target_language,
        )

        return {
            "translated": translated,
            "provider": TRANSLATION_PROVIDER,
        }


translation_service = TranslationService()