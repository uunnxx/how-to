##### A simple Class to track an employee's understanding of the word "Fraud"

class Employee
  def initialize
    @embezzled = []
  end



  # def embezzled(amount)
  #   @embezzled << amount
  # end

  # def embezzled_total
  #   @embezzled.inject(0) { |sum, amount| sum + amount }
  # end
  # Improving the Employee Class to Instantiate the @embezzled Array Lazily
  def embezzled(amount)
    (@embezzled ||= []) << amount
  end

  def embezzled_total
    (@embezzled || []).inject(0) { |sum, amount| sum + amount }
  end

  def embezzle(amount)
    (@embezzled ||= []) << amount
    # (@embezzled_total ||= 0) += amount
  end

  # def embezzled_total
  #   (@embezzled_total || 0)
  # end
end
