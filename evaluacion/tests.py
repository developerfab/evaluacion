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
