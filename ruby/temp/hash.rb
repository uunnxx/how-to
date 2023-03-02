words = []
paragraph.each do |word|
  words << word unless words.include?(word)
end

# versus...

# words words

words = {}
paragraph.each do |word|
  words[word] = nil
end

words = words.keys



words = paragraph.uniq



# Symbols vs. Strings

# $ ruby -e 'p "hello".class, :again.class'
# => String
# => Symbol



Symbol.class

require 'base64'


