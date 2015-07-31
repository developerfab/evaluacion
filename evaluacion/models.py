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

    def getArea(self):
        pass

    def getPerimetro(self):
        pass

    class Meta:
        abstract = True

class Cuadrado(Figura):
    lado = models.IntegerField()

    def getArea(self):
        area = pow(self.lado, 2)
        return area

    def getPerimetro(self):
        perimetro = self.lado*4
        return perimetro  

class Triangulo(Figura):
    base = models.IntegerField()
    altura = models.IntegerField()
    hipotenusa = models.IntegerField()

    def getArea(self):
        area = float(float((self.base)*(self.altura))/2)
        return area

    def getPerimetro(self):
        ladox = math.sqrt(pow(self.hipotenusa,2)-pow(self.base,2))
        perimetro = self.base+self.hipotenusa+ladox
        return perimetro

class Hexagono(Figura):
    radio = models.IntegerField()

    def getApotema(self):
        apotema = math.sqrt(pow(self.radio,2)-pow(self.radio/2,2))
        return apotema

    def getArea(self):
        area = self.getApotema()*self.getPerimetro()
        return area

    def getPerimetro(self):
        perimetro = self.radio*6
        return perimetro
