from test.class3 import Bank
from test.class3 import Acount

bank1 = Bank()
bank1.AddUser(1500)
bank1.AddUser(2000)
bank1.AddUser(500)
acount1 = bank1.user[0]
# print(bank1.user)

print("-------------------------------")

print(bank1.TotalMoney())
