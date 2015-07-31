from django.shortcuts import render
from evaluacion.models import *
from Figura import * 
# Create your views here.

def index(request):
    """
    Pagina principal del sitio
    """
    dic={'title':'Inicio'}
    return render(request, 'index.html', dic)

def createWorkSpace(request):
    """
    Metodo para crear el espacio de trabajo
    """
    diccionario = {'title':'crear espacio'}
    mensaje= ""
    if request.POST:    
        nombre = request.POST['nombre']
        limite = request.POST['limite']
        WorkSpace.objects.create(nombre=nombre, limiteFiguras=limite)
        mensaje = "area creada satisfactoriamente"
    diccionario['mensaje'] = mensaje
    return render(request, 'crearEspacio.html',diccionario)

def consultWorkSpace(request):
    """
    Metodo para la busqueda de los espacios de trabajo
    """
    dic = {'title':'Espacios de trabajo'}
    lista_espacios = WorkSpace.objects.all()
    espacios = []
    for espacio in lista_espacios:
        espacios.append(espacio)
    if len(lista_espacios)>0:
        dic['espacios'] = espacios
    else:
        dic['mensaje'] = 'No existen espacios de trabajo'
    return render(request, 'consultaEspacio.html', dic)

def seeWorkSpace(request, identificador):
    """
    Metodo para ver un espacio individual
    """
    lista_cuadrados = Cuadrado.objects.filter(workspace_id=int(identificador))
    lista_triangulos = Triangulo.objects.filter(workspace_id=int(identificador))
    lista_hexagonos = Hexagono.objects.filter(workspace_id=int(identificador))
    espacio = WorkSpace.objects.get(id=int(identificador))
    diccionario = {'title':espacio.nombre, 'espacio':espacio, 'lista_cuadrados':lista_cuadrados, 'lista_triangulos':lista_triangulos, 'lista_hexagonos':lista_hexagonos}
    return render(request, 'verEspacio.html', diccionario)

def searchWorkSpace(request):
    """
    Metodo para buscar por id un espacio de trabajo
    """
    identificador = request.POST['identificador']
    if WorkSpace.objects.filter(id=int(identificador)).exists():
        return seeWorkSpace(request, identificador)
    return render(request, 'index.html', {'mensaje':'El espacio ingresado no existe'})

def createFigure(request, identificador,figura):
    """
    Metodo para la creacion de las figuras
    """
    diccionario = {'title':'Crear figura'}
    if request.method == 'GET':
        diccionario['identificador']=int(identificador)
        diccionario['figura'] = figura
    else:
        valor = crearFigura(request, identificador, figura)
        if valor:
            diccionario['mensaje'] = "Figura creada con exito"
        else:
            diccionario['mensaje'] = "El area de trabajo esta llena, no se ha creado la figura"
    return render(request, 'crearFigura.html', diccionario)

def deleteFigure(request, identificador, figura, idFigura):
    """
    Metodo para eliminar las figuras
    """
    diccionario={}
    if eliminarFigura(request, identificador, idFigura, figura):
        diccionario['mensaje']="Figura eliminada"
    else:
        diccionario['mensaje']="Error al eliminar la figura"
    return seeWorkSpace(request, identificador)
