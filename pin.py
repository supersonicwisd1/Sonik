#to get PIN code
def bankCode():
    print('Enter your PIN code')
    code = input().strip()
    if code == "":
        bankCode()
    elif len(code) != 4:
        print("Pin has a maximum number of four digits")
        bankCode()
    else:
        pass