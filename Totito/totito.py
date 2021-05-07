from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Totito')

# Variables en donde se almacenara el nombre de los jugadores
nombre_jugador1 = StringVar()
nombre_jugador2 = StringVar()

# Variables asociadas a los botones que almacenaran el texto de cada uno de ellos
texto_boton1 = StringVar()
texto_boton2 = StringVar()
texto_boton3 = StringVar()
texto_boton4 = StringVar()
texto_boton5 = StringVar()
texto_boton6 = StringVar()
texto_boton7 = StringVar()
texto_boton8 = StringVar()
texto_boton9 = StringVar()

# ------------------------ CAMPOS DE TEXTO PARA INGRESO DEL NOMBRE DE LOS JUGADORES ----------------------------

# PARA JUGADOR 1
label = Label(root, text='Jugador 1', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)
jugador1 = Entry(root, textvariable=nombre_jugador1, bd=5)
jugador1.grid(row=1, column=1, columnspan=8)

# PARA JUGADOR 2
label = Label(root, text='Jugador 2', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)
jugador2 = Entry(root, textvariable=nombre_jugador2, bd=5)
jugador2.grid(row=2, column=1, columnspan=8)



bclick = True   # Variable que al almacenar 'False' permitira establecer el texto 'X' a un boton. Al tener 'True' perminitira establecer el texto '0' en un boton
num_movimientos = 0 # Llevara la cuenta de cuantas veces se han persionado los botones


# -------------------------------- FUNCIONES ------------------------------------------

# Deshabilitara los botones para que no puedan ser presionados (unicamente de ejecutara cuando haya un ganador)
def deshabilitar_boton():
    boton1.config(state=DISABLED)
    boton2.config(state=DISABLED)
    boton3.config(state=DISABLED)
    boton4.config(state=DISABLED)
    boton5.config(state=DISABLED)
    boton6.config(state=DISABLED)
    boton7.config(state=DISABLED)
    boton8.config(state=DISABLED)
    boton9.config(state=DISABLED)

# Se ejecutara cuando se presione un boton
def botonPresionado(texto_boton):
    global bclick, num_movimientos, jugador1, jugador2, jugador

    if texto_boton.get() == '' and bclick == True: # Si no hay nada en el boton (la varable asociada al boton 'texto_boton' esta vacio) y al jugador que le toca llenar una casilla es al jugador 1
        texto_boton.set('X')    # Colocando 'X' en el boton
        bclick = False  # Cambiando el valor de la variables para que en el siguiente turno le toque al jugador2
        checkForWin()   # Verificando si al poner el texto en ese boton es el jugador 1 es el ganador
        num_movimientos += 1    
    
    elif texto_boton.get() == '' and bclick == False: # Si no hay nada en el boton (la varable asociada al boton 'texto_boton' esta vacio) y al jugador que le toca llenar una casilla es al jugador 2
        texto_boton.set(str(0)) # Colocando '0' en el boton
        bclick = True # Cambiando el valor de la variables para que en el siguiente turno le toque al jugador2
        checkForWin() # Verificando si al poner el texto en ese boton es el jugador 2 es el ganador
        num_movimientos += 1
    
    else:   # Significa que el boton ya tiene un texto (una 'X' o un '0')
        tkinter.messagebox.showinfo('Totito', 'La casilla ya está llena.')

# Verificara si el texto esta en los botones este entre uno de los posibles arreglos que hacen que haya un ganador
def checkForWin():
    if (texto_boton1.get() == 'X' and texto_boton2.get() == 'X' and texto_boton3.get() == 'X' or # Posible arreglo ganador: 1,2,3
        texto_boton4.get() == 'X' and texto_boton5.get() == 'X' and texto_boton6.get() == 'X' or # Posible arreglo ganador: 4,5,6
        texto_boton7.get() == 'X' and texto_boton8.get() == 'X' and texto_boton9.get() == 'X' or # Posible arreglo ganador: 7,8,9
        texto_boton1.get() == 'X' and texto_boton5.get() == 'X' and texto_boton9.get() == 'X' or # Posible arreglo ganador: 1,5,9
        texto_boton3.get() == 'X' and texto_boton5.get() == 'X' and texto_boton7.get() == 'X' or # Posible arreglo ganador: 3,5,7
        texto_boton1.get() == 'X' and texto_boton4.get() == 'X' and texto_boton7.get() == 'X' or # Posible arreglo ganador: 1,4,7
        texto_boton2.get() == 'X' and texto_boton5.get() == 'X' and texto_boton8.get() == 'X' or # Posible arreglo ganador: 2,5,8
        texto_boton7.get() == 'X' and texto_boton6.get() == 'X' and texto_boton9.get() == 'X'):  # Posible arreglo ganador: 7,6,9
        deshabilitar_boton()    # Deshabilitando todos los botones
        tkinter.messagebox.showinfo('Totito', '¡Felicidades ' + nombre_jugador1.get() + " has ganado!")

    elif num_movimientos == 8:
        tkinter.messagebox.showinfo('Totito', 'No hubo ganador. ¡Intentalo de nuevo!')
    
    elif (texto_boton1.get() == '0' and texto_boton2.get() == '0' and texto_boton3.get() == '0' or # Posible arreglo ganador: 1,2,3
        texto_boton4.get() == '0' and texto_boton5.get() == '0' and texto_boton6.get() == '0' or # Posible arreglo ganador: 4,5,6
        texto_boton7.get() == '0' and texto_boton8.get() == '0' and texto_boton9.get() == '0' or # Posible arreglo ganador: 7,8,9
        texto_boton1.get() == '0' and texto_boton5.get() == '0' and texto_boton9.get() == '0' or # Posible arreglo ganador: 1,5,9
        texto_boton3.get() == '0' and texto_boton5.get() == '0' and texto_boton7.get() == '0' or # Posible arreglo ganador: 3,5,7
        texto_boton1.get() == '0' and texto_boton4.get() == '0' and texto_boton7.get() == '0' or # Posible arreglo ganador: 1,4,7
        texto_boton2.get() == '0' and texto_boton5.get() == '0' and texto_boton8.get() == '0' or # Posible arreglo ganador: 2,5,8
        texto_boton7.get() == '0' and texto_boton6.get() == '0' and texto_boton9.get() == '0'):  # Posible arreglo ganador: 7,6,9
        deshabilitar_boton() # Deshabilitando todos los botones
        tkinter.messagebox.showinfo('Totito', '¡Felicidades ' + nombre_jugador2.get() + " has ganado!")


# -------------------------------------------------- CREACION Y POSICIONAMIENTO DE LOS BOTONES ----------------------------------------------------------------------

boton1 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton1, command=lambda:botonPresionado(texto_boton1))
boton1.grid(row=3, column=0)

boton2 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8,textvariable=texto_boton2, command=lambda:botonPresionado(texto_boton2))
boton2.grid(row=3, column=1)

boton3 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton3, command=lambda:botonPresionado(texto_boton3))
boton3.grid(row=3, column=2)

boton4 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton4, command=lambda:botonPresionado(texto_boton4))
boton4.grid(row=4, column=0)

boton5 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton5, command=lambda:botonPresionado(texto_boton5))
boton5.grid(row=4, column=1)

boton6 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton6, command=lambda:botonPresionado(texto_boton6))
boton6.grid(row=4, column=2)

boton7 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton7, command=lambda:botonPresionado(texto_boton7))
boton7.grid(row=5, column=0)    

boton8 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton8, command=lambda:botonPresionado(texto_boton8))
boton8.grid(row=5, column=1) 

boton9 = Button(root, text=' ', font='Arial 10 bold', bg='black', fg='white', height=4, width=8, textvariable=texto_boton9, command=lambda:botonPresionado(texto_boton9))
boton9.grid(row=5, column=2)    

root.mainloop()