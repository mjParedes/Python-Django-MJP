from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :)</h1>
    <h3 style='color:red'>Esto es una prueba</h3> """)


def iniciar_sesion(request):
    return HttpResponse("Pasame tu username y tu password por WhatsApp :)")


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)


def anio_nacimiento(request, edad):
    edad = int(edad)
    anio_nac = datetime.now().year - edad

    return HttpResponse(f"Naciste en {anio_nac}")


def vista_plantilla(request):
    # Abrimos el archivo
    archivo = open(
        r"C:\Users\Usuario\Documents\curso-Python-Coder\17_django\proyectocoder\proyectocoder\templates\plantilla_bonita.html")

    # Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {"nombre": "Leonel", "fecha": datetime.now(
    ), "apellido": "Gareis", "edad": 28, "hobbies": ["futbol", "viajar", "programar"]}

    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos  la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    # Retornamos la respuesta
    return HttpResponse(documento)


def vista_listado_alumnos(request):

    archivo = open(
        r"C:\Users\Usuario\Documents\curso-Python-Coder\17_django\proyectocoder\proyectocoder\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia",
                       "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]

    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_alumnos2(request):

    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia",
                       "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]

    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
