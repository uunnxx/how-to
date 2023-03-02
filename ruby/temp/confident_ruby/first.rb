#def location(item, value)
#  sub_table = get_sub_table(item, value)
#  if (sub_table.length == 0)
#    raise MetricFu::AnalysisError, "The #{item.to_s} '#{value.to_s}'"\
#      'does not have any rows in the analysis table'
#  else
#    first_row = sub_table[0]
#    case item
#    when :class
#      MetricFu::Location.get(
#        first_row.file_path,
#        first_row.class_name,
#        nil
#      )
#    when :method
#      MetricFu::Location.get(
#        first_row.file_path,
#        first_row.class_name,
#        first_row.method_name
#      )
#    when :file
#      MetricFu::Location.get(
#        first_row.file_path,
#        nil,
#        nil
#      )
#    else
#      raise ArgumentError, 'Item must be :class, :method, or :file'
#    end
#  end
#end

#def import_legacy_purchase_data(data)
#  purchase_list = legacy_dataparser.parse_purchase_records(data)
#  purchase_list.each do |purchase_record|

#    customer = customer_list.get_customer(purchase_record.email_address)
#    product = product_inventory.get_product(purchase_record.product_id)
#    customer.add_purchased_product(product)
#    customer.notify_of_files_available(product)
#    log_successful_import(purchase_record)

#  end
#end

#CSV.new(data, headers: true, converters: [:data]).each do |purchase_record|
#  #...
#  customer.add_purchased_product(product)
#  #...
#end

#@logger && @logger.info "Imported purchase ID #{purchase_record.id}"


## 3.1 Introduction to collecting input
## It is possible for a method to receive no input whatsoever, but such methods
## don't usually accomplish much. Here's one such method: it simply returns
## the number of seconds in a day.

#def seconds_in_day
#  24 * 60 * 60
#end

## This method could just as easily be a constant:

#SECONDS_IN_DAY = 24 * 60 * 60

## Most methods receive input in some form or other. Some types of input are more
## obvious than others. The most unambiguous form of input is an argument:

#def seconds_in_day(num_days)
#  num_days * 24 * 60 * 60
#end

## Input can also in the form of a constant value specified in a class or module
## the method has access to.

#class TimeCalc
#  SECONDS_IN_DAY = 24 * 60 * 60

#  def seconds_in_day(num_days)
#    num_days * SECONDS_IN_DAY
#  end
#end

## Or an instance variable.

#class TimeCalc
#  def initialize
#    @start_date = Time.now
#  end

#  def time_n_days_from_now(num_days)
#    @start_date + num_days * 24 * 60 * 60
#  end
#end

#TimeCalc.new.time_n_days_from_now(2) # => 2022-20-20 20:20:20 -0200

#def format_time4
#  format = ENV.fetch('TIME_FORMAT') { '%D %r' }
#  Time.new.strftime(format)
#end

#format_time

#ENV['TIME_FORMAT'] = '%FT%T%:z'
#format_time


#require 'yaml'

#def format_time3
#  prefs = YAML.load_file('time-prefs.yml')
#  format = prefs.fetch('format') { '%D %r' }
#  Time.new.strftime(format)
#end

#IO.write('time-prefs.yml', <<EOF)
#---
#format: "%A, %B %-d at %-I:%M %p"
#EOF

#format_time

#require 'yaml'

#def format_time
#  user = ENV['USER']
#  prefs = YAML.load_file("/home/#{user}/time-prefs.yml")
#  format = prefs.fetch('format') { '%D %r' }
#  Time.now.strftime(format)
#end

#def format_time2
#  user = ENV['USER']
#  prefs = YAML.load_file("/home/#{user}/time-prefs.yml")
#  format = prefs.fetch('format') { '%D %r' }

#  Time.new.strftime(format)
#end

# winners = [
#   'Homestar',
#   'King of Town',
#   'Marzipan',
#   'Strongbad'
# ]

# Place = Struct.new(:index, :name, :prize)

# first = Place.new(0, 'first', 'Peasant\'s Quest game')
# second = Place.new(1, 'second', 'Limozeen Album')
# third = Place.new(2, 'third', 'Butter-da')

# # We'd like to announce the winners of teh race. We can do this with loop.

# [first, second, third].each do |place|
#   puts "In #{place.name} place, #{winners[place.index]}!"
#   puts "You win: #{place.prize}!"
# end


# Place = Struct.new(:index, :name, :prize) do
#   def to_int
#     index
#   end
# end


class VimConfigFile
  def initialize
    @filename = "#{ENV['HOME']}/.vimrc"
  end

  def to_path
    @filename
  end
end

vim_config = VimConfigFile.new


line_num = 0

File.foreach(vim_config) do |line|
  line_num += 1
end

p 'Line numbers: ' << line_num.to_s
