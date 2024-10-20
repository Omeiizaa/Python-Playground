#Bank_Details

Bank_database = dict()
def Add_User():
    while True:
        username = input('Enter your username: ')
        account_name = input('Enter Account Name: ')
        account_number = int(input('Enter Account Number: '))
        balance = float(input('Enter Account Balance Amount: '))
        pin = int(input('Input security pin: '))

        user = dict()
        user['account_name'] = account_name
        user['account_number'] = account_number
        user['balance'] = balance
        user['pin'] = pin

        Bank_database[f'{username}'] =user
        print(Bank_database.items())

        res = input('Are you a new user: (y) Yes, (n) No' )
        if res.lower() == 'y':
            continue
        else:
            break
def View_Database():
    for key, value in Bank_database.items():
        print('Username:', key)
        for x, y in value.items():
            print({x: y})

def withdraw(username):
    user = Bank_database[username]
    balance = user['balance']
    userpin = int(input('Enter your pin'))
    if userpin == user['pin']:
        withdrawal = float(input('Enter  amount to withdraw'))
        if withdrawal > user['balance']:
            print("Insufficient funds!!")
        else:
            user['balance'] = balance - withdrawal
            print(user['account_name'], user['balance'])
            print(user)
    else:
        print("Pin Incorrect!!")
    

def deposit(username):
    user = Bank_database[username]
    balance = user['balance']
    userpin = int(input('Enter your pin'))
    if userpin == user['pin']:
        depositing = float(input('Enter Amount to Deposit'))
        user['balance'] = balance + depositing
        print(user['account_name'], user['balance'])
        print(user)
    else:
        print('Incorrect Pin')
        
   

