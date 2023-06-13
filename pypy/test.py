from time import perf_counter

t1 = perf_counter()
nums = range(10**9)
sum = 0

for k in nums:
    sum = sum + k

print("Sum of 1,000 numbers is : ", sum)
t2 = perf_counter()
t = round(t2 - t1, 4)
print("Elapsed time is : ", t, " seconds")
