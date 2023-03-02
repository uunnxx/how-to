# frozen_string_literal: true

def solution(arg)
  # p arg.length
  # p arg.length / 2
  # p arg.sum
  # diff = 0
  lefthand = 0
  righthand = arg.sum

  
  arg.each_with_index do |e, i|
    # p "index: #{i} element: #{e}"
    p lefthand += e
    p righthand -= e
    diff = lefthand - righthand
    previous_diff = diff
    puts "Diffs: #{diff}"
    if diff < 0
      puts "Lefthand is less than Righthand"
    else
      puts "Righthand is less than Lefthand"
    end
    puts '---------------------------'
  end

end

lists = [3, 1, 2, 4, 3]
# solution(lists)


########################################################


class TapeEquilibrium
  def solution(a)
    sum_left = a[0]
    sum_right = a.sum - a[0]
    diff = (sum_left - sum_right).abs
    p = 0
    current_element_at_p = 0

    for i in (1..a.length - 2) do
      sum_left += a[i]
      sum_right -= a[i]
      current_diff = (sum_left - sum_right).abs
      diff = current_diff if diff > current_diff
      p = i
      current_element_at_p = a[i]
    end
    "difference is: #{diff}, p is: #{p}, and current el at p is: #{current_element_at_p}"
  end
end

puts TapeEquilibrium.new.solution([3, 1, 2, 4, 3])
