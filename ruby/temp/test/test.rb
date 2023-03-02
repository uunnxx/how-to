class Movie
  def initialize(title, rank = 0)
    @title = title.capitalize
    @rank = rank
  end

  def to_s
    "#{@title} has a rank of #{@rank}"
  end

  def +@
    puts "#{@title} has a rank of #{@rank}"
  end
end

movie1 = Movie.new('goonies', 10)
movie2 = Movie.new('ghostbusters', 9)
movie3 = Movie.new('goldfinger')

puts movie1
puts movie2
puts movie3

+movie1
+movie2
+movie3
