require 'socket'

# Socket.unix_server_loop("/home/baka/.mpv/socket") do |sock, client_addrinfo|
#   begin
#     IO.copy_stream(sock, sock)
#   ensure
#     sock.close
#   end
# end

s = UNIXSocket.new("/home/baka/.mpv/socket")
# s.send "{'command': ['get_property', 'filename']}", 0
# s.send "command", 0
# p s.addr
# p s.local_address
# p s

p s.gets
# p s.recv(100)
#
puts

# Socket.unix("/home/baka/.mpv/socket") do |sock|
#   t = Thread.new { IO.copy_stream(sock, $stdout) }
#   IO.copy_stream($stdin, sock)
#   t.join
# end


