# Import the BankAccount class from the BankAccount.py module file
from BankAccount import BankAccount


# Create a BankAccount instance called my_acc using its parameterised constructor.
# This will create a BankAccount object in memory with a fName of "Michelle" and 
# an lName of "Graham". As I haven't supplied the optional balance value,
# the object's balance will be set to 0
my_acc = BankAccount("Michelle", "Graham")
# As the balance variable is intended to be private (because its name starts with _),
# we shouldn't use my_acc._balance. Instead, we use a method to get that value
print("Michelle's current balance is €", my_acc.get_balance())
print(isinstance(my_acc, BankAccount))
