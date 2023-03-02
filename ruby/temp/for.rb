for i in (1..7).reverse_each do
  puts "Осталось #{i} секунд#{case i
  when 2..4 then "ы"
  when 1 then "а"
  else ""
  end }..."
  sleep(1)
end
puts "Готово!"


chars = 'a, b, c'

chars.split
