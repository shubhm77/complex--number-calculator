# --------------
import pandas as pd
import numpy as np
import math

#Code starts here

class complex_numbers():

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs                (self.imag))

    def __add__(self,other):
        a =  self.real + other.real
        b =  self.imag + other.imag
        return complex_numbers(a,b)

    def __sub__(self,other):
        a =  self.real - other.real
        b =  self.imag - other.imag
        return complex_numbers(a,b)

    def __mul__(self,other):
        a =  self.real * other.real - self.imag * other.imag
        b =  self.real * other.imag + self.imag * other.real
        return complex_numbers(a,b)

    def __truediv__(self,other):
        a = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 +                  other.imag ** 2)
        b = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 +                  other.imag ** 2)
        return complex_numbers(a,b)

    def absolute(self):
        abs_value = math.sqrt(self.real ** 2 + self.imag ** 2)
        return abs_value

    def argument(self):
        argument_value_radians = math.atan(self.imag / self.real)
        argument_value_degrees = math.degrees(argument_value_radians)
        return argument_value_degrees

    def conjugate(self):
        a = self.real
        b = -self.imag
        return complex_numbers(a,b)

comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)

comp_sum = comp_1 + comp_2
print("The sum of " + str(comp_1) + " and " + str(comp_2) + " is : " + str(comp_sum))

comp_diff = comp_1 - comp_2
print("The difference of " + str(comp_1) + " and " + str(comp_2) + " is : " + str(comp_diff))

comp_prod = comp_1 * comp_2
print("The product of " + str(comp_1) + " and " + str(comp_2) + " is : " + str(comp_prod))

comp_quot = comp_1 / comp_2
print("The quotient of " + str(comp_1) + " and " + str(comp_2) + " is : " + str(comp_quot))

comp_abs = comp_1.absolute()
print("The absolute value of " + str(comp_1) + " is : " + str(comp_abs))

comp_conj = comp_1.conjugate()
print("The conjugate value of " + str(comp_1) + " is : " + str(comp_conj))

comp_arg = comp_1.argument()
print("The argument value of " + str(comp_1) + " is : " + str(comp_arg))






