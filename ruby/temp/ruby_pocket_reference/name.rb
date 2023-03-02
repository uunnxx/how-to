class Name
  attr_accessor :family_name, :given_name

  # def family_name=(family)
  #   @family_name = family
  # end
  #
  # def given_name=(given)
  #   @given_name = given
  # end
  #
  # def family_name
  #   @family_name
  # end
  #
  # def given_name
  #   @given_name
  # end

  def to_s
    "-----------------------------------------\n" \
    ">>>> Name: #{@family_name} #{@given_name}\n" \
    "-----------------------------------------\n"
  end
end

n = Name.new
n.family_name = "Matsumoto"
n.given_name = "Yukihiro"
puts n
p n
