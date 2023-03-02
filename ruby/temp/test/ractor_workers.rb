scheduler =
  Ractor.new do
    loop do
      Ractor.yield Ractor.recv
    end
  end

workers =
  8.times.map do |i|
    Ractor.new(scheduler, Ractor.current) do |r_input, r_output|
      while inp = r_input.take
        r_output << [inp, inp ** inp]
      end
    end
  end

TASKS = 30_000

(1..TASKS).each do |i|
  scheduler << i
end

completed = 0
while completed < TASKS && res = Ractor.recv
  p res.first if res.first % 1000 == 0
  completed += 1
end
