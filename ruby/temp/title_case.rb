# A string is considered to be in title case if each word in the string is
# either (a) capitalised (that is, only the first letter of the word is
# in upper case) or (b) considered to be an exception and put entirely
# into lower case unless it is the first word, which is always capitalised.
#
# Write a function that will convert a string into title case,
# given an optional list of exceptions (minor words).
# The list of minor words will be given as a string with each
# word separated by a space. Your function should ignore
# the case of the minor words string -- it should behave in the same way
# even if the case of the minor word string is changed.
#
# ###Arguments (Haskell)
#
# First argument: space-delimited list of minor words
# that must always be lowercase except for the first word in the string.
# Second argument: the original string to be converted.
# ###Arguments (Other languages)
#
# First argument (required): the original string to be converted.
# Second argument (optional): space-delimited list of minor words
# that must always be lowercase except for the first word in the string.
# The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
# ###Example
#  KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'

def title_case(title, minor_words = '')
  downcase = title.downcase.split(' ')
  minor = minor_words.downcase.split(' ')
  result = []

  # downcase.map do |word|
  #   word.
  # end

  downcase.map { |word| result << word.capitalize } if minor_words.empty?
  downcase.map do |word|
    result << word if minor.include?(word)
    result << word.capitalize unless minor.include?(word)
  end

  # result[0].capitalize!
  # result = result.join(' ')
  puts result[0]
  puts result.class
end

# By zishee
# def title_case(title, minor_words = '')
#   title.capitalize.split().map{|a| minor_words.downcase.split().include?(a) ? a : a.capitalize}.join(' ')
# end

# By viorel
# def title_case(title, minor_words='')
#   minor_words = minor_words.downcase.split(' ')
#   title.capitalize.split(' ').map { |word| minor_words.include?(word.downcase) ? word : word.capitalize }.join(' ')
# end

# By Willux
# def title_case(title, minor_words = "")
#   title = title.split(" ").map { |w| minor_words.split(" ").map { |ww| ww.downcase }.include?(w.downcase) ? w.downcase : w.capitalize  }.join(" ")
#   title.length > 0 ? title[0].capitalize + title[1..-1] : ""
# end



title_case('', '')
title_case('a clash of KINGS', 'a an the of')
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')
