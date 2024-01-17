def closure():
    adder = 0
    def inner(num):
        nonlocal adder
        adder = adder + num
        return adder    
    return inner

print("Closure test:")
func = closure()
for i in range(10):
    print(func(i))
print("")

# decorators play
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Do something before func execution")
        func(*args, **kwargs)
        print("Do something after func execution")    
    return wrapper

print("No decorator test:")
func = lambda x: print(x)
func = decorator(func)
func("Print me please! I'm inside")
print("")


@decorator
def play_with_me(x):
    print(x)
print("Decorator test:")
play_with_me("I was called with decorator")
print("")

print("Parametrized ")





    
