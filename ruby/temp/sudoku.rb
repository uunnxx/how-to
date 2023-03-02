# Based on https://eregon.me/blog/2018/02/11/trick-sudoku.html
S = <<PUZZLE.lines.map { |l| l.chomp.chars.map(&:to_i)}
19___8__5
__2_5__89
8_674____
_____4_92
_23_7_81_
56_8_____
____279_3
93__8_1__
2__5___48
PUZZLE

next_fiber = Fiber.new {
  loop {
    puts S.map {|r| r * ' ' } << ''
    Fiber.yield
  }
}

[*0..8].product([*0..8]) {|r,c|
  if S[r][c] == 0
    succ = next_fiber
    next_fiber = Fiber.new {
      loop {
        1.upto(9) {|n|
          if (0..8).none? {|k| S[r][k] == n || S[k][c] == n || S[r - r%3 + k%3][c - c%3 + k/3] == n}
            S[r][c] = n
            succ.resume # We found a digit that works, try the next cell
          end
        }
        S[r][c] = 0
        Fiber.yield
      }
    }
  end
}

next_fiber.resume
