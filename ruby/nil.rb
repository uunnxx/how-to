class Person
  attr_reader :name

  def initialize(name)
    @name = name
  end

  def self.find(id)
    people = { 1 => new('alice'), 2 => new('bob') }
    # people[id]
    people.fetch(id)
  end
end


class SubscriptionController
  def create(person_id)
    person = Person.find(person_id)
    Subscription.create_for_person(person)
  end
end


class Subscription
  def self.create_for_person(person)
    create!(person:, person_name: person.name)
  end

  def self.create!(*args)
  end
end


SubscriptionController.new.create(3)
