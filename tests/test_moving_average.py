from scratch.calc import moving_average


def test_moving_average_starts_with_the_first_window() -> None:
    assert moving_average([2, 4, 6, 8], 2)[0] == 3
