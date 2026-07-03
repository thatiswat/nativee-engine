from abc import ABC, abstractmethod


class STTProvider(ABC):

    @abstractmethod
    async def transcribe(
        self,
        audio_path: str,
    ) -> str:
        ...


class TranslationProvider(ABC):

    @abstractmethod
    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:
        ...


class TTSProvider(ABC):

    @abstractmethod
    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> str:
        ...