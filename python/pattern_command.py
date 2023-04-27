"The Command Pattern Concept"
from typing import Protocol

class ICommand(Protocol):
    '''The command interface, that all commands will implement'''
    def execute():
        '''The required execute method that all command objects will use'''
        ...


class Invoker:
    '''The Invoker Class'''

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        '''Register commands in the Invoker'''
        self._commands[command_name] = command

    def execute(self, command_name):
        '''Execute any registered commands'''
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class ISwitchable(Protocol):
    '''The  interface for a Receiver'''

    @staticmethod
    def power_on():
        ''' power on action method'''
        ...

    @staticmethod
    def power_off():
        ''' power off action method'''
        ...


class Switch:
    "The Receiver"

    @staticmethod
    def power_on():
        '''A set of instructions to run'''
        print("Turning power on")

    @staticmethod
    def power_off():
        '''A set of instructions to run'''
        print("Turning power off")


class OpenSwitchCommand:
    '''A Command object, that implements the ICommand interface and
    runs the command on the designated receiver'''

    def __init__(self, receiver: ISwitchable):
        self._receiver = receiver

    def execute(self):
        self._receiver.power_on()


class CloseSwitchCommand:
    '''A Command object, that implements the ICommand interface and
    runs the command on the designated receiver'''

    def __init__(self, receiver: ISwitchable):
        self._receiver = receiver

    def execute(self):
        self._receiver.power_off()


# The CLient
# Create a receiver
receiver = Switch()

# Create Commands
open_switch_command = OpenSwitchCommand(receiver)
close_switch_command = CloseSwitchCommand(receiver)

# Register the commands with the invoker
Invoker = Invoker()
Invoker.register("1", open_switch_command)
Invoker.register("2", close_switch_command)

# Execute the commands that are registered on the Invoker
Invoker.execute("1")
Invoker.execute("2")
