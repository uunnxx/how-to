string = 'hello'
string2 = 'h2ll4'

VOWELS_TO_INT = { a: 1, e: 2, i: 3, o: 4, u: 5 }
INT_TO_VOWELS = VOWELS_TO_INT.invert

def encode(string):
  res = ''

  string.each_char do |ch|
    if ch =~ /[aeiou]/
      res << VOWELS_TO_INT[ch.to_sym].to_s
    else
      res << ch
    end
  end
  res
end


def decode(string)
  res = ''

  string.each_char do |ch|
    if ch =~ /[1-5]/
      res << INT_TO_VOWELS[ch.to_i].to_s
    else
      res << ch
    end
  end
  res
end

p encode(string)
p decode(string2)

# or:
# def encode(s)
#   s.tr("aeiou", "12345")
# end
#
# def decode(s)
#   s.tr("12345", "aeiou")
# end
