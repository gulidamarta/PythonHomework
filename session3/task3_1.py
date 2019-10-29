import string


def test1_1(*strings):
    """
    Function, which receive a changeable number of strings and return characters, that appear in all strings.
    """
    if len(strings) == 0:
        raise Exception("Amount of arguments should be higher than 0.")

    s = set(*strings)
    res = set(s.pop())
    for item in s:
        res = res.intersection(item)
    return res


def test1_2(*strings):
    """
    Function, which receive a changeable number of strings and return characters, that appear at least one string.
    """
    if len(strings) == 0:
        raise Exception("Amount of the arguments should be higher that 0.")

    ascii_set = set(string.ascii_lowercase)
    s = set(*strings)
    res = set()
    for item in s:
        res.update(ascii_set.intersection(item))
    return res


def test1_3(*strings):
    """
    Function, which receive a changeable number of strings and return characters, that appear at least in two strings.
    """
    if len(strings) == 0:
        raise Exception("Amount of the arguments should be higher that 0.")

    s = set(*strings)
    res = set()
    temp_set = set(s.pop())
    for item in s:
        res.update(temp_set.intersection(set(item)))
        temp_set = set(item)
    return res


def test1_4(*strings):
    """
    Function, which receive a changeable number of strings and return characters of alphabet, that were not used
    in any string.
    """
    if len(strings) == 0:
        raise Exception("Amount of the arguments should be higher that 0.")

    ascii_set = set(string.ascii_lowercase)
    s = set(*strings)
    res = ascii_set.difference(s.pop())
    for item in s:
        res.difference_update(item)
    return res


def main():
    """
    Testing functions.
    """
    test_strings = ["hello", "world", "python", ]
    print(test1_1(test_strings))
    print(test1_2(test_strings))
    print(test1_3(test_strings))
    print(test1_4(test_strings))


if __name__ == '__main__':
    main()
