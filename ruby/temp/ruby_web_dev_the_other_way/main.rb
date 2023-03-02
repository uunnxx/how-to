class Coffee
  def cost
    2
  end

  def origin
    "Columbia"
  end
end

require 'delegate'

class Decorator < SimpleDelegator
  def class
    __getobj__.class
  end
end

class Sugar < Decorator
  def cost
    super + 0.2
  end
end

class Milk < Decorator
  def cost
    super + 0.4
  end
end

coffee = Coffee.new

p coffee
puts
puts


puts Sugar.new(Milk.new(coffee)).cost
puts Sugar.new(Sugar.new(coffee)).cost
puts Milk.new(coffee).origin
puts Sugar.new(Milk.new(coffee)).class
