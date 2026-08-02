"""Unit tests for immutable benchmark identities."""

from dataclasses import FrozenInstanceError

import pytest

from hermes_autopilot_reliability import (
    AutonomyLevel,
    BenchmarkIdentity,
    FailureClass,
    Language,
    __version__,
)


def build_identity() -> BenchmarkIdentity:
    return BenchmarkIdentity(
        benchmark_id="python-false-success-001",
        repository="example/service",
        language=Language.PYTHON,
        failure_class=FailureClass.FALSE_COMPLETION,
        autonomy_level=AutonomyLevel.L3,
    )


def test_identity_normalizes_surrounding_whitespace() -> None:
    identity = BenchmarkIdentity(
        benchmark_id="  case-001  ",
        repository="  owner/repo  ",
        language=Language.JAVA,
        failure_class=FailureClass.STALE_EVIDENCE,
        autonomy_level=AutonomyLevel.L4,
    )
    assert identity.benchmark_id == "case-001"
    assert identity.repository == "owner/repo"


@pytest.mark.parametrize("field_name", ["benchmark_id", "repository"])
def test_identity_rejects_blank_required_fields(field_name: str) -> None:
    values = {
        "benchmark_id": "case-001",
        "repository": "owner/repo",
        "language": Language.PYTHON,
        "failure_class": FailureClass.PARTIAL_IMPLEMENTATION,
        "autonomy_level": AutonomyLevel.L3,
    }
    values[field_name] = "   "
    with pytest.raises(ValueError, match=field_name):
        BenchmarkIdentity(**values)  # type: ignore[arg-type]


def test_identity_is_immutable() -> None:
    identity = build_identity()
    with pytest.raises(FrozenInstanceError):
        identity.repository = "changed/repo"  # type: ignore[misc]


def test_identity_has_value_equality() -> None:
    assert build_identity() == build_identity()


def test_identity_exports_stable_json_friendly_values() -> None:
    assert build_identity().as_dict() == {
        "benchmark_id": "python-false-success-001",
        "repository": "example/service",
        "language": "python",
        "failure_class": "false_completion",
        "autonomy_level": 3,
    }


def test_autonomy_level_rejects_values_outside_l0_to_l4() -> None:
    with pytest.raises(ValueError):
        AutonomyLevel(5)


def test_version_is_available() -> None:
    assert __version__
