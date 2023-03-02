# Return true if num less or equal to 0

# variant 1:
def less_than_or_equal_to_zero(num)
  if num <= 0
    true
  else
    false
  end
end

# variant 2:
def less_than_or_equal_to_zero2(num)
  num <= 0
end

# variant 3:
def less_than_or_equal_to_zero(num)
  num <= 0 ? true : false
end
