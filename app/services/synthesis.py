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


synthesis_service = SynthesisService()