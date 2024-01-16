import time

def fib_generator(num):
    index = 0
    a = 0
    b = 1
    while index < num:
        time.sleep(0.1)        
        if index == 0:            
            yield a
        elif index == 1:
            yield b
        else:
            a, b = b, a + b
            yield b
        index+=1

for num in fib_generator(100):
    print(num)

