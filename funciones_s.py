import json
import modulo_coordinador
def abrirJSON():
    dicFinal={}
    with open('./coordinador.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./coordinador.json",'w') as outFile:
        json.dump(dic,outFile)
data=abrirJSON

def verificar_id():
    while True:
        id_usuario = input("\nDame tu ID: ")  # Pedir el ID
        data = abrirJSON()
        # Buscar el ID dentro de los entrenadores
        if any(coordi["id"] == id_usuario for coordi in data["coordinador"]):
            print("ID válido. Bienvenido.")
            print(modulo_coordinador.coordi())
            break
            
        else:
            print("ID no válido. Inténtalo de nuevo.")