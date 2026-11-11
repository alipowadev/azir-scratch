"""Small arithmetic helpers."""

from __future__ import annotations


def total(values: list[float]) -> float:
    """The sum of `values` (0 for an empty list)."""
    result = 0.0
    for value in values:
        result += value
    return result


def product(values: list[float]) -> float:
    """The product of `values` (1 for an empty list)."""
    result = 1.0
    for value in values:
        result *= value
    return result


def average(values: list[float]) -> float:
    """The mean of `values`. Raises ValueError for an empty list."""
    if not values:
        raise ValueError("average of an empty list")
    return total(values) / len(values)


def window_sums(values: list[float], size: int) -> list[float]:
    """The sum of every run of `size` consecutive values, in order."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [total(values[i : i + size]) for i in range(len(values) - size + 1)]
