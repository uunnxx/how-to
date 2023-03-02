# Temperature Conversion
# Write a program that takes a temperature input in celsius and converts it to Fahrenheit and Kelvin. Return the converted temperature values in an array.

# The formula to calculate the temperature in Fahrenheit from Celsius is:
# F = C*9/5 +32

# The formula to calculate the temperature in Kelvin from Celsius is:
# K = C + 273.15

# Examples
# temp_conversion(0) ➞ [32, 273.15]
# # 0°C is equal to 32°F and 273.15 K.
# temp_conversion(100) ➞ [212, 373.15]
# temp_conversion(-10) ➞ [14, 263.15]
# temp_conversion(300.4) ➞ [572.72, 573.55]

# Notes
# Return calculated temperatures up to two decimal places.
# Return "Invalid" if K is less than 0.

# variant 1:
def temp_conversion(celsius)
  result = []
  fahrenheit = (celsius * 9 / 5 + 32).round(2)
  kelvin = (celsius + 273.15).round(2)

  if kelvin > 0
    result << fahrenheit << kelvin
  else
    "Invalid"
  end
end

# variant 2:
def temp_conversion(celsius)
  celsius >= -273.15 ? [celsius * 1.8 + 32, celsius + 273.15].map { |x| x.round(2) } : "Invalid"
end


# variant 3:
def temp_conversion(celsius)
  celsius < -273.15 ? 'Invalid' : [(celsius * 1.8 + 32).round(2), (celsius + 273.15).round(2)]
end


# variant 4:
def temp_conversion(c)
  f = (c*9/5 +32).round(2)
  k = (c + 273.15).round(2)

  return "Invalid" if k<0
  [f,k]
end


# variant 5:
def temp_conversion(celsius)
  kf = []
  kf.push ((celsius*9/5 +32).round(2))
  kf.push ((celsius + 273.15).round (2))

  if kf[1] < 0
    return "Invalid"
  else
    return kf
  end
end






