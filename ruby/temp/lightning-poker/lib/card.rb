# frozen_string_literal: true

class Card
  attr_reader :suit, :rank

  def self.build(suit, rank)
    new(suit: suit, rank: rank)
  end

  private_class_method :new

  def initialize(suit:, rank:)
    @suit = suit
    @rank =
      case rank
      when :jack then 11
      when :queen then 12
      when :king then 13
      else rank
      end
  end

  def ==(other)
    rank == other.rank && suit == other.suit
  end

  def hash
    [rank, suit].hash
  end

  def eql?(other)
    self == other
  end
end
