import tkinter as tk
import urllib.request

def comprobar_estado(url):
    """Esta funcion recibe como parametro la URL introducida por el usuario y
    segun el codigo de estado HTTP muestra un mensaje en la interfaz. En caso
    de que haya un problema al tomar la informacion de la URL lo indica."""
    try:
        respuesta = urllib.request.urlopen(url)
        estado = respuesta.getcode()
        if estado == 200:
            mensaje_final.config(text="El sitio web esta disponible")
        else:
            mensaje_final.config(text="El sitio web no esta disponible")
    except:
        mensaje_final.config(text="No se pudo verificar la conexion del sitio web")
    

def guardar_url():
    """Esta funcion se encarga de guardar la URL introducida y se la pasa a la
    funcion que comprueba el estado del sitio web."""
    url_usuario = entrada.get()
    comprobar_estado(url_usuario)


#Creacion de la ventana
ventana = tk.Tk()
ventana.title("Comprobador de conexion")
ventana.minsize(width=400, height=100)
#Creacion del mensaje inicial
mensaje = "Ingrese la URL del sitio que desea verificar su conexion:"
mensaje_inicial = tk.Label(ventana, text= mensaje, wraplength=350)
mensaje_inicial.pack()
#Creacion del espacio para el ingreso de la URL
entrada = tk.Entry(ventana, width=60)
entrada.pack()
#Creacion del boton que para almacenar la URL
boton_consultar = tk.Button(ventana, text="Consultar", command=guardar_url)
boton_consultar.pack()
#Creacion del mensaje final
mensaje_final = tk.Label(ventana, text= "")
mensaje_final.pack()

ventana.mainloop()