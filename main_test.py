
import main


def test_main():
    numbers = [0, 1, 3, 3, 5, -10, 2, 4]
    print(numbers)
    v1, v2 = main.minmax(numbers)
    assert v1 == -10, "Min value does not match"
    assert v2 == 5, "Max value does not match"
    numbers = [-20, -5, 10, 20, 30]
    print(numbers)
    v1, v2 = main.minmax(numbers)
    assert v1 == -20, "Min value does not match"
    assert v2 == 30, "Max value does not match"
