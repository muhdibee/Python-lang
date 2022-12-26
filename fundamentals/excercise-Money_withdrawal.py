# Functions, parameters and arguments
# A function for withdrawing money.
def withdraw_money(current_balance, amount):
    balance = current_balance - amount
    if balance > 10:  # balance can not be less than 10.
        current_balance = balance
        return balance
    else:
        return False


def do_withdraw(bal, amt):
    balance = withdraw_money(bal, amt)
    if (balance):
        print('Success, Balance: ', balance)
    else:
        print('Failed, Insufficient fund.')


do_withdraw(100, 65)
do_withdraw(100, 99)
