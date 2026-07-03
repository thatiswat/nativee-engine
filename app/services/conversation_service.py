import time

from app.services.speech import (
    speech_service,
)

from app.services.translation import (
    translation_service,
)

from app.services.synthesis import (
    synthesis_service,
)


class ConversationService:

    async def process(
        self,
        audio_path,
        source_language,
        target_language,
    ):

        pipeline_start = (
            time.perf_counter()
        )

        stt_start = time.perf_counter()

        original = (
            await speech_service.transcribe(
                audio_path,
            )
        )

        stt_time = (
            time.perf_counter()
            - stt_start
        )

        translation_start = (
            time.perf_counter()
        )

        translation = (
            await translation_service.translate(
                original,
                source_language,
                target_language,
            )
        )

        translation_time = (
            time.perf_counter()
            - translation_start
        )

        tts_start = (
            time.perf_counter()
        )

        audio_output = (
            await synthesis_service.synthesize(
                translation["translated"],
                target_language,
            )
        )

        tts_time = (
            time.perf_counter()
            - tts_start
        )

        return {
            "original": original,
            "translated": translation[
                "translated"
            ],
            "provider": translation[
                "provider"
            ],
            "audio_output": audio_output,
            "stt": stt_time,
            "translation": translation_time,
            "tts": tts_time,
            "pipeline_total": (
                time.perf_counter()
                - pipeline_start
            ),
        }


conversation_service = (
    ConversationService()
)