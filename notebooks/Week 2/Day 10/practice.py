# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        

#     def average(self):
#         avg = sum(self.marks)/len(self.marks)
#         return avg

#     def grade(self,avg):
#         if avg >= 80:
#             print("A+")
#         elif avg >=70:
#             print("B")
#         elif avg >=60:
#             print("C")
#         else:
#             print("Fail")


# o = student("Rehman",[40,90,85,95,79])
# o = student("ALi",[91,90,85,95,79])
# avg = o.average()
# print("Average marks of ",o.name, "is ",avg)
# print(o.grade(avg))


# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner        
#         self._bank = "HBL"          
#         self.__balance = balance    

#     def deposit(self, amount):
#         self.__balance += amount    

#     def balance(self):
#         return self.__balance       

# acc = Account("Ali", 5000)
# acc.deposit(2000)
# print(acc.owner)         # public - works
# print(acc._bank)         
# print(acc.balance())     # private, reached through a method - the right way



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Refused: {self.owner} tried to withdraw Rs {amount} but has Rs {self.balance}")
            return
        self.balance -= amount
    def transfer(self,other,amount):
        if amount <= self.balance:
            print(f"Not Enough Amount to transfer")

        other.deposit(amount)
        self.withdraw(amount)
          

ali = BankAccount("Ali", 1000)
zara = BankAccount("zara",500)
ali.transfer(zara,500)          # fine
print("Balance:", ali.balance)
print("Balance:", zara.balance)
