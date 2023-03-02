# frozen_string_literal: true

def br(length: 80, linebreak: '-')
  puts ' ' * length
  puts linebreak * length
  puts linebreak * length
  puts ' ' * length
end

class Sequence
  def initialize(start, step, length)
    @start = start
    @step = step
    @length = length
  end

  # Virtual block always given, so we can use `yield` imlicitly
  # def each(&block)
  def each
    for i in 0...@length
      xi = @start + (@step * i)
      yield xi
    end
  end

  def select
    result = []
    each do |selected|
      result << selected if yield(selected)
    end
  end
end

sequence = Sequence.new 1, 1, 10
sequence.each do |element|
  puts element
end

br linebreak: '-', length: 100

sequence.select do |selected|
  puts selected if selected > 4
end
