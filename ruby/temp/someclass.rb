class SomeClass
  def method_that_calls_proc_or_lambda(procy)
    puts "calling #{proc_or_lambda(procy)} now!"
    procy.call
    puts "#{proc_or_lambda(procy)} gets called!"
  end

  def proc_or_lambda(proc_like_thing)
    proc_like_thing.lambda? ? 'Lambda' : 'Proc'
  end
end

c = SomeClass.new
c.method_that_calls_proc_or_lambda lambda { return }

puts '-' * 80

h = SomeClass.new
h.method_that_calls_proc_or_lambda proc { return }
