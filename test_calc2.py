from calc2 import mul


def test_mul() -> None:
    assert mul(3, 4) == 12


def test_mul_by_zero() -> None:
    assert mul(5, 0) == 0
