import random


def minmax(numbers):
    minval = None
    maxval = None
    
    for n in numbers:
        #find minval
        if minval is None or n < minval:
            minval = n
        
        #find maxval
        if maxval is None or n > maxval:
            maxval = n
    
    return minval, maxval


def main():

    numbers = [1, 2, 3, 4, 5]
    minval, maxval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value:{minval}')

    numbers = [random.randint(0, 100) for i in range(10)]
    minval, maxval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value: {minval}')


if __name__ == '__main__':
    main()
