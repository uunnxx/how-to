bad_slug = "Th!s !$ @ horrible slug"
good_slug = "This is a better slug"

def convent_to_slug(str)
  return "Sorry, that's not valid" if str.include?("$")
  str.gsub(" ", "-").downcase
end

puts
puts convent_to_slug(bad_slug)
puts convent_to_slug(good_slug)
