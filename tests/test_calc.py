import pytest
from scratch.calc import average, total, window_sums


def test_total() -> None:
    assert total([]) == 0
    assert total([1, 2, 3]) == 6
    assert total([1.5, 2.5]) == 4.0
    assert isinstance(total([]), float)


def test_average() -> None:
    assert average([2, 4]) == 3
    with pytest.raises(ValueError):
        average([])


def test_window_sums() -> None:
    assert window_sums([1, 2, 3, 4], 2) == [3, 5, 7]
    assert window_sums([1, 2], 3) == []
    with pytest.raises(ValueError):
        window_sums([1], 0)
