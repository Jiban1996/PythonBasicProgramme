num = 4  # Number of terms in the Fibonacci series

a, b = 0, 1
fib_series = []

for i in range(num):
    fib_series.append(a)  # Append the current Fibonacci number to the list
    sum = a + b
    a = b
    b = sum

print(fib_series) 