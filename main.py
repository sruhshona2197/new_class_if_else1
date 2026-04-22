#1 if/else
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        if self.balance == 0:
            return "Hisob bo'sh"
        else:
            return f"Balans: {self.balance}$"


account1 = BankAccount(0)
print(account1.check_balance())

account2 = BankAccount(1000)
print(account2.check_balance())


# 2
class Light:
    def __init__(self, state):
        self.state = state

    def status(self):
        if self.state:
            return "Chiroq yoniq"
        else:
            return "Chiroq o‘chiq"



lamp1 = Light(True)
print(lamp1.status())  

lamp2 = Light(False)
print(lamp2.status()) 
