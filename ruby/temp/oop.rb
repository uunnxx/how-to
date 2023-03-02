class Invoice
  attr_accessor :customer, :total

  def summary
    puts 'Invoice:'
    puts "Customer: #{customer}"
    puts "Total: #{total}"
  end
end


# Implementing instantiation
# Now that we have our class definition, we can create a new instance of `Invoice` and
# store it in a variable, as shown here:

invoice = Invoice.new
invoice.customer = 'customer name'
invoice.total = 'sum of total 22527'
puts invoice.customer
puts
invoice.summary
