#for person to send airtime
def phoneNum():
    print('Enter beneficiary mobile number')
    global mobileNumber
    mobileNumber = input().strip()
    #to check for a valid mobile number
    if len(mobileNumber) != 11:
        print('Invalid Mobile Number')
        phoneNum()