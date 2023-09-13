import json



def eraseDatabase(): #Borra todo el Data.txt
    with open("/workspaces/LMM-project/data.txt", "w") as file:
        file.write("{}")

def readDatabase(): #Devuelve el diccionario de Data.txt
    with open("/workspaces/LMM-project/data.txt", "r") as file:
        dataList = file.read()
        x = json.loads(dataList)
    print(x)
    return x

def addUserToDatabase(userName, password, admin): #Añade nuevo usuario al data (Puede repetir)
    curDatabase = readDatabase()
    databaseKeys = list(curDatabase.keys())
    userQuant = 0
    for i in range(len(databaseKeys)):
        if databaseKeys[i][:len(databaseKeys[i])-1] == "user":
            userQuant += 1
    
    with open("/workspaces/LMM-project/data.txt", "w") as file:
        newUserData = {"name" : userName, "password" : password, "isAdmin" : admin}
        curDatabase.update({("user" + str(userQuant+1)): newUserData})
        #userDict = {"name" : userName, "password" : password}
        jsonDict = json.dumps(curDatabase)
        file.write(jsonDict)

def addVehicleToDatabase(placa, usadoPor, reservado): #Añade nuevo vehiculo
    curDatabase = readDatabase()
    databaseKeys = list(curDatabase.keys())
    vehicleQuant = 0
    for i in range(len(databaseKeys)):
        if databaseKeys[i][:len(databaseKeys[i])-1] == "vehicle":
            vehicleQuant += 1

    with open("/workspaces/LMM-project/data.txt", "w") as file:
        newUserData = {"plate" : placa, "userDriving" : usadoPor, "reserved" : reservado}
        curDatabase.update({("vehicle" + str(vehicleQuant+1)): newUserData})
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
        #print(curUser)
        #print(curUser[:len(curUser)-1])
        #print("user in database: " + curDatabase[curUser]['name'])
        if curUser[:len(curUser)-1] == "user":
            print("reconocio palabra clave user")
            if curDatabase[curUser]['name'] == us:
                pas = input("Enter Password: ")

                if curDatabase[curUser]['password'] == pas:

                    if curDatabase[curUser]["isAdmin"]:
                        loginSession(True)
                    else:
                        loginSession(False)

def loginSession(isAdmin : bool):
    
    if isAdmin:
        opcao = input("MODO ADMIN\n\nOperacoes>\n1: Administrar Veiculos\n2: Administrar Motoristas\n3: Administrar Usuarios\n>: ")
        
        match opcao:
            case "1":
                vehicleOption = input("ADMINISTRACAO DE VEICULOS\nOperacoes>\n1: Adicionar Veiculo\n2: Remover Veiculo")
                match vehicleOption:
                    
                    case "1":
                        curDatabase = readDatabase()
                        databaseKeys = list(curDatabase.keys())
                        
                        plate = input("Digite a placa: ")
                        driving = input("Esta sendo utilizado? (s/n): ")
                        if driving == "s":
                            
                            invalid = True
                            while invalid:
                                driver = input("Digite o nome de usuario que esta utilizando: ")
                                
                                for i in range(len(curDatabase)):
                                    curUser = databaseKeys[i]
                                    
                                    if curUser[0 : 4] == "user":
                                        
                                        if curDatabase[curUser]['name'] == driver:
                                            invalid = False
                                    
                            
                        res = input("Esta reservado? (s/n): ")
                        if res == "s":
                            addVehicleToDatabase(plate, driver, True)
                        else:
                            addVehicleToDatabase(plate, driver, False)
                            
                        
                        case "2":
                        
                        
            case "2":
                motorOption = input("ADMINISTRACAO DE MOTORISTAS\nOperacoes>\n1: Atualizar uso")
                match motorOption:
                    case "1":
                        
                        curDatabase = readDatabase()
                        databaseKeys = list(curDatabase.keys())
                        
                        plate = input("Digite a placa: ")
                        invalid = True
                        while invalid:
                            driver = input("Digite o nome de usuario do dono: ")
                            
                            for i in range(len(curDatabase)):
                                curUser = databaseKeys[i]
                                
                                if curUser[:len(curUser)-1] == "user":
                                    
                                    if curDatabase[curUser]['name'] == driver:
                                        invalid = False
                        


#us = input("Enter Username: ")
#pas = input("Enter Password: ")
#opBool = adminInfoInput()

login()
    

#addToDatabase(us, pas, opBool)
