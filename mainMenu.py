from datetime import datetime

OnMainMenu = True

transactions = []

def mainMenu():
    global OnMainMenu
    if mainMenuSelection == "1":
        addTransaction()
    elif mainMenuSelection == "2":
        viewTransactions()
    elif mainMenuSelection == "3":
        viewSummary()
    elif mainMenuSelection == "4":
        OnMainMenu = False
    else:
        print("Invalid selection. Please try again.")

def addTransaction():
    validTransDescription = False
    validTransAmount = False
    validTransType = False
    validTransDate = False
    validTransCategory = False

    TransCategories = ["food", "transport", "housing", "entertainment", "salary", "other"]

    while validTransDate == False:
        dateInput = input("Please enter the date of the transaction (YYYY-MM-DD):")
        try:
            transDate = datetime.strptime(dateInput, "%Y-%m-%d").date()
            validTransDate = True
        except ValueError:
            print("Invalid date format. Please try again.")

    while validTransCategory == False:
        transCategory = input("Please enter the category of the transaction (food, transport, housing, entertainment, salary, other):")
        if transCategory.lower() in TransCategories:
            validTransCategory = True
        else:
            print("Invalid category. Please try again.")

    while validTransDescription == False:
        transDescription = input("Please enter a short (20 characters or less) description of the transaction:")
        if len(transDescription) > 20:
            print("Description is too long. Please try again.")
        else:
            validTransDescription = True

    while validTransAmount == False:
        transAmount = input("Please enter the amount of the transaction:")
        try:
            transAmount = float(transAmount)
            validTransAmount = True
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    while validTransType == False:
        transType = input("Please enter the type of transaction (Income/Expense):")
        if transType.lower() == "income" or transType.lower() == "expense":
            validTransType = True
        else:
            print("Invalid Type. Please enter either 'Income' or 'Expense'.")
        

    transactions.append({
        "description": transDescription,
        "amount": transAmount,
        "type": transType.lower(),
        "date": transDate,
        "category": transCategory.lower()
    })

def viewSummary():
    totalIncome = 0
    totalExpense = 0
    for tx in transactions:
        if tx["type"] == "income":
            totalIncome += tx["amount"]
        elif tx["type"] == "expense":
            totalExpense += tx["amount"]
    print("Summary:")
    print("Total Income: ${:.2f}".format(totalIncome))
    print("Total Expense: ${:.2f}".format(totalExpense))
    print("Net Balance: ${:.2f}".format(totalIncome - totalExpense))

def viewTransactions():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("Transactions:")
        for tx in transactions:
            print("Date: {}, Description: {}, Amount: {}, Type: {}, Category: {}".format(tx["date"], tx["description"], tx["amount"], tx["type"], tx["category"]))

while OnMainMenu == True:
    print("Please select an option from the menu:")
    print("")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Exit")
    mainMenuSelection = input("Enter your choice (1-4): ")
    mainMenu()