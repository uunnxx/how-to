require "open-uri"
require "async"

# sync
URI.open("https://httpbin.org/delay/2")
URI.open("https://httpbin.org/delay/2")
URI.open("https://httpbin.org/delay/2")


# async
1.upto(3).map do
  Thread.new do
    URI.open("https://httpbin.org/delay/2")
  end
end.each(&:join)


