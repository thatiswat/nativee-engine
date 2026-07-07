from app.engine.vad import vad


class SegmentScheduler:

    def should_flush(
        self,
        buffer,
        frame,
    ) -> bool:

        if not vad.is_speech(
            frame,
        ):
            return False

        return buffer.ready


scheduler = SegmentScheduler()