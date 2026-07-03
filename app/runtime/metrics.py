from dataclasses import dataclass, field
from time import perf_counter


@dataclass(slots=True)
class Metrics:

    values: dict = field(default_factory=dict)
    _running: dict = field(default_factory=dict)

    def start(
        self,
        name: str,
    ):

        self._running[name] = perf_counter()

    def stop(
        self,
        name: str,
    ):

        started = self._running.pop(name)

        self.values[name] = (
            perf_counter()
            - started
        )

    def get(
        self,
        name: str,
    ) -> float:

        return round(
            self.values.get(name, 0.0),
            3,
        )

    @property
    def total(
        self,
    ) -> float:

        return round(
            sum(self.values.values()),
            3,
        )