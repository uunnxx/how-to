# frozen_string_literal: true

require 'set'
require 'card'

RSpec.describe 'a playing card' do
  def card(params = {})
    defaults = {
      suit: :hearts,
      rank: 7
    }
    Card.build(*defaults.merge(params).values_at(:suit, :rank))
  end

  # Methods
  # it: Specify a property. "Example"
  # describe: Group examples/properties.

  it 'has a suit' do
    raise unless card(suit: :spades).suit == :spades
  end
  it 'has a rank' do
    raise unless card(rank: 4).rank == 4
  end

  context 'equality' do
    subject { card(suit: :spades, rank: 4) }
    # let(:subject) { card(suit: :spades, rank: 4) }
    # def subject
    #   @subject ||= card(suit: :spades, rank: 4)
    # end

    describe 'comparing against self' do
      let(:other) { card(suit: :spades, rank: 4) }
      # def other
      #   @other ||= card(suit: :spades, rank: 4)
      # end

      it 'is equal' do
        # subject = card(suit: :spades, rank: 4)
        # other = card(suit: :spades, rank: 4)

        raise unless subject == other
      end

      it 'is hash equal' do
        # subject = card(suit: :spades, rank: 4)
        # other = card(suit: :spades, rank: 4)

        raise unless Set.new([subject, other]).size == 1
      end
    end

    shared_examples 'an unequal card' do
      it 'is not equal' do
        raise unless subject != other
      end

      it 'is not hash equal' do
        raise unless Set.new([subject, other]).size == 2
      end
    end

    describe 'comparing to a card of different suit' do
      let(:other) { card(suit: :spades, rank: 5) }
      # def other
      #   @other ||= card(suit: :hearts, rank: 4)
      # end

      it_behaves_like 'an unequal card'
    end

    describe 'comparing to a card of different rank' do
      let(:other) { card(suit: :spades, rank: 5) }
      # def other
      #   @other ||= card(suit: :spades, rank: 5)
      # end

      it_behaves_like 'an unequal card'
    end
  end

  describe 'a jack' do
    it 'ranks higher than a 10' do
      lower = card(rank: 10)
      higher = card(rank: :jack)

      raise unless higher.rank > lower.rank
    end
  end

  describe 'a queen' do
    it 'ranks higher than a jack' do
      lower = card(rank: :jack)
      higher = card(rank: :queen)

      raise unless higher.rank > lower.rank
    end
  end

  describe 'a king' do
    it 'ranks higher than a queen' do
      lower = card(rank: :queen)
      higher = card(rank: :king)

      raise unless higher.rank > lower.rank
    end
  end
end
