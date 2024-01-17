import time

def fib_generator(num):
    index = 0
    a = 0
    b = 1
    while index < num:        
        if index == 0:            
            yield a
        elif index == 1:
            yield b
        else:
            a, b = b, a + b
            yield b
        index+=1

fib_nums = fib_generator(1000)

for num in fib_nums:
    print(num)

