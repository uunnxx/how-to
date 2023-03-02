## Errors

- LoadError
```
begin
    require 'ext_lib'
rescue LoadError
    $stderr.puts "Using std_lib instead of ext_lib"
end
```
