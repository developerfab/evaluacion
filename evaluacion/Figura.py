from evaluacion.models import Cuadrado, Triangulo, Hexagono
import math

def crearFigura(request, tipo):
    exito = false
    if tipo=='cuadrado':
        lado = request.POST['lado']
        workspace = WorkSpace.objects.get(id=request.POST['id'])
        Cuadrado.objects.create(lado=lado, numLados = 4, workspace=workspace)
        exito = True
    elif tipo=='triangulo':
        pass
    elif tipo=='hexagono':
        pass
    else:
        pass
    return exito