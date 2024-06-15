memo = {}  # dictionary for Memoization

def fib(n):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    elif n in memo:  # Check if result for n has already been evaluated
        return memo[n]
    else:  # otherwise recursive step
        memo[n] = fib(n-1) + fib(n-2)  # store the result of n in memoization dictionary
        return memo[n]  # return the value


print(fib(100))
