from dataclasses import dataclass, field
from time import perf_counter
from uuid import uuid4

from app.runtime.metrics import Metrics


@dataclass(slots=True)
class RequestContext:

    source_language: str

    target_language: str

    request_id: str = field(
        default_factory=lambda: uuid4().hex
    )

    started_at: float = field(
        default_factory=perf_counter
    )

    metrics: Metrics = field(
        default_factory=Metrics
    )

    metadata: dict = field(
        default_factory=dict
    )