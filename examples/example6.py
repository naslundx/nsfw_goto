from nsfw_goto import goto


class MyClass:
    def __init__(self, secret):
        self.secret = secret

    def __str__(self):
        return f"The secret is {self.secret}"


foo = MyClass(123)
secret_value = 456
goto(16)
secret_value += 5
bar = MyClass(secret_value)
print(str(foo))
print(str(bar))
