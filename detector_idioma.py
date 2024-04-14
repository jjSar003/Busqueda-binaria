from langdetect import detect
import tkinter as tk


def verificar_idioma():
    """Esta funcion permite verificar en que idioma esta la frase introducida, 
    con la libreria Langdetect obtenemos una sigla, revisamos si esta en el 
    diccionario y mostramos en la interfaz un mensaje con el idioma. De no ser
    así mostramos otro mensaje."""
    frase = entrada.get()
    sigla = detect(frase)
    if sigla in lenguajes:
        idioma = lenguajes[sigla]
        mensaje = f"EL idioma de la frase introducida es {idioma.lower()}"
    else:
        mensaje = "No se puedo detectar el idioma de la frase introducida"

    mensaje_final.config(text=mensaje)


def restablecer():
    """El proposito de esta funcion es simple, permite borrar el texto que 
    haya en el campo de entrada"""
    entrada.delete(0, tk.END)

#Diccionario que contiene la mayoria de siglas e idiomas 
lenguajes = {
    'af': 'Afrikáans',
    'ar': 'Árabe',
    'bg': 'Búlgaro',
    'bn': 'Bengalí',
    'ca': 'Catalán',
    'cs': 'Checo',
    'cy': 'Gales',
    'da': 'Danés',
    'de': 'Alemán',
    'el': 'Griego',
    'en': 'Inglés',
    'es': 'Español',
    'et': 'Estonio',
    'fa': 'Persa',
    'fi': 'Finlandés',
    'fr': 'Francés',
    'gu': 'Gujarati',
    'he': 'Hebreo',
    'hi': 'Hindi',
    'hr': 'Croata',
    'hu': 'Húngaro',
    'id': 'Indonesio',
    'it': 'Italiano',
    'ja': 'Japonés',
    'kn': 'Kannada',
    'ko': 'Coreano',
    'lt': 'Lituano',
    'lv': 'Letón',
    'mk': 'Macedonio',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepalí',
    'nl': 'Neerlandés',
    'no': 'Noruego',
    'pa': 'Panyabí',
    'pl': 'Polaco',
    'pt': 'Portugués',
    'ro': 'Rumano',
    'ru': 'Ruso',
    'sk': 'Eslovaco',
    'sl': 'Esloveno',
    'sq': 'Albanés',
    'sv': 'Sueco',
    'sw': 'Suajili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Tailandés',
    'tl': 'Tagalo',
    'tr': 'Turco',
    'uk': 'Ucraniano',
    'ur': 'Urdu',
    'vi': 'Vietnamita',
    'zh-cn': 'Chino (simplificado)',
    'zh-tw': 'Chino (tradicional)'
}

#Creacion de la ventana
ventana = tk.Tk()
ventana.title("Detector de idioma")
ventana.minsize(width=250, height=110)
#Creacion del mensaje inicial
mensaje = "Introduce una frase para verificar su idioma: \
    \n(Si la frase es muy corta el resultado puede ser incorrecto)"
mensaje_inicial = tk.Label(ventana, text=mensaje)
mensaje_inicial.pack()
#Creacion del campo de texto
entrada = tk.Entry(ventana, width=60)
entrada.pack()
#Creacion de un contenedor para los botones
frm_botones = tk.Frame(ventana)
frm_botones.pack()
#Creacion de los botones
boton_consultar = tk.Button(frm_botones, text="Verificar", command=verificar_idioma)
boton_consultar.pack(side= 'left', padx=5)
boton = tk.Button(frm_botones, text="Restablecer", command=restablecer)
boton.pack(side='left')
#Creacion del mensaje final
mensaje_final = tk.Label(ventana, text="")
mensaje_final.pack()

ventana.mainloop()