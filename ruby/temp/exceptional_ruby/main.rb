# begin
#   fail 'Oops';
# rescue => e
#   raise if e.message != 'Oops'
# end


# def assert(value)
#   raise(RuntimeError, 'Doh!', caller) unless value
# end

# assert(5 == 5)


# module RaiseExit
#   def raise(msg_or_exc, msg=msg_or_exc, trace=caller)
#     warn msg.to_s
#     exit!
#   end
# end

# module Kernel
#   include RaiseExit
# end

# def raise(klass, message, backtrace)
#   error = klass.new(message)
# end

# require 'net/http'

# class Net::HTTPInternalServerError
#   def exception(message = 'Internal server error')
#     RuntimeError.new(message)
#   end
# end

# class Net::HTTPNotFound
#   def exception(message = '404 Not Found')
#     RuntimeError.new(message)
#   end
# end

# response = Net::HTTP.get_response(URI.parse('http://avdi.org/notexist'))

# if response.code.to_i >= 400
#   raise response
# end

# def foo
#   puts '#caller: '
#   puts *caller
#   puts '------------'
#   puts '#caller(0)'
#   puts *caller(0)
# end

# def bar
#   foo
# end

# bar


# require 'English'
# puts $!.inspect

# begin
#   raise 'Oops'
# rescue
#   puts $!.inspect
#   puts $ERROR_INFO.inspect
# end

# puts $!.inspect


10.downto 1 do
  puts 'I love ruby'
end

10 upto 20

10.downto.1

class Department
  def resources(*res)
    @no_of_people = res[0]
    @no_of_comp = res[1]

    return @no_of_people, @no_of_comp
  end
end

def Department.employee_appraisal
  puts 'Employee appraisal happens once a year'
end

class Customer
  def initialize(name, age, sex, amt, &purchases)
    @name = name
    @age = age
    @sex = sex
    @purchases = purchases
    @amt = amt
    @purchases.call(@amt, @name)
  end
end


Department.employee_appraisal

Dept1 = Department.new
y = Dept1.resources(25, 10)
puts "Number of people are #{y[0]}"
puts "Number of computers are #{y[1]}"
