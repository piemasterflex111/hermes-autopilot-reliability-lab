"""Public package interface for the Hermes Autopilot Reliability Lab."""

from importlib.metadata import PackageNotFoundError, version

from .identity import AutonomyLevel, BenchmarkIdentity, FailureClass, Language

try:
    __version__ = version("hermes-autopilot-reliability-lab")
except PackageNotFoundError:  # pragma: no cover - source tree without installation
    __version__ = "0.0.0"

__all__ = [
    "AutonomyLevel",
    "BenchmarkIdentity",
    "FailureClass",
    "Language",
    "__version__",
]
