import json

def abrirJSON():
    dicFinal={}
    with open('./clientes.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./clientes.json",'w') as outFile:
        json.dump(dic,outFile)

movistar={}

def coordi():
    while True:
        print("Bienvenido!!")
        print("\nQue quieres hacer el dia de hoy?")
        print("\n1. Registrar Usuario")
        print("\n2. Gestionar Usuarios")
opt=input(":")
movistar=abrirJSON()
if opt == "2":
    print("\n 1. ver usuarios")
    print("\n 2. agregar usuarios")
    print("\n 3. Eliminar ususarios")
    opc=int(input(":"))
    
    if opc == 1:
        for i in range(len(movistar["clientes"])):
                    print(movistar["clientes"][i])
                    
    if opc == 2:
        nuevoUsuario=input("\n¿Como se llama el nuevo usuario?:")
        movistar["campers"].append(nuevoUsuario)
        
        guardarJSON(movistar)
        print("Usuario agregado")
        