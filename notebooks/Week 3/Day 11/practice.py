# class shape:
#     def area():
#         return 0

# class Rectangular(shape):
#     def area(self,width,height):
#         return height * width


# class Circle(shape):
#     def area(self,radius):
#         return 3.142 * radius **2

    

# for i in [shape.area(),Rectangular().area(4,7),Circle().area(5)]:
#     print(i)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Refused: {self.owner} has only Rs {self.balance}")
            return
        self.balance -= amount


class SavingsAccount(Account):        # SavingsAccount IS AN Account
    def add_interest(self, rate):
        self.balance += self.balance * rate
e = Account("arham",5000)
s = SavingsAccount("Ali", 10000)
s.deposit(2000)          # inherited from Account, no code repeated
s.add_interest(0.10)     # its own method
print(s.owner, "has Rs", s.balance)
print(e.balance)

