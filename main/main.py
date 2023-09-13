import json



def eraseDatabase(): #Borra todo el Data.txt
    with open("/workspaces/LMM-project/data.txt", "w") as file:
        file.write("{}")

def readDatabase(): #Devuelve el diccionario de Data.txt
    with open("/workspaces/LMM-project/data.txt", "r") as file:
        dataList = file.read()
        x = json.loads(dataList)
    #print(x)
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
        curDatabase.update({("user" + userName): newUserData})
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
        curDatabase.update({("vehicle" + placa): newUserData})
        #userDict = {"name" : userName, "password" : password}
        jsonDict = json.dumps(curDatabase)
        file.write(jsonDict)


#addToDatabase("admin", "1234", True)



# def adminInfoInput():
#     cat = input("Is admin? (y/n): ")

#     if cat == "y":
#         catBool = True
#         return catBool
#     elif cat == "n":
#         catBool = False
#         return catBool
#     else:
#         print("la opcion no existe\n")
#         return adminInfoInput()
    




def login():
    curDatabase = readDatabase()
    databaseKeys = list(curDatabase.keys())

    us = input("Enter Username: ")
    global logdUserName
    
    #print("username is: " + us)
    for i in range(len(curDatabase)):
        curUser = databaseKeys[i]
        #print(curUser)
        #print(curUser[:len(curUser)-1])
        #print("user in database: " + curDatabase[curUser]['name'])
        if curUser[0 : 4] == "user":
            
            logdUserName = us
            #print("reconocio palabra clave user")
            if curDatabase[curUser]['name'] == us:
                pas = input("Enter Password: ")

                if curDatabase[curUser]['password'] == pas:

                    if curDatabase[curUser]["isAdmin"]:
                        
                        loginSession(True)
                    else:
                        
                        loginSession(False)
    

def statVehicle(user):
    curDatabase = readDatabase()
    databaseKeys = list(curDatabase.keys())
    
    for i in range(len(curDatabase)):
        
        curVehicle = databaseKeys[i]
        
        if curVehicle[0 : 7] == "vehicle":
            
            if curDatabase[curVehicle]['reserved'] == False:
                
                curDatabase[curVehicle]['reserved'] = True
                curDatabase[curVehicle]['userDriving'] = user
                
                with open("/workspaces/LMM-project/data.txt", "w") as file:
                    databasejson = json.dumps(curDatabase)
                    file.write(databasejson)
                break

def loginSession(isAdmin : bool):
    
    if isAdmin:
        opcao = 0
        
        
        while opcao != "4":
            opcao = input("MODO ADMIN\n\nOperacoes>\n1: Administrar Veiculos\n2: Administrar Motoristas\n3: Administrar Usuarios\n4: Sair\n>: ")
            match opcao:
                case "1":
                    vehicleOption = input("ADMINISTRACAO DE VEICULOS\nOperacoes>\n1: Adicionar Veiculo\n2: Remover Veiculo\n3: Sair\n>:")
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
                            elif driving == "n":
                                driver = "none"
                                        
                                
                            res = input("Esta reservado? (s/n): ")
                            if res == "s":
                                addVehicleToDatabase(plate, driver, True)
                            else:
                                addVehicleToDatabase(plate, driver, False)
                                
                            
                        case "2":
                            curDatabase = readDatabase()
                            databaseKeys = list(curDatabase.keys())
                            vehicleQuant = 0
                            for i in range(len(curDatabase)):
                                    curVehicle = databaseKeys[i]
                                    if curVehicle[0 : 7] == "vehicle":
                                        vehicleQuant +=1
                                 
                            if vehicleQuant != 0:
                                invalid = True
                                while invalid:
                                    placa = input("Digite a placa do veiculo a remover: ")
                                    for i in range(len(curDatabase)):
                                        curVehicle = databaseKeys[i]
                                        
                                        
                                        if curVehicle[0 : 7] == "vehicle":
                                            
                                            if curDatabase[curVehicle]['plate'] == placa:
                                                curDatabase.pop(curVehicle)
                                                jsonDict = json.dumps(curDatabase)
                                                with open("/workspaces/LMM-project/data.txt", "w") as file:
                                                    file.write(jsonDict)
                                                invalid = False
                        case "3":
                            continue
                            
                            
                case "2":
                    
                    motorOption = input("ADMINISTRACAO DE MOTORISTAS\nOperacoes>\n1: Atualizar uso\n2: Sair\n>:")
                    match motorOption:
                        case "1":
                            
                            curDatabase = readDatabase()
                            databaseKeys = list(curDatabase.keys())
                            
                            
                            invalid = True
                            while invalid:
                                plate = input("Digite a placa: ")
                                
                                invalid2 = True
                                for i in range(len(curDatabase)):
                                    curVehicle = databaseKeys[i]
                                    
                                    if curVehicle[0 : 7] == "vehicle":
                                        
                                        while invalid2:
                                            driver = input("Digite o nome de usuario do motorista ('none' se nao tem): ")
                                            for j in range(len(curDatabase)):
                                                curUser = databaseKeys[j]
                                        
                                                if curUser[0 : 4] == "user":
                                            
                                                    if (curDatabase[curUser]['name'] == driver) or (driver == 'none'):
                                                        invalid2 = False

                                        if curDatabase[curVehicle]['plate'] == plate:
                                            curDatabase[curVehicle]['userDriving'] = driver
                                            if driver == 'none':
                                                curDatabase[curVehicle]['reserved'] = False
                                            else:
                                                curDatabase[curVehicle]['reserved'] = True
                                            jsonDict = json.dumps(curDatabase)
                                            with open("/workspaces/LMM-project/data.txt", "w") as file:
                                                file.write(jsonDict)
                                            invalid = False
                        case "2":
                            continue
                                            
                case "3":
                    
                    userOption = input("ADMINISTRACAO DE USUARIOS\nOperacoes>\n1: Adicionar usuario\n2: Eliminar usuario\n3:Sair\n>:")
                    
                    match userOption:
                        case "1": 
                            
                            curDatabase = readDatabase()
                            databaseKeys = list(curDatabase.keys())
                            
                            invalid = True
                            while invalid:
                                nomeUsuario = input("Digite o nome do usuario: ")
                                
                                for i in range(len(curDatabase)):
                                    curUser = databaseKeys[i]
                                    
                                    if curUser[0 : 4] == "user":
                                        
                                        if curDatabase[curUser]['name'] != nomeUsuario:
                                            invalid = False
                                            
                            senhaUsuario = input("Digite a senha do usuario: ")
                            
                            admin = input("O usuario é administrador?: s/n")
                            
                            if admin == "s":
                                addUserToDatabase(nomeUsuario, senhaUsuario, True)
                            else:
                                addUserToDatabase(nomeUsuario, senhaUsuario, False)
                        
                        case "2":
                            
                            curDatabase = readDatabase()
                            databaseKeys = list(curDatabase.keys())
                            
                            invalid = True
                            while invalid:
                                nome = input("Digite o nome do usuario a remover: ")
                                
                                for i in range(len(curDatabase)):
                                    curUsuario = databaseKeys[i]
                                    
                                    
                                    if curUsuario[0 : 4] == "user":
                                        
                                        if curDatabase[curUsuario]['name'] == nome:
                                            curDatabase.pop(curUsuario)
                                            jsonDict = json.dumps(curUsuario)
                                            with open("/workspaces/LMM-project/data.txt", "w") as file:
                                                file.write(jsonDict)
                                            invalid = False
                        case "3":
                            continue
        
    else:
        curDatabase = readDatabase()
        databaseKeys = list(curDatabase.keys())
        
        for i in range(len(curDatabase)):
            curVehicle = databaseKeys[i]
            
            if curVehicle[0 : 7] == "vehicle":
                
                if curDatabase[curVehicle]['userDriving'] == logdUserName:
                    opcao = input("Voce ja tem um veiculo reservado, deseja deixar usa-lo?(s/n)")
                    if opcao == "s":
                        curDatabase[curVehicle]['userDriving'] = "none"
                        curDatabase[curVehicle]['reserved'] = False
                        jsonDict = json.dumps(curDatabase)
                        with open("/workspaces/LMM-project/data.txt", "w") as file:
                            file.write(jsonDict)

                elif curDatabase[curVehicle]['userDriving'] == "none":
                    opcao = input("MODO USUARIO\n\nOperacoes>\n1: Reservar veículo.\n2: Sair\n\n")

                    match opcao:
                        case "1":
                            
                            statVehicle(logdUserName)


#us = input("Enter Username: ")
#pas = input("Enter Password: ")
#opBool = adminInfoInput()
running = True
while running:
    option = input("Fazer login? (s/n): ")
    if option == "s":
        login()
    else:
        option = input("Sair? (s/n): ")
        if option == "s":
            running = False
        else:
            running = True

#addToDatabase(us, pas, opBool)