def fib(n):
    memo = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n1f = 0
        n2f = 0
        n1 = n - 1
        n2 = n - 2
        if n1 in memo:
            n1f = memo[n1]
        else:
            n1f = fib(n1)
            memo[n1] = n1f

        if n2 in memo:
            n2f = memo[n2]
        else:
            n2f = fib(n2)
            memo[n2] = n2f
        return n1f + n2f

# Driver
n = 30
print('Fibonacci series of 5 numbers is:', end=" ")
for i in range(0, n):
    print(fib(i), end=" ")