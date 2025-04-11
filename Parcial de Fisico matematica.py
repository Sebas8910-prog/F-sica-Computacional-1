# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 14:39:08 2025

@author: Sebas
"""

#Diseño de Clases Abstractas e Concretas para Entidades Matemática
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt 

class EntidadMatematica(ABC):
    @abstractmethod
    def evaluar(self, *args):
        pass
    
    @abstractmethod
    def sumar(self, otra):
        pass
    
    @abstractmethod
    def multiplicar_escalar(self, escalar):
        pass
    
class Vector(EntidadMatematica):
    def _init_(self, componente):
        self.componente =np.array([componente])
        
#Representacion en numpy

    def evaluar(self):
        #Devuelve el valor del vector
        return self.componente[0]
    
    def sumar (self, otra):
        #Suma componente a componente
        nueva_componente=self.componente + otra.componente
        return Vector(nueva_componente[0])
    
    def multiplicar_escalar(self, escalar):
        #Multiplicar por escalar
        nueva_componente=self.componente*escalar
        return Vector(nueva_componente[0])
    
    def obtener_componente(self):
        #Método para acceder a la componente
        return self.componente[0]
    
class Function(EntidadMatematica):
    def _init_(self, funcion):
        self.funcion=funcion #Puede ser lambda o Numpy
        
    def evaluar(self, t):
        #Aquí evalua la función en t
        return self.funcion(t)
    
    def sumar(self, otra):
        #Devuelve una nueva función que es la suma
        nueva_func=lambda t: self.funcion(t)+otra.funcion(t)
        return Function(nueva_func)
    
    def multiplicar_escalar(self, escalar):
        #Devuelve una nueva función multiplicada por el escalar
        nueva_func=lambda t: self.funcion(t)*escalar
        return Function(nueva_func)
    
if __name__ == "__main__":
    # Crear vectores
    v1 = Vector(3)
    v2 = Vector(5)
    suma_v = v1.sumar(v2)
    escalar_v = v1.multiplicar_escalar(2)
    print("Vector 1:", v1.obtener_componente())
    print("Suma de vectores:", suma_v.obtener_componente())
    print("Vector escalado:", escalar_v.obtener_componente())
    
    # Crear funciones
    f1 = Function(lambda t: t**2)
    f2 = Function(lambda t: 3*t)
    suma_f = f1.sumar(f2)
    escalar_f = f1.multiplicar_escalar(2)
    print("Función en t=2:", f1.evaluar(2))
    print("Suma de funciones en t=1:", suma_f.evaluar(1))
    print("Función escalada en t=3:", escalar_f.evaluar(3))