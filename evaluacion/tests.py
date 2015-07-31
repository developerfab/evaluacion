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

    def consultaCuadrado(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Cuadrado.objects.create(lado=3, numLados=4, workspace=espacio)
        Cuadrado.objects.create(lado=4, numLados=4, workspace=espacio)
        Cuadrado.objects.create(lado=5, numLados=4, workspace=espacio)
        lista_cuadrado = Cuadrado.objects.filter(workspace_id=espacio.id)
        self.assertEqual(len(lista_cuadrado),3)

    def consultaTriangulo(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Triangulo.objects.create(base=1,altura=1, hipotenusa=2, numLados=3, workspace=espacio)
        Triangulo.objects.create(base=2,altura=3, hipotenusa=2, numLados=3, workspace=espacio)
        Triangulo.objects.create(base=3,altura=2, hipotenusa=2, numLados=3, workspace=espacio)
        lista_triangulo = Triangulo.objects.filter(workspace_id=espacio.id)
        self.assertEqual(len(lista_triangulo),3)

    def consultaHexagono(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Hexagono.objects.create(radio=4, numLados=6, workspace=espacio)
        Hexagono.objects.create(radio=5, numLados=6, workspace=espacio)
        Hexagono.objects.create(radio=6, numLados=6, workspace=espacio)
        Hexagono.objects.create(radio=7, numLados=6, workspace=espacio)
        lista_hexagono = Hexagono.objects.filter(workspace_id=espacio.id)
        self.assertEqual(len(lista_hexagono),4)

    def areaCuadrado(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Cuadrado.objects.create(lado=3, numLados=4, workspace=espacio)
        cuadrado = Cuadrado.objects.filter(workspace=espacio)[0]
        area = cuadrado.getArea()
        self.assertEqual(area, 9)

    def areaTriangulo(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Triangulo.objects.create(base=1,altura=1, hipotenusa=2, numLados=3, workspace=espacio)
        triangulo = Triangulo.objects.filter(workspace=espacio)[0]
        area = triangulo.getArea()
        self.assertEqual(area, 0.5)

    def areaHexagono(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Hexagono.objects.create(radio=4, numLados=6, workspace=espacio)
        hexagono = Hexagono.objects.filter(workspace=espacio)[0]
        area = hexagono.getArea()
        self.assertEqual(area, 83.13843876330611)

    def perimetroCuadrado(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Cuadrado.objects.create(lado=3, numLados=4, workspace=espacio)
        cuadrado = Cuadrado.objects.filter(workspace=espacio)[0]
        perimetro = cuadrado.getPerimetro()
        self.assertEqual(perimetro, 12)

    def perimetroTriangulo(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Triangulo.objects.create(base=1,altura=1, hipotenusa=2, numLados=3, workspace=espacio)
        triangulo = Triangulo.objects.filter(workspace=espacio)[0]
        perimetro = triangulo.getPerimetro()
        self.assertEqual(perimetro, 4.732050807568877)

    def perimetroHexagono(self):
        espacio = WorkSpace.objects.get(nombre="espacio")
        Hexagono.objects.create(radio=4, numLados=6, workspace=espacio)
        hexagono = Hexagono.objects.filter(workspace=espacio)[0]
        perimetro = hexagono.getPerimetro()
        self.assertEqual(perimetro, 24)
