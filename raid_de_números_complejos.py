# -*- coding: utf-8 -*-
"""Raid de números complejos

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nnOVW3RJtKgNa4pC81mV_Z8gBRLlBUs6
"""

from abc import ABC, abstractmethod

# Interfaz base (como Animal)
class NumberBase(ABC):
    @abstractmethod
    def square(self):
        """Debe devolver el cuadrado del número"""
        pass

    @abstractmethod
    def get_value(self):
        """Devuelve el valor original del número"""
        pass

# Clase para números reales
class RealNumber(NumberBase):
    def __init__(self, value: float):
        self.value = value

    def square(self):
        return self.value ** 2

    def get_value(self):
        return self.value

# Clase para números complejos
class ComplexNumber(NumberBase):
    def __init__(self, value: complex):
        self.value = value

    def square(self):
        return self.value ** 2

    def get_value(self):
        return self.value

# RAID que suma cuadrados
def sum_of_squares(numbers: list[NumberBase]):
    total = 0
    for number in numbers:
        squared = number.square()
        print(f"Número: {number.get_value()} | Cuadrado: {squared}")
        total += squared
    return total

# Lista mixta de números reales y complejos
numbers = [
    RealNumber(3),
    ComplexNumber(2 + 1j),
    RealNumber(4),
    ComplexNumber(1 - 1j)
]

# Ejecutar RAID y mostrar resultado
resultado = sum_of_squares(numbers)
print(f"Suma total de cuadrados: {resultado}")