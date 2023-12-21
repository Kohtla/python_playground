import time

print('Hello, world')

# could be simpler
def remove_duplicates(some_sort_of_string):
    symbols = {}
    return_string = ''
    total_deleted = 0

    for letter in some_sort_of_string:
        if symbols.get(letter):
            symbols[letter]+=1
        else:
            symbols[letter] = 1
    
    for symbol in symbols.keys():
        return_string += symbol
        total_deleted += symbols[symbol] - 1

    return return_string, total_deleted

print(remove_duplicates('aaabbbac'))

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        duration = time.time() - start
        print(duration)
    return wrapper

@timer
def check(num,n):
    print(num in range(n))


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@timer
def compute(n):
    print(fib(n))

compute()

