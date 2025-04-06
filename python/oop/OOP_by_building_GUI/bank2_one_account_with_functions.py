# Non-OOP
# Bank Version 2
# Single account

account_name = ''
account_balance = 0
account_password = ''


def new_account(name, balance, password):
    global account_name, account_balance, account_password

    account_name = name
    account_balance = balance
    account_password = password

def show():
    global account_name, account_balance, account_password

    print(f"\tName: {account_name}")
    print(f"\tBalance: {account_balance}")
    print(f"\tPassword: {account_password}")
    print()

def get_balance(password: str) -> None | int:
    global account_name, account_balance, account_password

    if password != account_password:
        print('Incorrect password')
        return None
    return account_balance

def deposit(amount_to_deposit, password):
    global account_name, account_balance, account_password

    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != account_password:
        print('Incorrect password')

    account_balance += amount_to_deposit
    return account_balance

def withdraw(amount_to_withdraw, password):
    global account_name, account_balance, account_password

    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != account_password:
        print('Incorrect password for this accountt')
        return None

    if amount_to_withdraw > account_balance:
        print('You cannot withdraw more than you have in you account')
        return None

    account_balance -= amount_to_withdraw
    return account_balance


new_account('Joe', 100, 'soup')


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do?').lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance: ')
        user_password = input('Please enter the password: ')
        if user_password != account_password:
            print('Incorrect password')
        else:
            print(f'Your balance is: {account_balance}')

    elif action == 'd':
        print('Deposit: ')
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_password = input('Please enter the password: ').strip()

        if user_deposit_amount < 0:
            print('You cannot deposit a negative amount!')
        elif user_password != account_password:
            print('Incorrect password')
        else:  # OK
            account_balance += user_deposit_amount
            print(f'Your new balance is: {account_balance}')
    elif action == 's':  # show
        print('Show: ')
        print(f"\tName: {account_name}")
        print(f"\tBalance: {account_balance}")
        print(f"\tPassword: {account_password}")
        print()
    elif action == 'w':
        print('Withdraw: ')

        user_withdraw_amount = int(input('Please enter the amount to withdraw: '))
        user_password = input('Please enter the password: ')

        if user_withdraw_amount < 0:
            print('You cannot withdraw a negative amount')
        elif user_password != account_password:
            print('Incorrect password for this account')
        elif user_withdraw_amount > account_balance:
            print('You cannot withdraw more than you have in your account')
        else:  # OK
            account_balance -= user_withdraw_amount
            print(f'Your new balance is: {account_balance}')
    elif action == 'q':
        break

print('Done')
