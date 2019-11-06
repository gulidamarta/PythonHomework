def call_once(function):
    """A decorator which runs a function or method once."""
    has_run = False

    def decorated(*args, **kwargs):
        nonlocal has_run
        if not has_run:
            func = function(*args, **kwargs)
            has_run = True
            return func
    return decorated


@call_once
def sum_of_numbers(a, b):
    """Function, which was decorated with help of @call_once"""
    return a + b


def main():
    """Test decorator"""
    print(sum_of_numbers(1, 2))
    print(sum_of_numbers(2, 3))
    print(sum_of_numbers(3, 4))


if __name__ == '__main__':
    main()
