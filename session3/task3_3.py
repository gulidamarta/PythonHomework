def count_letters(input_string: str):
    """
    A function, that takes string as an argument and returns a dictionary, that contains
    letters of given string as keys and a number of their occurrence as values.
    """
    result_dict = {ch: input_string.count(ch) for ch in input_string}
    return result_dict


def main():
    print(count_letters("stringsample"))
    print(count_letters("martamama"))


if __name__ == '__main__':
    main()
