import json



def eraseDatabase():
    with open("/workspaces/LMM-project/data.txt", "w") as file:
        file.write("{}")

def readDatabase():
    with open("/workspaces/LMM-project/data.txt", "r") as file:
        dataList = file.read()
        x = json.loads(dataList)
    print(x)
    return x

def addToDatabase(userName, password, admin): 
    curDatabase = readDatabase()
    
    userQuant = len(curDatabase)

    with open("/workspaces/LMM-project/data.txt", "w") as file:
        newUserData = {"name" : userName, "password" : password, "isAdmin" : admin}
        curDatabase.update({("user" + str(userQuant+1)): newUserData})
        #userDict = {"name" : userName, "password" : password}
        jsonDict = json.dumps(curDatabase)
        file.write(jsonDict)



#addToDatabase("admin", "1234", True)



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
        return adminInfoInput()
    




def login():
    curDatabase = readDatabase()
    databaseKeys = list(curDatabase.keys())

    us = input("Enter Username: ")
    print("username is: " + us)
    for i in range(len(curDatabase)):
        curUser = databaseKeys[i]
        print(curUser)
        print(curUser[:len(curUser)-1])
        print("user in database: " + curDatabase[curUser]['name'])
        if curUser[:len(curUser)] == "user":
            if curDatabase[curUser]['name'] == us:
                pas = input("Enter Password: ")

                if curDatabase[curUser]['password'] == pas:

                    if curDatabase[curUser]["isAdmin"]:
                        loginSession(True)

def loginSession(isAdmin : bool):
    if isAdmin:
        opcao = input("MODO ADMIN\n\nOperacoes>\n1: Administrar Veiculos\n2: Administrar Motoristas\n3: Administrar Usuarios\n>: ")
        
        match opcao:
            case "1":
                print("op1 seleccionada")


#us = input("Enter Username: ")
#pas = input("Enter Password: ")
#opBool = adminInfoInput()

login()
    

#addToDatabase(us, pas, opBool)
