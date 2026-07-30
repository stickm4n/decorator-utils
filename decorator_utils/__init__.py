from __future__ import annotations

from importlib.metadata import version

from .context import DecoratorContext as DecoratorContext
from .decorators.benchmark import Benchmark as Benchmark
from .metadata import FunctionMetadata as FunctionMetadata
from .wrapper import function_wrapper as function_wrapper


__version__ = version('decorator-utils')
