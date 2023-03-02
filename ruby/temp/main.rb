class User
  def invite(message)
    InvitationMailer.invitation(message).deliver_later
    @invited = true
  end

  def invite!(message)
    invite(message)
    save!
  end
end


module Main
  class Person
    def pp
      class < self
        def main

        end

      end

    end
  end

  class Test
    def stne

    end

    def aaa

    end
  end

  class tsaest
    def initialize

    end

    def staeo

    end
  end
end

class UsersController < ApplicationController
  def invite
    @user.invite!(params[:message])
  end
end
