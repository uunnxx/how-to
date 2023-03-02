# frozen_string_literal: true

def br(string = nil, width = 80)
  tab_width = '    '
  if string
    string = tab_width + string
    string += tab_width
  end

  puts "\n", '=' * width
  puts string.center(width, '-') if string
  puts '=' * width, "\n"
end

def brd
  puts "\n\n", "-" * 80, "\n\n"
end


br('main')


list = %w[one two three]
p list

(1..5).each do |n|
  if n.even?
    p 'even'
  else
    p 'odd'
  end
end


br("split()")


base_string = 'abc def  ghi'

p base_string.split
p base_string.split('  ')
p base_string.split('d')
p base_string.split('efghi')


br('join()')


stringlist = %w[This is a sentence]
p stringlist
p stringlist.join(' ')
p stringlist.join(',')
p stringlist.join(' A SPACE ')


br('String interpolation')


first = 'Jack'
last = 'Black'
full_name = "#{first} #{last}"

p first
p last
p full_name

smith_brothers = %w[Terry Jerry Harry]

brd

smith_brothers.each { puts "#{_1} Smith" }


br("compact()")


list_compact = [1, nil, 2, nil, nil, 3, nil, []]
p list_compact
p list_compact.compact


br('flatten()')


list_flatten = [[1, [2, 3]], 4, [5, 6]]
p list_flatten
p list_flatten.flatten


br('push()')


list_push = (1..5).to_a
p list_push
p list_push.push(666)


br('pop()')


list_pop = (1..5).to_a
puts "list: #{list_pop}"
tail = list_pop.pop
puts "list.pop: #{tail}"
puts "list: #{list_pop}"


br('unshift()')


list_unshift = (1..5).to_a
puts "list: #{list_unshift}"
puts "list.unshift(666)"
list_unshift.unshift(666)
puts "list: #{list_unshift}"
