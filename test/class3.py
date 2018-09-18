from typing import List, Any


class Acount:
    name = "joe"
    def __init__(self, money):
        self.money = money

    def deposit(self, money):
        if money > 0:
            self.money += money
        else:
            print("wrong money")

    def withdraw(self, money):
        if money > 0:
            self.money -= money
        else:
            print("wrong money")

    def getmoney(self):
        return self.money

class Bank:
    user: List[Acount]

    def __init__(self):
        self.user = []

    def AddUser(self, money):
        self.user.append(Acount(money))

    def DelUser(self,number):
        self.user.pop(number)

    def TotalMoney(self):
        summ = 0
        for n in range(len(self.user)):
            summ += self.user[n].money
        return summ