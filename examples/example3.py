from nsfw_goto import goto

x = 2
goto(line=9)
x = 3
if x == 3:
    if x == 2:
        x = 4
        print('hello world!')
        goto(line=7)
        print('end of inner if')
    print('end of outer if')
print(x)
