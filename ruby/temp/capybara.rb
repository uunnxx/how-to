require 'minitest'
require 'capybara/dsl'

class CapybaraTestCase < Test::Unit::TestCase
  include Capybara::DSL

  def teardown
    Capybara.reset_sessions!
    Capybara.use_default_driver
  end
end

CapybaraTestCase.allocate.class.allocate.class
