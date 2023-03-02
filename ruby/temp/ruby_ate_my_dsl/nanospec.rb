# https://www.youtube.com/watch?v=Ov-tMtOkKS4

class Entity
  def initialize name
    @name = name
    @specs = {}
  end

  def it name, &block
    @specs[name] = block
  end

  def check
    @specs.each do |spec, block|
      puts "** #{@name} #{spec}"
      block.call
    end
  end
end


module Kernel
  def describe name, &block
    entity = Entity.new name
    (@entities ||= []) << entity
    entity.instance_eval &block
  end
end


at_exit do
  @entities.each { |entity| entity.check }
end
