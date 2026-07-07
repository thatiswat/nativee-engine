from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(slots=True)
class ConversationSession:

    id: str = field(
        default_factory=lambda: uuid4().hex
    )

    source_language: str = "en"

    target_language: str = "hi"

    transcript: str = ""

    translation: str = ""