from collections.abc import AsyncIterator

from app.providers.edge import EdgeProvider


class SynthesisService:

    def __init__(self):
        self.provider = EdgeProvider()

    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> str:

        return await self.provider.synthesize(
            text,
            language,
        )

    async def stream(
        self,
        text: str,
        language: str,
    ) -> AsyncIterator[bytes]:

        async for chunk in self.provider.stream(
            text,
            language,
        ):
            yield chunk


synthesis_service = SynthesisService()