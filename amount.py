#to get amount for transaction

def amt():
    print('Enter amount 50000 - 2000000')
    global amtNeeded
    try:
        amtNeeded = int(input().strip())
    except:
        print("Enter numerical values")
        amt()
    while amtNeeded > 2000000:
        print("You don't have sufficient funds.")
        amt()