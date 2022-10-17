
import main


def test_main():
    
    Numbers = [-10, 20, 30, 40, -50]
    v1, v2 = main.minmax(numbers)
    
    assert v1 == -50, "Min value does not match"
    assert v2 == 40, "Max value does not match"
    
