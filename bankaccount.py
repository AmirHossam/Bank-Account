#Account CLASS

#Account class includes features shared by all accounts
class Account: 
    #__INIT__ constructor method with attributes shared by all accounts
    def __init__(self,account_number,opening_deposit):
        self.account_number = account_number
        self.balance = opening_deposit

#Define a __str__ method to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance:.2f}'


#Define a universal method to accept deposits
    def deposit(self,dep_amount):
        self.balance += dep_amount

#Define a universal method to handle withdrawals
    def withdraw(self,wd_amount):
        if self.balance >= wd_amount:
            self.balance -= wd_amount
            return f" your balance :${self.balance:.2f}"
        else:
            return "Funds Unavailable"
            


#Check class inherits from Account and adds checking-specific traits

#inheriting from account class
class Checking(Account):
    def __init__(self,account_number,opening_deposit):
        super().__init__(account_number,opening_deposit)

#Define a __str__ method to return a string specific to checking accounts

    def __str__(self):
        return "Checking Account #{}\n Balance:{}".format((self.account_number),(Account.__str__(self)))


#Testing Checking Account object
"""
x= Checking(54225,654.22)
print(x)

print(x.withdraw(1000))
print(x.withdraw(600))
print(x.balance)
"""

#THIS SAVINGS CLASS INHERTING FROM ACCOUNT CLASS

class Savings(Account):
    def __init__(self,account_number,opening_deposit):

        super().__init__(account_number,opening_deposit)

    #Define a __str__ method to return a string specific to savings accounts

    def __str__(self):
        return "Saving Account #{}\n Balance : {}".format((self.account_number),(Account.__str__(self)))
        



#Business class that inheriting from account class 

class Business(Account):
    def __init__(self,account_number,opening_deposit):

        super().__init__(account_number,opening_deposit)

#Define a __str__ method to return a string specific to business accounts
    def __str__(self):
        return "Business Account #{}\n Balance:{}".format(self.account_number,Account.__str__(self))

        



class Customer:

    def __init__(self,name,PIN):
        self.name = name
        self.PIN = PIN

        #Create a dictionary of accounts to hold multiple accounts
        self.accts={'Check':[],'Save':[],'Business':[]}
    def __str__(self):
        return self.name

    def open_checking(self,account_number,opening_deposit):
        self.accts['Check'].append(Checking(account_number,opening_deposit))

    def open_savings(self,account_number,opening_deposit):
        self.accts['Save'].append(Savings(account_number,opening_deposit))

    def open_business(self,account_number,opening_deposit):
        self.accts['Business'].append(Business(account_number,opening_deposit))

        
        #method that computes the total needed deposit

    def get_total_deposits(self):
        total=0

        for acct in self.accts['Check']:
            print(acct)
            total += acct.balance

        for acct in self.accts['Save']:
            print(acct)
            total += acct.balance

        for acct in self.accts['Business']:
            print(acct)
            total += acct.balance

        print(f'Total deposits : ${total:.2f}')

#Testing
"""
bob = customer("BoB",1)
bob.open_checking(321,5555.5555)
bob.get_total_deposits()
bob.open_savings(321,1000)
bob.get_total_deposits()
"""
"""
#Testing Business
Amir = Customer("Amir",2)
Amir.open_business(551,100000)
Amir.get_total_deposits()
"""
def make_deposit(cust,acc_type,acc_num,dep_amount):
    '''
        make_dep(cust,acc_type,acc_num,dep_amount)
        cust   =  the customer ID
        acc_type = Check , Save , Business
        acc_num = integer
        dep_amount = integer
    '''

    for acct in cust.accts[acc_type]:
        if acct.account_number == acc_num:
            acct.deposit(dep_amount)
"""
#Testing Deposit:
make_deposit(Amir,"Business",551,1000000)
Amir.get_total_deposits()
"""

def make_withdraw(cust,acc_type,acc_num,wd_amount):
    '''
        make_withdraw(cust,acc_type,acc_num,wd_amount)
        cust   =  the customer ID
        acc_type = Check , Save , Business
        acc_num = integer
        wd_amount = integer
    '''
    for acct in cust.accts[acc_type]:
        if acct.account_number== acc_num:
            acct.withdraw(wd_amount)
"""
#Testing withdraw:
make_withdraw(Amir,"Business",551,1000000)
Amir.get_total_deposits()
"""