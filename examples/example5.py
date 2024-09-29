from nsfw_goto import goto


def square(x):
    return x * x


my_value = 1
goto(15)


def helper_method(x):
    print(x)


helper_method(my_value)
helper_method(square(2))
