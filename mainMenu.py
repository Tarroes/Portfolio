OnMainMenu = True

def mainMenu():
    global OnMainMenu
    if mainMenuSelection == "1":
        addTransaction()
    elif mainMenuSelection == "2":
        print("Runs function: viewTransactions()")
    elif mainMenuSelection == "3":
        OnMainMenu = False
    else:
        print("Invalid selection. Please try again.")

def addTransaction():
    ValidTransDescription = False
    ValidTransAmount = False

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

    print("Transaction added successfully!")
    print("Description: " + transDescription)
    print("Amount: " + str(transAmount))
    

while OnMainMenu == True:
    print("Please select an option from the menu:")
    print("")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    mainMenuSelection = input("Enter your choice (1-3): ")
    mainMenu()