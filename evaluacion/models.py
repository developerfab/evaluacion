from django.db import models
import math

class WorkSpace(models.Model):
    nombre = models.CharField(max_length=50)
    limiteFiguras = models.IntegerField()

    def agregarFigura(self, figura):
        """
        Metodo para agregar una figura
        """
        if not self.isLleno():
            figura.workspace=self
            figura.save()
            return True
        return False

    def eliminarFigura(self, figura):
        """
        Metodo para eliminar una figura
        """
        figura.delete()
        return True

    def isLleno(self):
        """
        Metodo para saber si un area de trabajo esta llena
        """
        lleno = len(Cuadrado.objects.filter(workspace=self.id))+len(Triangulo.objects.filter(workspace=self.id))+len(Hexagono.objects.filter(workspace=self.id))
        if lleno<self.limiteFiguras:
            return False
        return True

    def getAreaTotal(self):
        areaTotal = 0
        lista_cuadrado = Cuadrado.objects.filter(workspace=self)
        lista_triangulo = Triangulo.objects.filter(workspace=self)
        lista_hexagono = Hexagono.objects.filter(workspace=self)
        for cuadrado in lista_cuadrado:
            areaTotal += cuadrado.getArea()
        for triangulo in lista_triangulo:
            areaTotal += triangulo.getArea()
        for hexagono in lista_hexagono:
            areaTotal += hexagono.getArea()
        return areaTotal

    def getApotemaTotal(self):
        apotemaTotal = 0
        lista_hexagono = Hexagono.objects.filter(workspace=self)
        for hexagono in lista_hexagono:
            apotemaTotal += hexagono.getApotema()
        return apotemaTotal

    def cambiarFigura(self, figura, cambio):
        pass

class Figura(models.Model):
    numLados = models.IntegerField()
    workspace = models.ForeignKey("WorkSpace", blank=True, null=True)

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
