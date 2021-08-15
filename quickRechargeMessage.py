import time
from randomBalance import *
import main


def quickMessage(amount):
    time.sleep(10)
    print('######################################################################\n')
    input('\nMessage!!! from Supersonik, press enter to open')
    print('\nSUpersonik bank')
    print('Debit Message\n')
    print('You just recharge your mobile phone with the sum of', 'N' + str(amount), '.\nYou have been debited by',
          str(amount), 'on', time.asctime())
    print('Your new Account balance is', balanceAmount)
