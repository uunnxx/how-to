require 'debug'

# Debug
debug = false
debug = true if ARGV[0] == 'debug'

a = 1
b = 2
binding.break if debug
c = 3
d = 4
binding.break if debug
p [a, b, c, d]
