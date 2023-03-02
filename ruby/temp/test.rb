class MyApp
  class << self
    def config
      @config ||= Configuration.new
    end

    def configure
      yield config
    end
  end

  class Configuration
    attr_reader :app_id, :title, :cookie_name

    puts 'inner class: Configuration'
  end

  class Tttt
    def main
      'return value'
    end
  end
end
