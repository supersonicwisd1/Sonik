
import airtimeother
import airtimeself
import history
import otherBank
import quickRechargeMessage
import sameBank
from randomBalance import *
import time

operation_dict = ('''1 Airtime Self
2 Airtime Others
3 Tranfer to Supersonik
4 Tranfer to Other bank
5 Check Balance''')

# quickRechargeMessage
def quickMessage(amount):
    time.sleep(10)
    print('######################################################################\n')
    input('\nMessage!!! from Supersonik, press enter to open')
    print('\nSUpersonik bank')
    print('Debit Message\n')
    print('You just recharge your mobile phone with the sum of', 'N' + str(amount), '.\nYou have been debited by',
          str(amount), 'on', time.asctime())
    print('Your new Account balance is', balanceAmount)
    quit()

#the heart of all
def bankOperation():
    accessList = ['*429#']
    print('To get access to Supersonik bank mobile banking, dial *429#\n')
    global ass
    ass = str(input())

# quickRecharge
    if "*429*1*" in ass:
        amt1 = ass[7:]
        amt = amt1[:-1]
        quickMessage(amt)
    else:
        print("Error")

    if ass == '*429#':
        print('Welcome to Supersonik mobile banking code')
        print(operation_dict)

        choice = eval(input())
        if choice is 1:
            airtimeself.airself()
        elif choice is 2:
            airtimeother.airothers()
        elif choice is 3:
            sameBank.transferSupersonik()
        elif choice is 4:
            otherBank.transferOther()
        elif choice is 5:
            history.checkBalance()
        else:
            print('Invalid input')
    else:

        print('Unsupport code')
        print(bankOperation())


bankOperation()