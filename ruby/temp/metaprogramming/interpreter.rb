# frozen_string_literal: true

class Interpreter
  def run(_response, cmd)
    send(cmd)
  end

  def method_missing(m, *args, &block)
    puts 'Hi there'
  end
end
