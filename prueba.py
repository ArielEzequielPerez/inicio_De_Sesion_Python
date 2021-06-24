from tkinter import *
from tkinter import ttk

class Programa:
    def __init__(self, ventana):
        self.ventana = ventana

        marco = LabelFrame(self.ventana, text="Login")
        marco.grid(row = 0 , column = 3, pady = 20)

        #Nombre de usuario 
        Label(marco, text="Usuario: ").grid(row = 0, column = 0)
        Entry(marco).grid(row = 0, column = 1)
        
        #Clave
        Label(marco, text="Contraseña: ").grid(row = 1, column = 0)
        Entry(marco).grid(row = 1, column = 1)

        #Boton
        ttk.Button(marco, text = "Iniciar sesion").grid(row = 2, column = 2)#sticky = W+E)
        ttk.Button(marco, text = "Registrarse").grid(row = 2, column = 3)



if __name__ == "__main__":
    ventana = Tk()
    aplicacion = Programa(ventana)
    ventana.mainloop()

