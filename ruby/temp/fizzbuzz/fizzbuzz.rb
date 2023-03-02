# frozen_string_literal: true

def fizzbuzz
  fizzy = [nil, nil, :Fizz].cycle
  buzzy = [nil, nil, nil, nil, :Buzz].cycle

  (1..100).map do |n|
    "#{fizzy.next}#{buzzy.next}"[/.+/] || n
  end
end

puts fizzbuzz
