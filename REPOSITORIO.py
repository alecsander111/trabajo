class Comida():
    def __init__(self, nombre, ingredientes, precio,idd):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.idd = idd
        

class Bebida(Comida):
    def __init__(self, nombre, ingredientes, precio,sabor):
        super().__init__(nombre, ingredientes, precio)
        self.sabor = sabor

menuComida=[]
menuBebida=[]
pagosrealizados=[]
pos=0

def Mostrar():
    print("")
    
    

for i in range (1,14):
    nombre=str(input(f"Digite el nombre del platillo {i}"))
    ingredientes=str(input("¿Qué ingrediente caracteristico el platillo?"))
    precio=float(input("Inserte el valor del platillo"))
    pos=pos+1
    idd=pos
    menuComida.append(Comida(nombre,ingredientes,precio,idd))

for b in range(1,6):
    nombre=str(input(f"Digite el nombre de la bebida {b}"))
    ingredientes=str(input("¿Qué ingrediente caracteristico la bebida?"))
    precio=float(input("Inserte el valor de la bebida"))
    sabor=str(input("que sabor tiene la bebida?"))
    pos=pos+1
    idd=pos
    menuBebida.append(Bebida(nombre,ingredientes,precio,sabor,idd))

#""""Hamburguesa de carne simple,doble,pollo pizza de piña,carnes,mexicana,champiñones, perros,simple, choriperro,perrocineta salchipapas simple,choripapa,choricostah"""
#"""Jugo de mora->leche
 #   Limonada->de coco
  #  Jugo de maracuya->leche
   # Jugo de guanabana->leche
    #Gaseosa
    #Te->Granizado o normal"""
#Metodo de ingreso + Menu alcliente de selecion de carta
valor=0
valor2=0
while i==0:
    print("BIENVENIDO")
    print("1. Registrar Cuenta")
    print("2. Consultar Listado de ventas")
    print("3. Salir")
    opcion = int(input())
    if opcion==1:
        print("registrar ***")
        nplatos = input("Cuantos platos consumieron")
        for i in range(1,nplatos+1):
            print(menuComida[1].idd,"->",menuComida[1].nombre)
            print(menuComida[2].idd,"->",menuComida[2].nombre) 
            print(menuComida[3].idd,"->",menuComida[3].nombre) 
            print(menuComida[4].idd,"->",menuComida[4].nombre) 
            print(menuComida[5].idd,"->",menuComida[5].nombre) 
            print(menuComida[6].idd,"->",menuComida[6].nombre) 
            print(menuComida[7].idd,"->",menuComida[7].nombre) 
            print(menuComida[8].idd,"->",menuComida[8].nombre) 
            print(menuComida[9].idd,"->",menuComida[9].nombre) 
            print(menuComida[10].idd,"->",menuComida[10].nombre) 
            print(menuComida[11].idd,"->",menuComida[11].nombre) 
            print(menuComida[12].idd,"->",menuComida[12].nombre) 
            print(menuComida[13].idd,"->",menuComida[13].nombre)   
            print("////////////////")
            print("Ingrese datos Plato", i )
            plato=int(input("Ingrese el codigo"))
            if plato==1:
                valor=valor+menuComida[1].precio
            elif plato==2:
                valor=valor+menuComida[2].precio
            elif plato==3:
                valor=valor+menuComida[3].precio
            elif plato==4: 
                valor=valor+menuComida[4].precio
            elif plato==5:
                valor=valor+menuComida[5].precio
            elif plato==6:
                valor=valor+menuComida[6].precio
            elif plato==7: 
                valor=valor+menuComida[7].precio
            elif plato==8:
                valor=valor+menuComida[8].precio
            elif plato==9:
                valor=valor+menuComida[9].precio
            elif plato==10: 
                valor=valor+menuComida[10].precio    
            elif plato==11:
                valor=valor+menuComida[11].precio
            elif plato==12:
                valor=valor+menuComida[12].precio
            elif plato==13: 
                valor=valor+menuComida[13].precio    
                
        print("El total de costo de los platos :$",valor)
            
        nbebida = input("Cuantas bebidas consumieron")
        for i in range(1,nbebida+1):
            print(menuBebida[1].idd,"->",menuBebida[1].nombre)
            print(menuBebida[2].idd,"->",menuBebida[2].nombre)
            print(menuBebida[3].idd,"->",menuBebida[3].nombre)
            print(menuBebida[4].idd,"->",menuBebida[4].nombre) 
            print("////////////////")
            print("Ingrese datos de la bebida", i )
            bebidaa=int(input("Ingrese el codigo"))
            if bebidaa==1:
                print=("Su tipo de gaseosa adquirio:")
                print=("1-Gaseosa Personal")
                print=("2-Gaseosa 1 litro")
                pre=int(input())
                if pre==1:
                    valor2=valor2+menuBebida[1].precio
                elif pre==2:
                    litro=2000
                    valor2=valor2+menuBebida[1].precio
                    valor2=valor2+litro
                valor2=valor2+menuComida[1].precio
            elif bebidaa==2:
                print=("Su bebida fue preparada en")
                print=("1-Leche")
                print=("2-Agua")
                pre=int(input())
                if pre==1:
                    valor2=valor2+menuBebida[2].precio
                    leche=2000
                    valor2=valor2+leche
                elif pre==2:
                    valor2=valor2+menuBebida[2].precio
            elif bebidaa==3:
                print=("Su bebida fue preparada en")
                print=("1-Leche")
                print=("2-Agua")
                pre=int(input())
                if pre==1:
                    valor2=valor2+menuBebida[3].precio
                    leche=2000
                    valor2=valor2+leche
                elif pre==2:
                    valor2=valor2+menuBebida[3].precio
            elif bebidaa==4:
                print=("Su bebida fue preparada en")
                print=("1-Leche")
                print=("2-Agua")
                pre=int(input())
                if pre==1:
                    valor2=valor2+menuBebida[4].precio
                    leche=2000
                    valor2=valor2+leche
                elif pre==2:
                    valor2=valor2+menuBebida[4].precio
            elif bebidaa==5:
                print=("Su bebida fue preparada en")
                print=("1-Leche")
                print=("2-Agua")
                pre=int(input())
                if pre==1:
                    valor2=valor2+menuBebida[5].precio
                    leche=2000
                    valor2=valor2+leche
                elif pre==2:
                    valor2=valor2+menuBebida[5].precio
        print("El total de costo de las bebidas es de :$",valor2)            
                
        total = valor+valor2
        pagosrealizados.append(total)
        print("Datos registrados correctamente!")
    elif opcion==2:
        print("mostrar ***")
        Mostrar()
    elif opcion==3:
        exit()

cantidadtotal=0
for i in pagosrealizados:
    cantidadtotal=cantidadtotal+pagosrealizados[i]
print(cantidadtotal)

