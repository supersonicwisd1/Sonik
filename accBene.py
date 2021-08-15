import accNumber

def accountNumberBeneficiary():
    print('Do you want to add to your beneficiary.\n1. Yes\n2. No')
    accountBeneficiaryDict = {
        '1' : 'yes',
        '2' : 'no'
    }
    accountBeneficiary = eval(input().strip().lower())
    if accountBeneficiary == 1:
        accountBeneficiaryList = []
        accountBeneficiaryList.append(accNumber.accountNumber)
        print('This number has been added to your beneficiary list')
    elif accountBeneficiary == 2:
        print('This number will not be add to your beneficiary list')
    else:
        print('Invalid input')
        return accountBeneficiary
    return accountNumberBeneficiary
