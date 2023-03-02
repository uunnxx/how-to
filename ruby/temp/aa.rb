begin
    require 'ext_lib'
rescue LoadError
    $stderr.puts "std::err -- Using std_lib instead of ext_lib"
end

puts 'ttt'
