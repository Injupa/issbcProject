# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:15:35 2018

@author: i42papaj
"""

#Define la base de conocimiento de un test de drogas

__docformat__ = "restructuredtext"

from esquemaConocimiento import *


class Temperatura(Parametro):
    #Clase que define el parametro temperatura
    def __init__(self):
        Parametro.__init__(self, nombre=u'Cocaina', unidad='ng/ml')

        self.norma=Norma(valor=300, valor2=0, tipo='<=')

class Marihuana(Parametro):
    #Clase que define el parametro marihuana
    def __init__(self):
        Parametro.__init__(self, nombre=u'Marihuana', unidad=u'ng/ml')

        self.norma=Norma(valor=50, valor2=0, tipo='<=')

class Anfetaminas(Parametro):
    #Clase que define el parametro anfetaminas
    def __init__(self):
        Parametro.__init__(self, nombre=u'Anfetaminas', unidad='ng/ml')

        self.norma=Norma(valor=500, valor2=0, tipo='<=')

class Heroina(Parametro):
    #Clase que define el parametro heroina
    def __init__(self):
        Parametro.__init__(self, nombre=u'Heroina', unidad=u'ng/ml')

        self.norma=Norma(valor=300, valor2=0, tipo='<=')

class Morfina(Parametro):
    #Clase que define el parametro morfina
    def __init__(self):
        Parametro.__init__(self, nombre=u'Morfina', unidad=u'ng/ml')

        self.norma=Norma(valor=300, valor2=0, tipo='<=')

def clases():
    #Lista de parametros
    return [Cocaina(), Marihuana(), Anfetaminas(), Heroina(), Morfina()]