import json

def eraseDatabase():
    with open("/workspaces/LMM-project/data.txt", "w") as file:
        file.write("{}")

def addToDatabase(userName, password, admin): 
    curDatabase = readDatabase()
    
    userQuant = len(curDatabase)

    with open("/workspaces/LMM-project/data.txt", "w") as file:
        newUserData = {"name" : userName, "password" : password, "isAdmin" : admin}
        curDatabase.update({("user" + str(userQuant+1)): newUserData})
        #userDict = {"name" : userName, "password" : password}
        jsonDict = json.dumps(curDatabase)
        file.write(jsonDict)


def adminInfoInput():
    cat = input("Is admin? (y/n): ")

    if cat == "y":
        catBool = True
        return catBool
    elif cat == "n":
        catBool = False
        return catBool
    else:
        print("la opcion no existe\n")
        adminInfoInput()
    

def readDatabase():
    with open("/workspaces/LMM-project/data.txt", "r") as file:
        dataList = file.read()
        x = json.loads(dataList)
    print(x)
    return x




us = input("Enter Username: ")
pas = input("Enter Password: ")
opBool = adminInfoInput()


    

addToDatabase(us, pas, opBool)
