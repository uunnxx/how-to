42
3.14159
"foo"

0x7FFF # hexidecimal
0o755 # octal

require 'fileutils'
include FileUtils

def chmod(permission, file)
  # chmod 755, 'somefile'
  #
  #    U  G  O
  #   rwxrwxrwx
  # 0b111101101
  # o
end

perms = 0b111101101
p perms.to_s(8) # 755

chmod perms, 'somefile'
