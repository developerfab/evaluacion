from django.test import TestCase
from evaluacion.models import *

# Create your tests here.
class WorkSpaceTest(TestCase):
    def setUp(self):
        WorkSpace.objects.create(nombre="espacio", limiteFiguras=5)

    def creacion(self):
        WorkSpace.objects.create(nombre="espacioTest", limiteFiguras=3)
        #consulta
        espacio = WorkSpace.objects.get(nombre="espacioTest")
        self.assertEqual(espacio.limiteFiguras, 3)

    def consultaEpacios(self):
        espacios = WorkSpace.objects.all()
        self.assertEqual(espacios[0].nombre, "espacio")

class FiguraTest(TestCase):
    def setUp(self):
        WorkSpace.objects.create(nombre="espacio", limiteFiguras=5)

    def crearCuadrado(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Cuadrado.objects.create(lado=3, numLados=4, workspace=espacio)
        cuadrado = Cuadrado.objects.get(workspace=espacio)
        self.assertEqual(cuadrado.numLados, 4)

    def crearTriangulo(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Triangulo.objects.create(base=1,altura=1, hipotenusa=2, numLados=3, workspace=espacio)
        triangulo = Triangulo.objects.get(workspace=espacio)
        self.assertEqual(triangulo.numLados, 3)

    def crearHexagono(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Hexagono.objects.create(radio=4, numLados=6, workspace=espacio)
        hexagono = Hexagono.objects.get(workspace=espacio)
        self.assertEqual(hexagono.radio, 4)
