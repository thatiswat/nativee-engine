from dataclasses import dataclass, field


@dataclass(slots=True)
class Stage:

    name: str

    elapsed: float

    metadata: dict = field(
        default_factory=dict,
    )


class Profiler:

    def __init__(self):

        self.stages = []

    def add(
        self,
        name: str,
        elapsed: float,
        **metadata,
    ):

        self.stages.append(
            Stage(
                name=name,
                elapsed=elapsed,
                metadata=metadata,
            )
        )

    @property
    def total(self):

        return sum(
            stage.elapsed
            for stage in self.stages
        )

    def to_dict(self):

        return {
            stage.name.lower(): {
                "latency_ms": round(
                    stage.elapsed * 1000,
                    2,
                ),
                **stage.metadata,
            }
            for stage in self.stages
        }

    def report(self):

        lines = []

        lines.append("")
        lines.append("=" * 55)
        lines.append("Nativee Engine Profiler")
        lines.append("=" * 55)

        for stage in self.stages:

            lines.append(
                f"{stage.name:<15}"
                f"{stage.elapsed * 1000:>8.2f} ms"
            )

            for key, value in stage.metadata.items():

                lines.append(
                    f"    {key:<12}: {value}"
                )

        lines.append("-" * 55)

        lines.append(
            f"{'TOTAL':<15}"
            f"{self.total * 1000:>8.2f} ms"
        )

        lines.append("=" * 55)

        return "\n".join(lines)