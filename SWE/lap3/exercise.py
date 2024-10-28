def fibonacci_iterative_list(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Test the function
print(fibonacci_iterative_list(10))
def fibonacci_index_exceeding(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
print(fibonacci_index_exceeding(100))  # Example with value 100
def is_fibonacci(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number

# Test the function
print(is_fibonacci(21))  # True
print(is_fibonacci(22))  # False
