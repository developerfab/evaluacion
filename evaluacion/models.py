from django.db import models
import math

class WorkSpaceManager(models.Manager):
    """
    Metodos de la clase WorkSpace
    """
    def agregarFigura(self, figura):
        pass
    def eliminarFigura(self, figura):
        pass
    def isLleno(self):
        pass
    def getAreaTotal(self):
        pass
    def getApotemaTotal(self):
        pass
    def cambiarFigura(self, figura, cambio):
        pass

class WorkSpace(models.Model):
    nombre = models.CharField(max_length=50)
    limiteFiguras = models.IntegerField()
    objects = WorkSpaceManager()

class Figura(models.Model):
    numLados = models.IntegerField()
    workspace = models.ForeignKey("WorkSpace")

    class Meta:
        abstract = True

class CuadradoManager(models.Manager):
    """
    Metodos de la clase cuadrado
    """
    def getArea(self, cuadrado):
        area = pow(cuadrado.objects.lado, 2)
        return area

    def getPerimetro(self, cuadrado):
        perimetro = cuadrado.objects.lado*4
        return perimetro

class Cuadrado(Figura):
    lado = models.IntegerField()
    objects = CuadradoManager()


class TrianguloManager(models.Manager):
    """
    Metodos de la clase Triangulo
    """
    def getArea(self, triangulo):
        area = ((triangulo.objects.base)*(triangulo.objects.altura)/2)
        return area

    def getPerimetro(self, triangulo):
        ladox = math.sqrt(triangulo.objects.base)

class Triangulo(Figura):
    base = models.IntegerField()
    altura = models.IntegerField()
    hipotenusa = models.IntegerField()
    objects = TrianguloManager()

class HexagonoManager(models.Manager):
    def getApotema(self):
        pass
    def getArea(self):
        pass
    def getPerimetro(self):
        pass

class Hexagono(Figura):
    radio = models.IntegerField()
    objects = HexagonoManager()
