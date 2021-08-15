#to get random balance
from randomBalance import *
import messages

def randomBalance():
    print('This will cost N20 as charges. Do you want to continue')
    balanceDict = '''1 Yes
2 No'''
    print(balanceDict)
    balance = eval(input().strip())
    if balance is 1:
        print('You will receive message shortly\n')
        import time
        time.sleep(5)
        messages.balanceMessage()
    if balance == 2:
        quit()
    if balance == '':
        print('Invalid input')
