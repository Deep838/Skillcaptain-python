class BankAccount:
    def __init__(self,acc_no,acc_name,bal):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.bal = int(bal)

    def deposit(self):
        dep = int(input("How much money you want to deposit: "))
        self.bal = dep + self.bal
        print(f"Your remaining balance is {self.bal}")

    def withdraw(self):
        withdraw = int(input("How much money you want to withdraw: "))
        self.bal = self.bal - withdraw
        print(f"Your remaining balance is {self.bal}")




my_acc =  BankAccount(123456789, "Deep Mondal" , 5000)

print(f"your account number is {my_acc.acc_no}")
print(f"Your account name is {my_acc.acc_name}")
print(f"Your remaining balance is {my_acc.bal}")

my_acc.deposit()


my_acc.withdraw()
