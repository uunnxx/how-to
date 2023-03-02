require 'time'

module TimeMachine
  refine Time do
    def to_s
      hour <= 12 ? 'Sleep on!' : super
    end
  end
end


class Earth
  using TimeMachine

  def morning
    Time.parse('09:00').to_s
  end

  def afternoon
    Time.parse('13:00').to_s
  end
end

p Earth.new.morning
p Earth.new.afternoon
