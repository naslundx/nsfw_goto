from nsfw_goto import goto, goto_v2

class MyClass:
    def __init__(self, secret):
        self.secret = secret

    def __str__(self):
        return f"The secret is {self.secret}"

foo = MyClass(123)
secret_value = 456
goto_v2(14)
secret_value += 5
bar = MyClass(secret_value)
print(str(foo))
print(str(bar))
