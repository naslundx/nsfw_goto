from nsfw_goto import goto

global_value = 0

def foo():
    global global_value
    global_value = 100
    local_value = 200
    goto(line=12)

def bar():
    print(global_value + local_value)

if global_value == 0:
    foo()
