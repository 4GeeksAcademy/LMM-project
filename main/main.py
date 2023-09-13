
def updateDatabase(userName, password):

    with open("/workspaces/LMM-project/data.txt", "a") as file:
        #appendedStr = str("user(", userName, ",", password, ")\n")
        file.write("user("+ userName + "," + password + ")\n")

dataDict = {}

us = input("Enter Username: ")
pas = input("Enter Password: ")

updateDatabase(us, pas)