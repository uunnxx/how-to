# frozen_string_literal: true

require 'nokogiri'
require 'open-uri'

# Fetch and parse HTML document
# doc = Nokogiri::HTML(URI.open('https://nokogiri.org/tutorials/installing_nokogiri.html'))

# Search for nodes by css
# doc.css('nav ul.menu li a', 'article h2').each do |link|
#   puts link.content
# end

# Search for nodes by xpath
# doc.xpath('//nav//ul//li/a', '//article//h2').each do |link|
#   puts link.content
# end

# Or mix and match
# doc.search('nav ul.menu li a', '//article//h2').each do |link|
#   puts link.content
# end

# doc = Nokogiri::HTML5(<<-EOF)
# <!DOCTYPE html>
# <pre>
# Content</pre>
# EOF
# puts doc.at('/html/body/pre').serialize
#

# doc = Nokogiri::HTML5("<!DOCTYPE html><span>Hello world!</span>")
# puts doc.serialize

# doc = Nokogiri::HTML5.parse('<span/>Hi there!</span foo=bar />', max_errors: 10)
# doc.errors.each do |err|
#   puts("#{err.line}:#{err.column}: #{err.str1}")
# end
