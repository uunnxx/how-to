result = DATA
  .readlines(chomp: true)
  .map(&:split)
  # .map {_1.split(" ")}
  .map { [_1, _2.to_i] }

p result

def main(a, b)
  a + b
end


main(2, 4)


__END__
addx 12
addx 15
addx 12
addx 15