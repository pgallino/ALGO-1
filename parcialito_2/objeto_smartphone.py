"""Modelar en python:

Una clase App que permita crear aplicaciones con su nombre y una lista de sistemas operativos soportados.

Una clase Smartphone que permita crear smartphones con su nombre de modelo y su nombre de sistema operativo, 
además de permitir instalar apps (debe poder almacenar la instancia de la App).

Los objetos instanciados de dichas clases deberán cumplir con el siguiente comportamiento:

>>> app_fb = App("Facebook", ["ios", "android"])    >>> nexus.instalar(app_itunes)
>>> app_tw = App("Twitter", ["ios", "android"])     Exception(“La app no es compatible
>>> app_itunes = App("iTunes", ["ios"])             con el sistema operativo”)
>>> nexus = Smartphone("Nexus 6P", "android")       >>> iphone.instalar(app_itunes)
>>> iphone = Smartphone("iPhone 7", "ios")          >>> iphone.instalar(app_tw)
>>> nexus.instalar(app_fb)                          >>> print(nexus)
>>> nexus.instalar(app_fb)                          Nexus 6P (android). Apps: Facebook
Exception(“La app ya está instalada”)               >>> print(iphone)
                                                    iPhone 7 (ios). Apps: Itunes, Twitter"""

class App:

    def __init__(self, nombre, sistemas_operativos):
        
        self.nombre = nombre
        self.sistemas_operativos = sistemas_operativos

class Smartphone:

    def __init__(self, modelo, sistema_operativo):
        
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.apps = []
    
    def __str__(self):
        aplicaciones = ", ".join(self.apps)
        return f"{self.modelo} ({self.sistema_operativo}). Apps: {aplicaciones}"
    
    def instalar(self, app):
        if self.sistema_operativo in app.sistemas_operativos:
            if not app.nombre in self.apps:
                self.apps.append(app.nombre)
            elif app.nombre in self.apps:
                raise Exception("La app ya está instalada")
        elif not self.sistema_operativo in app.sistemas_operativos:
            raise Exception("La app no es compatible con el sistema operativo")
        