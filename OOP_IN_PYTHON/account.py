import datetime
import pytz
# creat account class
class account:

    # now creating static method 
    # _current_time method
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # constructor
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance      # double underscore(_) before the balance indicates that user can't change the value of balance
        self.transaction_list= [(account._current_time(), balance)]
        print("Account created for "+ self.name)

    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
            print("{}  Deposited in " .format(amount) +self.name+"'s "+ "account ")
            self.show_balance()
            self.transaction_list.append((account._current_time(), amount))

    # withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            print("{} is withdrawn from {} " .format(amount, self.__balance))
            self.__balance -= amount
            self.transaction_list.append((account._current_time(), amount))
        else:
            print("TO withdraw {}, you must have this much in your account" .format(amount))
        self.show_balance()

    # show_balance method
    def show_balance(self):
        print(" Your balance is: {}" .format(self.__balance))

    # show_transcation method
    def show_transcation(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposted"
            else:
                tran_type = "withdrawn"
            print("{} {} on {} (local time was {})" .format(amount, tran_type, date, date.astimezone()))



# class ended
# to check if file is running from main or not
if __name__ == "__main__":
    zen = account("zen",0)
    zen.deposit(500)
    # zen.__balance= 450   this line won't work eve if the line was uncommented due to double underscore(_) 
    zen.withdraw(150)
    zen.withdraw(100)
    zen.withdraw(150)
    print("><"*50)
    zen.show_transcation()
    zen.show_balance()
    print(zen.__dict__)
#  now for user to change the balanace, they must see the name using __dict__ or just by using '_<class-name>__<variable-name>'
    zen._account__balance = 000
    zen.show_balance()
