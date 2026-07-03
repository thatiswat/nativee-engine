import time
from abc import ABC, abstractmethod
from functools import lru_cache

from deep_translator import GoogleTranslator
from fastapi import HTTPException


# ==========================================================
# Config
# ==========================================================

SOURCE_LANGUAGE = "auto"


# ==========================================================
# Internal Cached Translator
# ==========================================================

@lru_cache(maxsize=2048)
def _cached_translate(
    text: str,
    target_language: str,
) -> str:
    """
    Cached Google translation call.
    """

    return GoogleTranslator(
        source=SOURCE_LANGUAGE,
        target=target_language,
    ).translate(text)


# ==========================================================
# Base Provider
# ==========================================================

class TranslationProvider(ABC):
    @abstractmethod
    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:
        """
        Translate text.
        """
        raise NotImplementedError


# ==========================================================
# Google Provider
# ==========================================================

class GoogleProvider(TranslationProvider):
    """
    Google Translation Provider.

    Wrapped as a class so it can be registered
    inside TranslationRegistry.
    """

    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:

        start = time.perf_counter()

        try:
            translated = _cached_translate(
                text.strip(),
                target_language,
            )

            if (
                not translated
                or translated.startswith("Error 500")
                or "That's an error" in translated
            ):
                raise HTTPException(
                    status_code=502,
                    detail="Google Translate temporarily unavailable.",
                )

            elapsed = (
                time.perf_counter()
                - start
            )

            print(
                f"🌍 Translation : {elapsed:.3f}s"
            )

            return translated

        except HTTPException:
            raise

        except Exception as exc:
            raise HTTPException(
                status_code=500,
                detail=f"Translation failed: {exc}",
            )


# ==========================================================
# Future Providers
# ==========================================================

# class IndicProvider(TranslationProvider):
#     async def translate(
#         self,
#         text: str,
#         source_language: str,
#         target_language: str,
#     ) -> str:
#         ...


# class NLLBProvider(TranslationProvider):
#     async def translate(
#         self,
#         text: str,
#         source_language: str,
#         target_language: str,
#     ) -> str:
#         ...