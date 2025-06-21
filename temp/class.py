class Account:
    interest = 0.02
    def __init__(self,account_holder):
        self.balance=0
        self.holder=account_holder

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance=self.balance-amount
        return self.balance    
class CheckingAccount(Account):
    interest=0.01    
    withdraw_fee=1

    def withdraw(self,amount):
        return Account.withdraw(self,amount+self.withdraw_fee)
    
class Bank:
    """ A bank **has** account
    >>> bank=Bank()
    >>> john=bank.open_account('john',10)
    >>> jack=bank.open_account('jack',5,CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts=[]

    def open_account(self,holder,amount,kind=Account):
        account=kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1


    




class Ratio:
    def __init__(self,n,d):
        self.numer=n
        self.denom=d
    def __repr__(self):
        return 'Ratio({0},{1})'.format(self.numer,self.denom)
    def __str__(self):
        return '{0}/{1}'.format(self.numer,self.denom)
    def __add__(self,other):
        if isinstance(other,int):
            n=self.numer+self.denom*other
            d=self.denom
        elif isinstance(other,Ratio):
            n=self.numer * other.denom+self.denom * other.numer
            d=self.denom * other.denom
        elif isinstance(other,float):
            return float(self) + other
        g=gcd(n,d)
        return Ratio(n//g,d//g)
    
    __radd__=__add__
    
    def __float__(self):
        return self.numer/self.denom
    
def gcd(n,d):
    while n!=d:
        n,d=min(n,d),abs(n-d)
    return n


class myclass:
    def __init__(self,person_name,person_age):
        self.__name=person_name
        self.age=person_age