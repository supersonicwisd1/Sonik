import chooseBank

def secondPage():
    print("Choose Bank")
    pageTwo = '''1 FCMB bank
2 Union bank
3 Wema bank
4 Access bank
5 Unity bank
6 Previous'''
    print(pageTwo)
    bankChoice = int(input())
    if bankChoice == 6:
        chooseBank.firstPage()


