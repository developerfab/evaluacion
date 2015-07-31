from evaluacion.models import *

def crearFigura(request, idWorkSpace, tipo):
    exito = False
    if tipo=='cuadrado':
        lado = request.POST['lado']
        workspace = WorkSpace.objects.get(id=int(idWorkSpace))
        cuadrado = Cuadrado()
        cuadrado.lado = lado
        cuadrado.numLados = 4
        cuadrado.save()
        if workspace.agregarFigura(cuadrado):
            exito = True
        else:
            cuadrado.delete()
        return exito
    elif tipo=='triangulo':
        workspace = WorkSpace.objects.get(id=int(idWorkSpace))
        triangulo = Triangulo()
        triangulo.base = request.POST['base']
        triangulo.altura = request.POST['altura']
        triangulo.hipotenusa = request.POST['hipotenusa']
        triangulo.numLados = 3
        triangulo.save()
        if workspace.agregarFigura(triangulo):
            exito = True
        else:
            triangulo.delete()
        return exito
    elif tipo=='hexagono':
        workspace = WorkSpace.objects.get(id=int(idWorkSpace))
        hexagono = Hexagono()
        hexagono.radio = request.POST['radio']
        hexagono.numLados = 6
        hexagono.save()
        if workspace.agregarFigura(hexagono):
            exito = True
        else:
            hexagono.delete()
        return exito
