from pathlib import Path
import logging
import time

from app.core.profiler import Profiler
from app.speech.service import speech_service
from app.translation.service import translation_service
from app.voice.service import synthesis_service

logger = logging.getLogger(__name__)


class ConversationOrchestrator:

    async def run(
        self,
        audio_path: str,
        source_language: str,
        target_language: str,
        request_id: str,
    ):
        profiler = Profiler()
        overall_start = time.perf_counter()

        try:

            # ---------------------------------------
            # Input
            # ---------------------------------------

            audio_file = Path(audio_path)

            profiler.add(
                name="Input",
                elapsed=0,
                filename=audio_file.name,
                size_kb=round(
                    audio_file.stat().st_size / 1024,
                    2,
                ),
            )

            # ---------------------------------------
            # Speech
            # ---------------------------------------

            start = time.perf_counter()

            original = await speech_service.transcribe(
                audio_path,
            )

            speech_elapsed = (
                time.perf_counter() - start
            )

            profiler.add(
                name="Speech",
                elapsed=speech_elapsed,
                provider="Groq",
                model="whisper-large-v3",
                characters=len(original),
                words=len(original.split()),
            )

            # ---------------------------------------
            # Translation
            # ---------------------------------------

            start = time.perf_counter()

            translation = await translation_service.translate(
                text=original,
                source_language=source_language,
                target_language=target_language,
            )

            translation_elapsed = (
                time.perf_counter() - start
            )

            profiler.add(
                name="Translation",
                elapsed=translation_elapsed,
                provider=translation["provider"],
                source=source_language,
                target=target_language,
                input_chars=len(original),
                output_chars=len(
                    translation["translated"]
                ),
            )

            # ---------------------------------------
            # Voice
            # ---------------------------------------

            start = time.perf_counter()

            audio_output = await synthesis_service.synthesize(
                translation["translated"],
                target_language,
            )

            voice_elapsed = (
                time.perf_counter() - start
            )

            profiler.add(
                name="Voice",
                elapsed=voice_elapsed,
                provider="Edge",
                voice=target_language,
                characters=len(
                    translation["translated"]
                ),
            )

            # ---------------------------------------
            # Output
            # ---------------------------------------

            output_file = Path(audio_output)

            profiler.add(
                name="Output",
                elapsed=0,
                filename=output_file.name,
                size_kb=round(
                    output_file.stat().st_size / 1024,
                    2,
                ),
            )

            # ---------------------------------------
            # Engine
            # ---------------------------------------

            engine_elapsed = (
                time.perf_counter()
                - overall_start
            )

            profiler.add(
                name="Engine",
                elapsed=engine_elapsed,
                success=True,
            )

            logger.info(
                profiler.report()
            )

            return {
                "request_id": request_id,
                "original": original,
                "translated": translation["translated"],
                "audio_url": f"/audio/{output_file.name}",
                "provider": translation["provider"],
                "latency_ms": round(
                    engine_elapsed * 1000,
                    2,
                ),
                "profiling": profiler.to_dict(),
            }

        except Exception:

            profiler.add(
                name="Engine",
                elapsed=(
                    time.perf_counter()
                    - overall_start
                ),
                success=False,
            )

            logger.exception(
                "Conversation request failed."
            )

            logger.info(
                profiler.report()
            )

            raise


orchestrator = ConversationOrchestrator()