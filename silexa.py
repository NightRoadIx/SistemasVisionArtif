# importar la librería del TuTub
# Instalar la versión 15.0.0
from pytube import YouTube

# Colocar la cadena con el enlace del TuTub
# Revisar que sea hasta donde está:
# v=codigoVideo
enlace = "https://www.youtube.com/watch?v=-5VbcPihV3s"

# Intentar
try:
    # Crear el objeto TuTub
    yt = YouTube(enlace)
    # Obtener algunas características del video
    print("Nombre del video: ", yt.title)
    print("Longitud de video: ", yt.length)
    print("Autor: ", yt.author)
    print("Descripción del video: ", yt.description)
    print("Lista de subtítulos disponibles: ", yt.captions)
    print("Lista de formatos disponibles: ", yt.streams)
    # Obtener el video con la máxima resolución
    stream = yt.streams.get_highest_resolution()
    # A partir de la lista de los formatos disponibles
    # se puede seleccionar que formato se quiere usar
    # usando por ejemplo
    # stream = yt.streams.filter(res="360p").first()
    # En este caso se filtra todos los elementos con
    # resolución de 360p y se selecciona el primero
except Exception as e:
    print(f"Error en conexión con video: {enlace}")
    # Mostrar el error en consola
    print(e)

try:
    # Intentar descargar el video
    # Con el nombre colocado con el atributo
    # filename y formato mp4
    stream.download(filename="Checo.mp4")

    # Si se desea descargar solamente el audio:
    # stream = yt.streams.filter(only_audio=True).first()
except Exception as e:
    print("Error mortal")
    print(e)
