from dataclasses import dataclass, field


FRAME_SIZE = 3200
MAX_SEGMENT_SIZE = 64000


@dataclass(slots=True)
class AudioBuffer:

    frames: list[bytes] = field(
        default_factory=list
    )

    def append(
        self,
        frame: bytes,
    ):

        self.frames.append(frame)

    def clear(self):

        self.frames.clear()

    def bytes(self):

        return b"".join(
            self.frames
        )

    @property
    def size(self):

        return sum(
            len(frame)
            for frame in self.frames
        )

    @property
    def ready(self):

        return (
            self.size >= MAX_SEGMENT_SIZE
        )