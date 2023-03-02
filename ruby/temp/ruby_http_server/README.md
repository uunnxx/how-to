# Ruby HTTP Server From the Ground Up


## How does HTTP look anyway?
HTTP is plaintext protocol implemented over TCP so we can easily inspect what requests look like (HTTP 2 is actually no longer plaintext, it's binary for efficiency purposes).
One way to look at request structure is to use curl with -v (verbose) flag:


> `curl http://google.com -H "x-some header: custom_header_value" -v

```
Outputs:


> GET / HTTP/1.1
> Host: google.com
> User-Agent: curl/7.74.0
> Accept: */*
> x-some header: custom_header_value
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 400 Bad Request
< Content-Type: text/html; charset=UTF-8
< Referrer-Policy: no-referrer
< Content-Length: 1555
< Date: Thu, 10 Feb 2022 07:43:05 GMT

doctype html...
html...

```


## The Plan:

- Let's define the steps we are going to need:
  - Listen on a local socket for incoming TCP connections
  - Read incoming request's data (text)
  - Parse the text of the request to extract method, path, query, headers and body from it
  - Send the response to the remote socket via the connection
  - Close the connection

With that in mind let's setup the general structure of our program:

```ruby
require 'socket'

class SingleThreadedServer
  PORT = ENV.fetch('PORT', 3000)
  HOST = ENV.fetch('HOST', '127.0.0.1').freeze
  # number of incoming connections to keep in a buffer
  SOCKET_READ_BACKLOG = ENV.fetch('TCP_BACKLOG', 12).to_i

  attr_accessor :app

  # app: a Rack app
  def initialize(app)
    self.app = app
  end

  def start
    socket = listen_on_socket
    loop do # continuously listen to new connections
      conn, _addr_info = socket.accept
      request = RequestParser.call(conn)
      status, headers, body = app.call(request)
      HttpResponder.call(conn, status, headers, body)
    rescue => e
      puts e.message
    ensure # always close the connection
      conn&.close
    end
  end
end

SingleThreadedServer.new(SomeRackApp.new).start

```


## Listening on a Socket

A 'full' version of the implementation of `listen_on_socket` looks like this:

```ruby
def listen_on_socket
  Socket.new(:INET, :STREAM)
  socket.setsockopt(Socket::SOL_SOCKET, Socket::SO_REUSEADDR, true)
  socket.bind(Addrinfo.tcp(HOST, PORT))
  socket.listen(SOCKET_READ_BACKLOG)
end
```

However, there's a lot of boilerplate here and all this code could be replaced with:

```ruby
def listen_on_socket
  socket = TCPServer.new(HOST, PORT)
  socket.listen.(SOCKET_READ_BACKLOG)
end

```

## Parsing a Request

Before we start let's define what an end should look like.
We want our server to be Rack compatible.
Here's an example I found of what Rack expects in its environment as a part of the request:


```

{
  "GATEWAY_INTERFACE"=>"CGI/1.1",
  "PATH_INFO"=>"/",
  "QUERY_STRING"=>"",
  "REMOTE_ADDR"=>"127.0.0.1",
  "REMOTE_HOST"=>"localhost",
  "REQUEST_METHOD"=>"GET",
  "REQUEST_URI"=>"http://localhost:9292/",
  "SCRIPT_NAME"=>"",
  "SERVER_NAME"=>"localhost",
  "SERVER_PORT"=>"9292",
  "SERVER_PROTOCOL"=>"HTTP/1.1",
  "SERVER_SOFTWARE"=>"WEBrick/1.3.1 (Ruby/2.2.1/2015-02-26)",
  "HTTP_HOST"=>"localhost:9292",
  "HTTP_ACCEPT_LANGUAGE"=>"en-US,en;q=0.8,de;q=0.6",
  "HTTP_CACHE_CONTROL"=>"max-age=0",
  "HTTP_ACCEPT_ENCODING"=>"gzip",
  "HTTP_ACCEPT"=>"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  "HTTP_USER_AGENT"=>"Mozilla/5.0 WebKit/537.36 (KHTML, like Gecko) Chrome",
  "rack.version"=>[1, 3],
  "rack.url_scheme"=>"http",
  "HTTP_VERSION"=>"HTTP/1.1",
  "REQUEST_PATH"=>"/"
}

```

























#### Source
- https://www.dmitry-ishkov.com/2021/07/ruby-http-server-from-ground-up.html
- https://www.dmitry-ishkov.com/2021/07/http-server-in-ruby-3-fibers-ractors.html
