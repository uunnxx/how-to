def row_sum_odd_numbers(numbers)
  return 1 if numbers < 2
  
  sum_to_return = 0
  count = numbers - 1
  get_first_odd = (numbers * count) + 1
  
  (0...numbers).each do
    sum_to_return += get_first_odd
    get_first_odd += 2
  end
  
  sum_to_return
end
