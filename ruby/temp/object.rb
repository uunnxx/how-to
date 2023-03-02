def br
  puts "\n#{'-' * 80}\n\n"
end

br

puts "SELF"
p self
p self.class

br

puts "MODULE"
p Module.class
p Module.ancestors
p Module.constants
p Module.class_variables

br

puts "OBJECT"
p Object.class
p Object.methods
p Object.instance_variables
p Object.instance_methods
p Object.instance_methods(false)
p Object.ancestors

br

puts "KERNEL"
p Kernel.class
p Kernel.ancestors

br

puts "BASICOBJECT"
p BasicObject.class
p BasicObject.ancestors
p BasicObject.methods
p BasicObject.instance_methods
p BasicObject.instance_variables
p BasicObject.constants

br

p Class.ancestors
