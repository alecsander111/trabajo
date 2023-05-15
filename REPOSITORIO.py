class Comida():
    def __init__(self, nombre, ingredientes, precio):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio

class Bebida(Comida):
    def __init__(self, nombre, ingredientes, precio,sabor):
        super().__init__(nombre, ingredientes, precio)
        self.sabor=sabor

menuComida=[]
menuBebida=[]

for i in range (1,14):
    nombre=str(input(f"Digite el nombre del platillo {i}"))
    ingredientes=str(input("¿Qué ingrediente caracteristico el platillo?"))
    precio=float(input("Inserte el valor del platillo"))
    menuComida.append(Comida(nombre,ingredientes,precio))

for cualquierletra in range(1,12):
    nombre=str(input(f"Digite el nombre de la bebida {cualquierletra}"))
    ingredientes=str(input("¿Qué ingrediente caracteristico la bebida?"))
    precio=float(input("Inserte el valor de la bebida"))
    sabor=str(input("que sabor tiene la bebida?"))
    menuBebida.append(Bebida(nombre,ingredientes,precio,sabor))

""""Hamburguesa de carne simple,doble,pollo pizza de piña,carnes,mexicana,champiñones, perros,simple, choriperro,perrocineta salchipapas simple,choripapa,choricostah"""
"""Jugo de mora->leche
    Limonada->de coco
    Jugo de maracuya->leche
    Jugo de guanabana->leche
    Gaseosa
    Te->Granizado o normal"""
print("")
