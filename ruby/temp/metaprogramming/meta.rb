# frozen_string_literal: true

require_relative 'interpreter'

class Meta
  def initialize
    @interpreter = Interpreter.new
  end

  def run
    printf '> '
    @cmd = gets.gsub("\n", "")

    @response = @interpreter.run(@response, @cmd)
  end
end

meta = Meta.new
meta.run
