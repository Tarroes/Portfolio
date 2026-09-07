OnMainMenu = True

transactions = []

def mainMenu():
    global OnMainMenu
    if mainMenuSelection == "1":
        addTransaction()
    elif mainMenuSelection == "2":
        viewTransactions()
    elif mainMenuSelection == "3":
        OnMainMenu = False
    else:
        print("Invalid selection. Please try again.")

def addTransaction():
    ValidTransDescription = False
    ValidTransAmount = False
    ValidTransType = False

    while ValidTransDescription == False:
        transDescription = input("Please enter a short (20 characters or less) description of the transaction:")
        if len(transDescription) > 20:
            print("Description is too long. Please try again.")
        else:
            ValidTransDescription = True

    while ValidTransAmount == False:
        transAmount = input("Please enter the amount of the transaction:")
        try:
            transAmount = float(transAmount)
            ValidTransAmount = True
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    while ValidTransType == False:
        transType = input("Please enter the type of transaction (Income/Expense):")
        if transType.lower() == "income" or transType.lower() == "expense":
            ValidTransType = True
        else:
            print("Invalid Type. Please enter either 'Income' or 'Expense'.")
        

    transactions.append({
        "description": transDescription,
        "amount": transAmount,
        "type": transType.lower()
    })

def viewTransactions():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("Transactions:")
        for tx in transactions:
            print("Description: " + tx["description"] + ", Amount: " + str(tx["amount"]) + ", Type: " + str(tx["type"]))

while OnMainMenu == True:
    print("Please select an option from the menu:")
    print("")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    mainMenuSelection = input("Enter your choice (1-3): ")
    mainMenu()

