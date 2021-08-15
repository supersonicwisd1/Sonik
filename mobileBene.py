#to get into beneficiary list

import phoneNumber

def mobileNumberBeneficiary():
    print('Do you want to add to your beneficiary.\n1. Yes\n2. No')
    mobileBeneficiaryDict = {
        '1' : 'yes',
        '2' : 'no'
    }
    mobileBeneficiary = eval(input().strip().lower())
    if mobileBeneficiary == 1:
        mobileBeneficiaryList = []
        mobileBeneficiaryList.append(phoneNumber.mobileNumber)
        print('This number has been added to your beneficiary list')
    elif mobileBeneficiary == 2:
        print('This number will not be add to your beneficiary list')
    else:
        print('Invalid input')
        mobileNumberBeneficiary()

