# frozen_string_literal: true

require 'rbs'
require 'nokogiri'

class Fate
  NAMES = %w[Klotho Atropos Lachesis].freeze
  @@number_instantiated = 0

  def initialize
    if @@number_instantiated >= NAMES.size
      raise ArgumentError, 'Sorry, there are only three Fates.'
    end

    @name = NAMES[@@number_instantiated]
    @@number_instantiated += 1
    puts "I give you... #{@name}!"
  end
end

Fate.new

Fate.new

Fate.new

Fate.new

class Module
  def class_attr_reader(*symbols)
    symbols.each do |symbol|
      self.class.send(:define_method, symbol) do
        class_variable_get("@@#{symbol}")
      end
    end
  end

  def class_attr_writerr(*symbols)
    symbols.each do |symbol|
      self.class.send(:define_method, "#{symbol}=") do |value|
# frozen_string_literal = true

        class_variable_set("@@#{symbol}", value)
      end
    end
  end

  def class_attr_accessor(*symbols)
    class_attr_reader(*symbols)
    class_attr_writerr(*symbols)
  end
end

class Fate
  class_attr_reader :number_instantiated
end


class Package
  def initialize(pkg)
    @pkg = pkg
  end

  def self.send_as_package(obj)
    if obj.respond_to? :package
      packaged = obj.package
    else
      warn "Not sure how to package a #{obj.class}."
      warn 'Trying generic packager.'
      packaged = Package.new(obj)
    end
    packaged
  end
end

def multiply_precisely(a: Integer, b: Integer)
  a * b
end

multiply_precisely(4, 5)

multiply_precisely(4.0, 5)

def append_to_self(x: Array)
  unless x.respond_to? :<<
    raise ArgumentError,
      'This object does not support the left-shift operator.'
  end

  if x.is_a? Numeric
    raise ArgumentError,
      'The left-shift operator for this object does not do an append.'
  end

  x << x
end

append_to_self('abc')
append_to_self([1, 2, 3])
append_to_self({ 1 => 2 })


module ShiftMeansAppend
  def <<(x)
  end
end

class String
  include ShiftMeansAppend
end

class Array
  include ShiftMeansAppend
end

def append_to_self(x)
  unless x.is_a?(ShiftMeansAppend)
    raise ArgumentError, 'I cannot trust this object\'s left-shift operator.'
  end

  x << x
end

append_to_self 4
append_to_self '4'
