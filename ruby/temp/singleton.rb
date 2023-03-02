class Foo
  def singleton_method_removed(name)
    puts "singleton method \"#{name}\" was removed"
  end
end

obj = Foo.new
def obj.foo
end

def obj.bar() end



class << obj
  remove_method :foo
  remove_method :bar
end

def hello() :hello end


# Endless method

def the_answer = 42
def get_x = @x
def square(x) = x * x:q



def main

end

defined?

define_singleton_method()
IOError.attr.===()


Errno::ENOMEM


Errno::EEXIST.new()



Errno::EBADEXEC.new()
erro
a




