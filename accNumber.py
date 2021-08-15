#to get account number
import amount

import time
def accNum():
    print('Enter account number')
    global accountNumber
    accountNumber = input().strip()
    #to validation of account number
    while len(str(accountNumber)) != 10:
        print('Invalid Account Number')
        accNum()
    print('You are about to transfer a sum of N{amt} to Orjiene Kenechukwu Wisdom\nDo you want to continue\n1 Yes\n2 No'.format(amt = str(amount.amtNeeded)))
    accNumDict = {
        '1' : 'yes',
        '2' : 'no'
    }
    accChoice = eval(input().strip())
    if accChoice is 1:
        print('Your request is being processed...')
        time.sleep(3)
    if accChoice is 2:
        quit()