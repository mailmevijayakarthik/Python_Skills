fibonacci_cache = {}
def fibonacci(n):

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        value=fibonacci(n-1)+fibonacci(n-2)
        fibonacci_cache[n]=value
        return value

for n in range(1,1000):
    print(n,":",fibonacci(n))