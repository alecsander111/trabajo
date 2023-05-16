class Comida():
    referencia=0
    def __init__(self, nombre, ingredientes, precio):
        referencia+=1
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.referencia=referencia

class Bebida(Comida):
    referenciab=0
    def __init__(self, nombre, ingredientes, precio,sabor):
        referenciab+=1
        super().__init__(nombre, ingredientes, precio)
        self.sabor=sabor
        self.referenciab=referenciab


"""def sumar_productos(productos,pago):
    with open("productos.txt","r") as archivo:
        lineas=archivo.readlines()
        for linea in lineas:
            if "Precio:" in linea:
                precio=float(linea.split(":")[1])
                ventas_totales+=precio
    return ventas_totales"""
    
menuComida=[]
menuBebida=[]

for i in range (1,14):
    nombre=str(input(f"Digite el nombre del platillo {i}: "))
    ingredientes=str(input("¿Qué ingrediente caracteristico el platillo?: "))
    precio=float(input("Inserte el valor del platillo: "))
    menuComida.append(Comida(nombre,ingredientes,precio))
    

for cualquierletra in range(1,12):
    nombre=str(input(f"Digite el nombre de la bebida {cualquierletra}: "))
    ingredientes=str(input("¿Qué ingrediente caracteristico la bebida? "))
    precio=float(input("Inserte el valor de la bebida: "))
    sabor=str(input("que sabor tiene la bebida? "))
    menuBebida.append(Bebida(nombre,ingredientes,precio,sabor))
    



""""Hamburguesa de carne simple,doble,pollo pizza de piña,carnes,mexicana,champiñones, perros,simple, choriperro,perrocineta salchipapas simple,choripapa,choricostah"""
"""Jugo de mora->leche
    Limonada->de coco
    Jugo de maracuya->leche
    Jugo de guanabana->leche
    Gaseosa
    Te->Granizado o normal"""
calificaciones=[]
calificacion=int(input("Como calificaria usted el servicio:\n.Excelente\n.Bueno\n.Ni bueno ni malo\n.Insuficiente\n.Pesimo"))
calificaciones.append(calificacion)
def sumcalificaciones(calificaciones):
    Excelentes=0   
    Buenos=0
    Nibuenos=0
    Insuficentes=0
    Pesimos=0

    for i in calificaciones:
        if calificaciones[i]==1:
            Excelentes+=1
        elif calificaciones[i]==2:
            Buenos+=1
        elif calificaciones[i]==3:
            Nibuenos+=1
        elif calificaciones[i]==4:
            Insuficientes+=1
        elif calificaciones[i]==5:
            Pesimos+=1
    Sumac=Excelentes+Buenos+Nibuenos+Insuficentes+Pesimos
    return "Opiniones totales",str(Sumac),"\nExcelente: ",str(Excelentes),"\nBueno: ",str(Buenos),"\nNi bueno ni malo: ",str(Nibuenos),"\nInsuficiente: ",str(Insuficientes),"\nPesimo: ",str(Pesimos)
print (sumcalificaciones(calificaciones))


