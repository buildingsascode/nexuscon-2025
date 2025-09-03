NUMBER_1 = 1
NUMBER_2 = 1


def add_numbers(number_1: int, number_2: int) -> int:
    return number_1 + number_2


def test_add_numbers_returns_sum_of_two_numbers():
    assert add_numbers(NUMBER_1, NUMBER_2) == NUMBER_1 + NUMBER_2


def test_add_numbers_returns_integer():
    """Watch out, bad tests can be misleading, this test will never fail"""
    assert True
