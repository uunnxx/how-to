require_relative 'enum'


class Country < Enum
  enum_value :RUSSIA, 1
  enum_value :USA, 2
end

puts Country::RUSSIA              # <Country::RUSSIA value=1>
p Country::RUSSIA.is_a?(Country)  # true

p Country.values

country1 = Country::RUSSIA
country2 = Country::RUSSIA
p country1 == country2            # true


# Errors

class Country < Enum
  enum_value :RUSSIA, 1
  enum_value :RUSSIA, 2           # raise
end

class Country < Enum
  enum_value :RUSSIA, 1
  enum_value :USA, 1              # raise
end

Country.new(:China, 3)            # raise
