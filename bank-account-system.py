class BankAccount:
    def __init__(self, account_number, account_holder, balance ):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance 

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            return self.balance
    

    def withdraw(self, amount):
        if self.balance < amount:
            return f"Insufficient funds"
        else: 
            self.balance -= amount
            return self.balance 
        
    def get_balance(self):
       return f"The balance in this account is {self.balance}" 
    
    def __str__(self):
        return f"{self.account_holder} account number {self.account_number} has amount {self.balance}"


acc = BankAccount("12345", "John Doe", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  # Output: 1300
print(acc)  # Output: Account 12345 - Holder: John Doe - Balance: $1300

    