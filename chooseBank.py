#to check for the bank to do transaction
from chooseBank2 import *

def firstPage():
    print('Choose Bank')
    pageOne = '''1 First bank
2 GT bank
3 Fidelity bank
4 Zenith bank
5 UBA
6 Next'''
    print(pageOne)
    bankChoice = int(input())
    if bankChoice == 6:
        secondPage()
