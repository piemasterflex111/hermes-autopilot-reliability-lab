"""Typed identifiers for reproducible autonomous-agent benchmark cases."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, StrEnum
from typing import Final

_EMPTY_FIELD_MESSAGE: Final = "{field_name} must not be blank"


class Language(StrEnum):
    """Implementation language exercised by a benchmark case."""

    PYTHON = "python"
    JAVA = "java"
    JAVASCRIPT = "javascript"


class FailureClass(StrEnum):
    """Failure class intentionally measured by the reliability lab."""

    FALSE_COMPLETION = "false_completion"
    PARTIAL_IMPLEMENTATION = "partial_implementation"
    STALE_EVIDENCE = "stale_evidence"
    CONTRADICTORY_RECOVERY_STATE = "contradictory_recovery_state"
    UNSAFE_SUCCESS = "unsafe_success"


class AutonomyLevel(IntEnum):
    """Hermes Project Autopilot autonomy level."""

    L0 = 0
    L1 = 1
    L2 = 2
    L3 = 3
    L4 = 4


@dataclass(frozen=True, slots=True)
class BenchmarkIdentity:
    """Immutable identity for one reproducible benchmark case."""

    benchmark_id: str
    repository: str
    language: Language
    failure_class: FailureClass
    autonomy_level: AutonomyLevel

    def __post_init__(self) -> None:
        for field_name in ("benchmark_id", "repository"):
            value = getattr(self, field_name).strip()
            if not value:
                raise ValueError(_EMPTY_FIELD_MESSAGE.format(field_name=field_name))
            object.__setattr__(self, field_name, value)

    def as_dict(self) -> dict[str, str | int]:
        """Return a stable JSON-friendly representation."""

        return {
            "benchmark_id": self.benchmark_id,
            "repository": self.repository,
            "language": self.language.value,
            "failure_class": self.failure_class.value,
            "autonomy_level": int(self.autonomy_level),
        }
