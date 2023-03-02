nums.minmax.reduce(:gcd)

def findGCD
  low, high = nums.minmax
  low.gcd(high)
end


