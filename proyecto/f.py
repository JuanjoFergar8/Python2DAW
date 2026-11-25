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
