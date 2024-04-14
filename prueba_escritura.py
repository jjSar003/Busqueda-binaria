#Importar modulos
import tkinter as tk
import random
import timeit


def calcular_velocidad(tiempo, longitud):
    """Esta funcion calcula la velocidad de escritura en base a la longitud de
    la frase introducida y el tiempo que se tardo el usuario en escribir"""
    velocidad = longitud / tiempo
    resultado.config(text=f"Velocidad: {velocidad:.2f} caracteres por segundo")


def calcular_precision(frase_usuario, frase_original):
    """Esta funcion calcula la precision al tomar cada caracter de las dos
    frases y comprobar si coinciden, guarda el numero de aciertos en una
    variable para realizar una operacion que nos permite saber el porcentaje.
    Por ultimo muesttra este resultado en la interfaz grafica"""
    aciertos = 0
    for i in range(len(frase_usuario)):
        if frase_usuario[i] == frase_original[i]:
            aciertos += 1
    porcentaje_aciertos = ((aciertos/len(frase_original)) * 100)
    precision.config(text=f"Precision: {porcentaje_aciertos:.0f}%")


def iniciar_medicion():
    """Esta funcion toma el tiempo en el que se inicio la prueba, lo guarda en
    una variable global para despues poder utilizarla.
    Si no es la primera ejecucion del script se borra la informacion 
    innecesaria de la interfaz"""
    global inicio, frase_seleccionada
    entrada.delete(0, tk.END)
    etiqueta.config(text="Introduce la frase:")
    inicio = timeit.default_timer()
    frase_seleccionada = random.choice(frases)
    etiqueta_frase.config(text=frase_seleccionada)
    resultado.config(text="")
    precision.config(text="")


def finalizar_medicion():
    """Esta funcion toma el tiempo en el que se finalizo la prueba y hace el
    calculo del tiempo que tardo el usuario en escribir. Ademas de esto guarda
    la frase ingresada por el usuario en una variable y si se cumple la
    condicion llama a las funciones que calculan la precision y la velocidad"""
    fin = timeit.default_timer()
    tiempo = fin - inicio
    frase_usuario = entrada.get()
    etiqueta.config(text="")

    #Si la longitud de la frase que introdujo el usuario es menor o igual a la
    #frase seleccionada se llama a las funciones
    if len(frase_usuario) <= len(frase_seleccionada):
        longitud_frase = len(frase_usuario)
        calcular_velocidad(tiempo, longitud_frase)
        calcular_precision(frase_usuario, frase_seleccionada)
    #Si no, no se llaman a las funciones para evitar que el codigo falle
    elif len(frase_usuario) > len(frase_seleccionada):
        resultado.config(text=f"Has escrito mas de lo solicitado.")

# Lista de frases de ejemplo
frases = [
    "El rápido zorro marrón salta sobre el perro perezoso.",
    "Los pingüinos felices bailan en la nieve.",
    "La luna brilla en el cielo estrellado.",
    "Python es un lenguaje de programación versátil y poderoso.",
    "Los gatos curiosos exploran el jardín por la noche."
]

#Creacion de la ventana
ventana = tk.Tk()
ventana.title("Prueba de escritura")
ventana.minsize(width=300, height=150)
#Se establece el espacio que va a tener la frase seleccionada
etiqueta_frase = tk.Label(ventana, text="", wraplength=300)
etiqueta_frase.pack()
#Creacion del boton iniciar
boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar_medicion)
boton_iniciar.pack()
#Añadir una etiqueta encima del campo de entrada de texto
etiqueta = tk.Label(text="")
etiqueta.pack()
#Creacion del espacio para que el usuario pueda escribir
entrada = tk.Entry(ventana, width=45)
entrada.pack()
#Creacion del boton finalizar
boton_finalizar = tk.Button(ventana, text="Finalizar", command=finalizar_medicion)
boton_finalizar.pack()
#Se asigna el espacio para mostrar la velocidad de escritura
resultado = tk.Label(ventana, text="")
resultado.pack()
#Se asigna el espacio para mostrar la precision
precision = tk.Label(ventana, text="")
precision.pack()
#Esta funcion mantiene la ventana abierta
ventana.mainloop()