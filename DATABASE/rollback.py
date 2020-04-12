import sqlite3

db = sqlite3.connect("DATABASE/accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, account))")


class Account(object):

    def __init__(self, name: str, bal: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self.bal = row
            print("Retrived record for {} " .format(self.name), end='')
        else:
            self.name = name
            self.bal = bal 
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, bal))
            cursor.connection.commit()
            print("Account created for {} " .format(self.name),end='')
        self.show_bal()

    def deposit(self, amount: int):
        if amount > 0.0:
            self.bal += amount
            # ':.2f' means up to 2 decimal places 
            print("{:.2f} deposited" .format(amount/100))  
        return self.bal / 100

    def withdraw(self, amount: int):
        if 0 < amount <= self.bal:
            self.bal -= amount
            print("{:.2f} withdrawn" .format(amount / 100))
            return amount /100
        else:
            print("Amount must be between 0 and your present balance")
            return 0.0

    def show_bal(self):
        print("Balance on account {} is {:.2f} " .format(self.name, self.bal / 100))

if __name__ == '__main__':
    zen = Account('zen')
    zen.deposit(1010)
    zen.deposit(10)
    zen.deposit(10)
    zen.withdraw(30)
    zen.withdraw(0)
    zen.show_bal()

    yukino = Account("Yukino",10000)
    hikki = Account("Hikigaya",100)
    eureka = Account("Eureka")

    db.close()
    