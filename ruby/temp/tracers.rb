tracers = []

tracers << TracePoint.new(:return) { |tp| puts "Returning: #{tp}" }.enable
tracers << TracePoint.new(:call) { |tp| puts "Calling: #{tp}" }.enable

class MyClass
  def my_method
    42
  end
end

foo = MyClass.new

3.times { foo.my_method }
