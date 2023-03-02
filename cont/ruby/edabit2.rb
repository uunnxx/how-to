# Write a function that returns the string "something" joined with a space " " and the given argument a

def give_me_something(a)
  "something " << a
end


# Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

# Notes
# n will always be greater than 2.
# The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.

def sum_polygon(n)
  if n >= 2
    (n - 2) * 180
  end
end



# Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

# wins get 3 points
# draws get 1 point
# losses get 0 points
def football_points(wins, draws, losses)
  (wins * 3) + draws
end

# Find the Unique Letters
# Create a function that takes a string and returns the letters that occur only once
# variant 1:
def find_letters(word)
  tmp = []
  word.each_char do |char|
    unless (word.scan(char).length > 1)
      tmp << char
    end
  end
  tmp
end

# variant 2:
def find_letters(word)
  word.chars.select { |x| word.count(x) == 1 }
  # word.chars.select { |x| word.count(x) < 2 }
end

# variant 3:
def find_letters(word)
  hash = Hash.new(0)
  word.each_char { |char| hash[char] += 1 }
  hash.select { |k, v| v == 1 }.keys
end

def find_letters(word)
  word.chars.uniq.map { |char| char if word.count(char) == 1 }.compact
end

def find_letters(word)
  arr = []
  word.chars.each do |char|
    arr < c if word.count(char) == 1
  end
end

def find_letters(word)
  word.split(//).select { |char| word.count(char) == 1 }
end



