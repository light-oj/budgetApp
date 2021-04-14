class Budget:

    # Initialize account balance as 0
    balance = [0, 0, 0]

    def __init__(self, category):
        self.category = category

    def deposit(self, value):
        data = int(input("Enter Deposit Amount: "))
        Budget.balance[value] += data
        return "You deposit {} into {}".format(Budget.balance[value], self.category)

    def withdraw(self, value):
        data = int(input("Enter Withdrawal Amount: "))
        Budget.balance[value] -= data
        return "You withdraw {} from {}".format(Budget.balance[value], self.category)

    def transfer(self, value1, value2):
        data = int(input("Enter Transfer Amount: "))
        if data > Budget.balance[value1]:
            print("Insufficient Fund")
        else:
            Budget.balance[value1] -= data
            Budget.balance[value2] += data
            print("Done \n")
        return "You transfer {} from {}".format(Budget.balance[value1], self.category)

    def checkBalance(self, value):
        return "# {}.".format(Budget.balance[value])


# budget_one = Budget("Food").deposit(0)
# print(budget_one)
# Budget("Data").transfer(0, 2)
# print(Budget("Data").checkBalance(2))


def main():
    print("Welcome     ")

    selectedOption = int(input(
        "What would you like to do? \n ** 1. Deposit \n ** 2. Withdrawal \n ** 3. Check balance \n ** 4. Transfer \n "
        "** 5. Exit\n"))

    if selectedOption == 1:
        category = ["Food", "HealthCare", "Data"]
        response = int(input("Which category are you depositing to?\n"
                             " 1. Food \n 2. HealthCare \n 3. Data\n"))
        if response == 1:
            withdraw = Budget(category[response - 1]).deposit(response - 1)
            print("Done \n")
            main()

        elif response == 2:
            withdraw = Budget(category[response - 1]).deposit(response - 1)
            print("Done \n")
            main()

        elif response == 3:
            withdraw = Budget(category[response - 1]).deposit(response - 1)
            print("Done \n")
            main()

        else:
            print("Invalid option")
            main()

    elif selectedOption == 2:
        category = ["Food", "HealthCare", "Data"]
        response = int(input("Which category are you withdrawing from?\n"
                             " 1. Food \n 2. HealthCare \n 3. Data\n"))
        if response == 1:
            withdraw = Budget(category[response-1]).withdraw(response-1)
            print("Done \n")
            main()

        elif response == 2:
            withdraw = Budget(category[response-1]).withdraw(response-1)
            print("Done \n")
            main()

        elif response == 3:
            withdraw = Budget(category[response-1]).withdraw(response-1)
            print("Done \n")
            main()

        else:
            print("Invalid option")
            main()

    elif selectedOption == 3:
        category = ["Food", "HealthCare", "Data"]
        response = int(input("Select option:\n 1. Food \n 2. HealthCare \n 3. Data \n 4. Total Balance\n"))

        if response == 1:
            balance = Budget(category[response-1]).checkBalance(response-1)
            print("Your balance is: ")
            print(" === === ==== ==== === ===\n")
            print(" Food: " + str(balance))
            print("\n === === ==== ==== === ===")
            main()

        elif response == 2:
            balance = Budget(category[response-1]).checkBalance(response-1)
            print("Your balance is: ")
            print(" === === ==== ==== === ===\n")
            print(" HealthCare: " + str(balance))
            print("\n === === ==== ==== === ===")
            main()

        elif response == 3:
            balance = Budget(category[response - 1]).checkBalance(response - 1)
            print("   Your balance is: ")
            print(" === === ==== ==== === ===")
            print("   Data: " + str(balance))
            print(" === === ==== ==== === ===")
            main()

        elif response == 4:
            print("Your balance is as follows: ")
            print(" === === ==== ==== === ===")
            print(" Food: " + str(Budget.balance[0]))
            print(" HealthCare: " + str(Budget.balance[1]))
            print(" Data: " + str(Budget.balance[2]))
            print(" === === ==== ==== === ===")
            main()

        else:
            print("Invalid option")
            main()

    elif selectedOption == 4:
        category = ["Food", "HealthCare", "Data"]
        value1 = int(input("Transfer from: * 1. Food * 2. HealthCare * 3. Data\n"))
        value2 = int(input("Transfer to: * 1. Food * 2. HealthCare * 3. Data\n"))
        if value1 == value2:
            print("You cannot transfer within the same category")
            main()
        else:
            transfer = Budget(category[value1 - 1]).transfer(value1-1, value2-1)
            main()
    elif selectedOption == 5:
        print("Thank you... \nGoodbye!!!!")
        exit()

    else:
        print("Invalid option selected")
        main()


main()
