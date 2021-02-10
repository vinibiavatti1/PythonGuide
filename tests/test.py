x = 1
def func():
    global x
    x = 2
    print(x)
func()
print(x)