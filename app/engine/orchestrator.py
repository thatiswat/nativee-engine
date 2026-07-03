from pathlib import Path

from app.runtime.context import RequestContext

from app.services.speech import speech_service
from app.services.translation import translation_service
from app.services.synthesis import synthesis_service


class ConversationOrchestrator:

    async def run(
        self,
        context: RequestContext,
        audio_path: str,
    ):

        # ---------------------------------------
        # Speech-to-Text
        # ---------------------------------------

        context.metrics.start("stt")

        original = await speech_service.transcribe(
            audio_path,
        )

        context.metrics.stop("stt")

        # ---------------------------------------
        # Translation
        # ---------------------------------------

        context.metrics.start("translation")

        translation = await translation_service.translate(
            text=original,
            source_language=context.source_language,
            target_language=context.target_language,
        )

        context.metrics.stop("translation")

        # ---------------------------------------
        # Text-to-Speech
        # ---------------------------------------

        context.metrics.start("tts")

        audio_output = await synthesis_service.synthesize(
            translation["translated"],
            context.target_language,
        )

        context.metrics.stop("tts")

        return {
            "request_id": context.request_id,
            "original": original,
            "translated": translation["translated"],
            "audio_url": f"/audio/{Path(audio_output).name}",
            "provider": translation["provider"],
            "stt": context.metrics.get("stt"),
            "translation": context.metrics.get("translation"),
            "tts": context.metrics.get("tts"),
            "pipeline_total": context.metrics.total,
        }


orchestrator = ConversationOrchestrator()