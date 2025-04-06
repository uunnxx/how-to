import argparse


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A simple CLI tool')

        # Define commands
        subparser = self.parser.add_subparsers(dest='command', help='Available commands')

        # Define sub-command: greet
        parser_greet = subparser.add_parser('greet', help='Greet the user')
        parser_greet.add_argument('name', help='Name of the user to greet')

        # Define sub-command: calculate
        parser_calc = subparser.add_parser('calculate', help='Perform a calculation')
        parser_calc.add_argument('num1', type=float, help='First number')
        parser_calc.add_argument('num2', type=float, help='Second number')
        parser_calc.add_argument(
            '--operation',
            choices=['add', 'subtract', 'multiple', 'divide'],
            default='add',
            help='Operation to perform (default: add)'
        )

    def run(self):
        args = self.parser.parse_args()

        if args.command == 'greet':
            self.greet(args)
        elif args.command == 'calculate':
            self.calculate(args)

    def greet(self, args):
        print(f"Hello, {args.name}")

    def calculate(self, args):
        if args.operation == 'add':
            result = args.num1 + args.num2
        elif args.operation == 'subtract':
            result = args.num1 - args.num2
        elif args.operation == 'multiply':
            result = args.num1 * args.num2
        elif args.operation == 'divide':
            result = args.num1 / args.num2 if args.num2 != 0 else 'Divide by zero!'

        print(f"Result of {args.num1} {args.operation} {args.num2} = {result}")


if __name__ == '__main__':
    cli = CLI()
    cli.run()
