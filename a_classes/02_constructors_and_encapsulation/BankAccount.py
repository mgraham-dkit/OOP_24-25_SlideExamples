# Define a class called BankAccount (this should be in a file called BankAccount.py)
class BankAccount:
    # Create a constructor that requires two parameters, with a third optional parameter
    # Where only two values are provided, the value for _balance defaults to 0
    # Where three values are provided, the value supplied in the _balance
    # position is used for _balance
    def __init__(self, fName, lName, _balance=0):
        # Store the supplied value for fName in the fName attribute
        self.fName = fName
        # Store the supplied value for lName in the lName attribute
        self.lName = lName
        # Store the supplied (or default) value for _balance in the _balance attribute
        self._balance = _balance
    
    # Define a display method to print out the information of the current bank account
    # self is specified as a parameter so this method knows whose version of the attributes to use
    def display(self):
        print(f"BankAccount[first name: {self.fName}, last name: {self.lName}, balance: {self._balance}]")
        
    # Getter method to retrieve the current value of _balance
    # This is provided because _balance is intended as a private variable,
    # i.e. only this class should access it directly (using self._balance)
    def get_balance(self):
        return self._balance
    
    # Setter method to change the value of the _balance attribute
    # This is needed because _balance is a private variable
    def set_balance(self, new_bal):
        # If the new balance value is below 0, do not change the _balance value
        if new_bal > 0:
            self._balance = new_bal
        else:
            print("No overdraft enabled")
            
            