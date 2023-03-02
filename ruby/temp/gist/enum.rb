class Enum
  attr_reader :name
  attr_reader :value

  def initialize(name, value)
    @name = name
    @value = value
  end

  def to_i
    value.to_i
  end

  def to_sym
    name.to_sym
  end

  def to_s
    "<#{self.class.name}::#{name} value=#{value}>"
  end
  
  class << self
    def enum_value(name, value)
      @@values ||= []

      raise 'Name already exists' if @@values.detect { |item| item.name == name }
      raise 'Value already exists' if @@values.detect { |item| item.value == value }

      new_value = new(name, value)
      @@values << new_value

      const_set(name, new_value)
    end

    def values
      @@values ||= []
    end

    private

    def new(*args)
      super
    end
  end
end
