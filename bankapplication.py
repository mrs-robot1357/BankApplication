from helpers import verify_type_or_raise_error
import random


user_name = input("Please enter your name: ")
print(f"Welcome {user_name.capitalize()}. We have multiple banks for you to create an account with.")


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []


user_object = User(user_name)


class Bank:
    def __init__(self, name, pid):
        self.name = name
        self.pid = verify_type_or_raise_error(pid, int)
        self.hq_address = ""
        self.accounts = []
        self.user_count = 0


class Kuda(Bank):
    def __init__(self, name, pid):
        super().__init__(name, pid)
        self.hq_address = "Abuja"
        self.pid = 275
        # print("Thank you for banking with Kuda")


class Zenith(Bank):
    def __init__(self, name, pid):
        super().__init__(name, pid)
        self.hq_address = "Lagos"
        self.pid = 220
        # print("Zenith is the best, you made a good call")


class Access(Bank):
    def __init__(self, name, pid):
        super().__init__(name, pid)
        self.hq_address = "Enugu"
        self.pid = 396
        # print("Banking with Access is secure and happy banking.")


k = Kuda("kuda", 275)
z = Zenith("Zenith", 220)
a = Access("Access", 396)

bank_inventory = {
    "Kuda": k,
    "Zenith": z,
    "Access": a
}

kuda_account_object = Bank("Kuda", 275)
zenith_account_object = Bank("Zenith", 220)
access_account_object = Bank("Access", 396)


class Account:
    def __init__(self, account_holder, bank):
        self.account_holder = verify_type_or_raise_error(account_holder, User)
        self.bank = verify_type_or_raise_error(bank, Bank)
        self.account_number = str(self.bank.pid) + str(random.randint(1, 899999 + 100000))
        self.account_balance = 1000
        print(f"{user_name.capitalize()}'s {bankKey} account")
        print(f"Your account number is {self.account_number} and bank id is {self.bank.pid}")

    def __repr__(self):
        return f"{user_name}'s {self.bank.name} account"

    def deposit(self, amount):
        if amount >= 500 and (amount <= 1000):
            print(f"Your account has been credited with {amount}")
            self.account_balance += amount
            print(f"Your new account balance is {self.account_balance}")
        else:
            print("You need to deposit a minimum of N500 and a maximum of N1000")

    def withdraw(self, amount):
        self.account_balance -= amount
        if amount > self.account_balance:
            print("You have an insufficient balance. Please try again.")
        else:
            print(f"Your account has been debited with {amount}")
            print(f"Your new account balance is {self.account_balance}")

    def transfer(self, amount):
        transfer_question = int(input("Do you wish to transfer to your other account? Press 1 for yes and 2 for no"))
        if transfer_question == 1:
            user_amount = int(input("How much would you like to transfer"))
            self.account_balance -= user_amount
            if user_amount > self.account_balance:
                print("You have an insufficient balance. Please try again.")
            else:
                print(f"Your account has been debited with {user_amount}")
                print(f"Your new account balance is {self.account_balance}")
        elif transfer_question == 2:
            print("You do not wish to transfer")


while True:
    create_account = int(input("Type 1 for KudaBank, 2 for ZenithBank, 3 for AccessBank and 0 to quit the applicaton"))

    if create_account == 1:
        print(f"Hi {user_name.capitalize()}! Thank you for choosing with Kuda.")

    elif create_account == 2:
        print(f"Hi {user_name.capitalize()}! Thank you for choosing with Zenith.")

    elif create_account == 3:
        print(f"Hi {user_name.capitalize()}! Thank you for banking with Access.")

    if create_account > 3:
        print("You have entered an invalid option.")

    bankKey, bankValue = list(bank_inventory.items())[(create_account - 1)]


    def bank_list():
        return bank_inventory.keys()


    if create_account == 1:
        user_account = Account(user_object, kuda_account_object)
        user_object.accounts.append(user_account)

    elif create_account == 2:
        user_account = Account(user_object, zenith_account_object)
        user_object.accounts.append(user_account)

    elif create_account == 3:
        user_account = Account(user_object, access_account_object)
        user_object.accounts.append(user_account)

    elif create_account == 0:
        break

    # user_account.withdraw(350)
    total_number_of_accounts = len(user_object.accounts)
    if total_number_of_accounts > 2:
        user_deposit = int(input("How much would you like to deposit?Min of 500 and max of 1000: "))
        user_account.deposit(user_deposit)
        if bankKey == bankKey:
            user_account.transfer(user_deposit)

    print("Your existing accounts are: ", user_object.accounts)
















