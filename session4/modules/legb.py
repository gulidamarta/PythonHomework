a = "I am global variable!"


def enclosing_funcion_task_1():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)
    return inner_function


def enclosing_function_task_2_1():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)
    return inner_function


def enclosing_function_task_2_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)
    return inner_function


def main():
    inner_function_task_1 = enclosing_funcion_task_1()
    inner_function_task_1()
    inner_function_task_2_1 = enclosing_function_task_2_1()
    inner_function_task_2_1()
    inner_function_task_2_2 = enclosing_function_task_2_2()
    inner_function_task_2_2()


if __name__ == '__main__':
    main()
