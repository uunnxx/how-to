def br():
    print()
    print('-' * 80)
    print()


###############################################################
# O(n) Runtime complexity, O(n) Space complexity
# O(n) Stack complexity <--------------------------------------

memo = [1, 1]


def fibonacci(n):
    if len(memo) > n:
        return memo[n]

    result = fibonacci(n - 1) + fibonacci(n - 2)
    memo.append(result)  # f(n) = f(n-1) + f(n-2)
    return result


###############################################################
# Iterative Dynamic Programming
# O(n) Runtime complexity, O(n) Space complexity
# No recursive stack <-----------------------------------------

def fibonacci_no_recursive_stack(n):
    memo = [1, 1]  # f(0) = 1, f(1) = 1

    memo.extend(memo[i - 1] + memo[i - 2] for i in range(2, n + 1))
    return memo[n]


###############################################################################
# Advanced Iterative Dynamic Programming
# O(n) Runtime complexity, O(1) Space complexity
# No recursive stack <---------------------------------------------------------

def fibonacci_advanced(n):
    memo = [1, 1]  # f(1) = 1, f(2) = 1

    for i in range(2, n):
        memo[i % 2] = memo[0] + memo[1]

    # return memo[0] + memo[1]
    return sum(memo)


br()

print("Memoized: ", fibonacci(1000))
# print("Memoized no recursive stack: ", fibonacci_no_recursive_stack(1000))
# print("Memoized, Advanced no recursive stack: ", fibonacci_advanced(1000))

br()
