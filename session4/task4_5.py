def remember_result(function):
    """Decorator which remembers last result of function it decorates
    and prints it before next call."""
    last_result = None

    def wrapper(*args):
        nonlocal last_result
        print(f"Last result: '{last_result}'")
        # Применяем к каждому аргументу функцию str
        args = map(str, args)
        func = function(*args)
        last_result = func
    return wrapper


@remember_result
def sum_list(*args):
    """Function, which is decorated with help of @remember_result"""
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


def main():
    """Testing decorator"""
    sum_list('a', 'b')
    sum_list("abc", "cde")
    sum_list(1, 2, 3)


if __name__ == '__main__':
    main()