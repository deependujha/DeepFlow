# credits: https://github.com/deependujha

from deepflow_engine.core.engine import DeepFlowEngine
from deepflow_engine.core.game import DeepFlowGame
from deepflow_engine.core.event import Event
from deepflow_engine.core.pipeline import run_pipeline
from deepflow_engine.publisher import BasePublisher, TelegramPublisher
from importlib.metadata import version


def get_version() -> str:
    """Returns the current version of DeepFlow-Engine."""
    return version("deepflow-engine")


def main() -> None:
    print(f"Hello from DeepFlow-Engine v{get_version()}!")


__all__ = [
    "DeepFlowEngine",
    "DeepFlowGame",
    "Event",
    "BasePublisher",
    "TelegramPublisher",
    "run_pipeline",
]
