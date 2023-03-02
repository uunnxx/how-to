# chars = 'a,b,c'
#
# chars.split(',').length
#
# chars.size
#
# # require 'twitchbot'
#
# # Twitchbot.bot
#
#
# def main
#   something_doing
#
# end
#
#
# def tabs
# end
#

# def number(from=0, to=9999999, country_code=7, company_code=985)
#   template = "+#{country_code} #{company_code}"
#   # array = []
#   result = ""
#
#   from.upto(to) do |num|
#     puts result = "#{template} #{num.to_s.rjust(7, '0')}"
#     # array << result
#   end
#   # array
# end

def number(from=0, to=9999999, country_code=7, company_code=985)
  template = "+#{country_code} #{company_code}"
  result = ""
  i = 0

  while true
    puts result = "#{template} #{i.to_s.rjust(7, '0')}"
    i += 1
    break if i == to
  end
end



number
# puts number(100, 2000)


def main

end
