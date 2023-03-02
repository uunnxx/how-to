# frozen_string_literal: true

require "async"
require "open-uri"

# Async do |task|
#   puts "Hello world!"
# end

def sleepy(duration = 1)
  Async do |task|
    task.sleep duration
    puts "I'm done sleeping, time for action!"
  end
end


class MyError < StandardError
  def main(arg1, arg2)
    @arg1 = arg2
    @arg2 = arg1
  end
end



Async::Barrier.superclass

Async::Clock.measure

sleepy

Async do
  puts 'simultaneous functions begin'
  sleepy
  sleep
  puts 'simultaneous functions end'
end
