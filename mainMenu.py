OnMainMenu = True

def mainMenu():
    global OnMainMenu
    if mainMenuSelection == "1":
        print("Runs function: addTransaction()")
    elif mainMenuSelection == "2":
        print("Runs function: viewTransactions()")
    elif mainMenuSelection == "3":
        OnMainMenu = False
    else:
        print("Invalid selection. Please try again.")

while OnMainMenu == True:
    print("Please select an option from the menu:")
    print("")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    mainMenuSelection = input("Enter your choice (1-3): ")
    mainMenu()