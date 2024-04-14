#Este scrip va a recibir la URL de un articulo y va a pasar el texto a voz
#Importacion de modulos
from newspaper import Article
from gtts import gTTS
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

def extraer_texto_url(url):
    """Esta funcion va a procesar el texto del articulo en un archivo para poder
    pasarlo de texto a voz"""
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    return articulo.text
    

def pedir_url():
    """Esta funcion va a pedir al usuario la URL y la va a pasar a la funcion 
    que estrae el texto de la URL"""
    print("Bienvenido")
    print("Introduce la URL del articulo que quieres pasar a voz")
    url = input("URL: ")
    return url


def pedir_nombre_archivo():
    """Esta funcion le pide al usuario el nombre que va a recibir el archivo 
    de audio y le asigna el fomato mp3"""
    nombre = input("Ingrese el nombre que va a tener el archivo: ")
    nombre_archivo = nombre + ".mp3"
    return nombre_archivo

def texto_a_voz(frases, archivo_salida):
    """Esta funcion toma las frases extraidas del texto y las une en un solo 
    archivo de voz."""
    voz = gTTS(text=" ".join(frases), lang= "es-us")
    voz.save(archivo_salida)


#Ejecucion del scrip
url = pedir_url()
nombre_archivo = pedir_nombre_archivo()
print("Procesando...")
articulo = extraer_texto_url(url)
frases = sent_tokenize(articulo)
texto_a_voz(frases, nombre_archivo)
print(f"El articulo ha sido guardado en {nombre_archivo}")