# ---FUNCIONES---

def insertarElemento():
    insertar= input("Indica qué ")
def buscarElemento():
    buscar= input("Indica qué ")    
def modificarElemento():        
    modificar= input("Indica qué ")
def eliminarElemento():  
    eliminar= input("Indica qué ")
def mostrarElementos():
    mostrar= input("Indica qué ")
    
def opciones(eleccion):
    if (eleccion==1):
        return insertarElemento()
    elif (eleccion==2):
        return buscarElemento()    
    elif (eleccion==3):
        return modificarElemento()      
    elif (eleccion==4):
        return eliminarElemento()      
    elif (eleccion==5):
        return mostrarElementos()

# ---MAIN---

lista = []

eleccion = int(input("Bienvenido al polideportivo El Romeral,elija una opcion (del 1 al 5)\
\n 1: Insertar elemento \n 2: Buscar Elemento \n 3: Modificar Elemento\
\n 4: Eliminar Elemento \n 5: Mostrar todos \n Elige que operacion realizar:"))

