def br
  puts ' ' * 80
  puts '-' * 80
  puts ' ' * 80
end

br

# Ruby’s self keyword (and implicit self)
# self is a reserved keyword in Ruby that always refers to an object, but the object self refers to frequently changes based on the context. When methods are called without an explicit receiver, Ruby sends the message to the object assigned to the self keyword. Calling methods without an explicit receiver is common, so understanding the object assigned to the keyword self at any time is essential.

# self is initially set to main, an instance of the Object class that is automatically created whenever a Ruby program is interpreted. The main object is the ‘top-level’ namespace of the program.

p self # the main object
# In a class definition (but not in an instance method), the self keyword refers to the class itself.

br

class Dog
  p self # the Dog class
end

br
# In singleton methods, the self keyword also refers to the class itself.

class Dog
  def self.about
    self
  end
end
 
p Dog.about # Dog
# In instance methods, the self keyword refers to instances of the class.

br

class Dog
  def bark
    self
  end
end
 
p Dog.new.bark # an instance of the Dog class
# In modules, self refers to the module itself.

br

module Cab
  p self # Cab
end
# self refers to an instance of a class if it’s defined in a module that’s mixed in to the class.

br

module Cab
  def hi
    self
  end
end
 
class Cat
  include Cab
end
 
p Cat.new.hi # instance of the Cat class
# When a method is called without an explicit self, the implicit self is used, which is the value of the self keyword. In the following example, the Person#full_name method uses the values from Person#first_name and Person#last_name, but does not explicitly use self and relies on the value of the implicit self.

br

class Person
  attr_reader :first_name, :last_name
 
  def initialize(first_name, last_name)
    @first_name = first_name
    @last_name = last_name
  end
 
  def full_name
    "#{first_name} #{last_name}"
  end
end

p Person.new('John', 'Smith').full_name

# Relying on the implicit self can save quite a bit of typing over time and is very common among Ruby programmers.

br
