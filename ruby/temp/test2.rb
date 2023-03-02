require 'rspec/autorun'

def result(them, me)
  me.ord - 87
end

def bonus(them, me)
  case [them, me]
  in ['A', 'Z'] | ['B', 'X'] | ['C', 'Y']
    0
  in ['A', 'X'] | ['B', 'Y'] | ['C', 'Z']
    3
  else
    6
  end
end

def total(them, me)
  result(them, me) + bonus(them, me)
end

RSpec.describe 'RPS' do
  [
    ['A', 'Y', 2, 6, 8],
    ['B', 'X', 1, 0, 1],
    ['C', 'Z', 3, 3, 6]
  ].each do |them, me, _result, _bonus, _total|
    it "calculates the score #{them}, #{me}" do
      expect(result(them, me)).to eq(_result)
      expect(bonus(them, me)).to eq(_bonus)
      expect(total(them, me)).to eq(_total)
    end
  end
end

# if __FILE__ == $0
# if __FILE__ == $PROGRAM_NAME
#   File
#     .readlines(ARGV.first)
#     .map(&:chomp)
#     .map(&:split)
#     .map { total(_1, _2) }
#     .sum
# end
