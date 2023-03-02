# https://www.reddit.com/r/ruby/comments/q0lrmf/add_to_specific_elements_of_an_array_the_ruby_way/
require 'pry'
require 'byebug'
require 'nokogiri'


def array_element_update2(array)
  'duplicate_method' << array
end

def array_element_update(array)
  array_new = []
  array.each_with_index do |element, index|
    if index >= 1 && index <= 3
      element = element + 3
    end
    array_new.append(element)
    binding.pry
  end
  array_new
end



module MMMM
  class Main
    def main
      some_value
    end

    def mmm
      puts 'string'
    end

    def some_value
      'ttt'
    end
  end

  def main
    'ttt'
  end

  def mmm

  end
end

array = [1, 2, 3, 4, 5]

puts array_element_update(array)


def array_element_update(array)
  array.map.with_index do |element, index|
    (1..3).include?(index) ? element + 3 : element
  end
end

[1, 2, 3, 4, 5].map.with_index do |number, index|
  index >= 1 && index <= 3 ? number += 3 : number
  number
end

def main; end

def do_stuff(array)
  array.map.with_index do |n, i|
    if (1..3).cover? i
      n += 3
    else
      n
    end
    n
  end
end

class Class
  def descendants
    ObjectSpace.each_object(::Class).select { |klass| klass < self }
  end
end



def main
  do_stuff
  t
  ti

end

Nokogiri::VersionInfo
Nokogiri::HTML5::Document::PI_NODE

attr_accessor :main
attr_protected :clear


def main

end

class Main
  def initialize
    
  end
end

def mamm
  '.'.each_char do |x|
    x
  end
end


Nokogiri::HTML5::Node::PI_NODE




def method_name
  
end
