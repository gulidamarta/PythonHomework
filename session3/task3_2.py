def generate_squares(number: int):
    """
    A function that takes a number as an argument and returns a dictionary, where the
    key is a number and the value is the square of that number.
    """
    numbers = {x: x ** 2 for x in range(1, number)}
    return numbers


def main():
    print(generate_squares(5))


if __name__ == '__main__':
    main()
