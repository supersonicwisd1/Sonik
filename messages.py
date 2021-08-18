#messages from supersonik bank

import amount
from balance import *

import time
import datetime
def accountDebitMessage():
    time.sleep(10)
    print('######################################################################\n')
    Message = input('\nMessage!!! from Supersonik, press enter to open')
    print('\nSupersonik bank')
    print('Debit Message\n')
    print('You sent the sum of', 'N'+str(amount.amtNeeded),'to Orjiene Kenechukwu Wisdom.\nYou have been debited by N'+ str(amount.amtNeeded) +' on', time.asctime())
    print('Your new Account balance is', balanceAmount)
    return accountDebitMessage
def mobileNumberDebitMessage():
    time.sleep(10)
    print('######################################################################\n')
    Message = input('\nMessage!!! from Supersonik, press enter to open')
    print('\nSupersonik bank')
    print('Debit Message\n')
    print('You just recharge your mobile phone with the sum of', 'N'+str(amount.amtNeeded),'.\nYou have been debited by', str(amount.amtNeeded),'on', time.asctime())
    print('Your new Account balance is', balanceAmount)
    return mobileNumberDebitMessage
def othersDebitMessage():
    time.sleep(10)
    print('######################################################################\n')
    Message = input('\nMessage!!! from Supersonik, press enter to open')
    print('\nSupersonik bank')
    print('Debit Message\n')
    print('You just recharged Orjiene Kenechukwu Wisdom with the sum of', 'N'+str(amount.amtNeeded),'.\nYou have been debited by', str(amount.amtNeeded),'on', time.asctime())
    print('Your new Account balance is', balanceAmount)
    return othersDebitMessage
def balanceMessage():
    print('######################################################################\n')
    Message = input('\nMessage!!! from Supersonik, press enter to open')
    print('Your balance is', balanceAmount)
    return balanceMessage
