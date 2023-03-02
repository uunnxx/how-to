def fib(n)
  new, old = 1, 0
  n.times { new, old = new + old, new }
  old
end


t1 = Thread.new do
  3000.times.each do |i|
    fib(i) if i % 2 == 0
  end
end

t2 = Thread.new do
  3000.times.each do |i|
    fib(i) if i % 2 == 1
  end
end

t1.join
t2.join
