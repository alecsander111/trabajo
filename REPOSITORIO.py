class Comida():
    def __init__(self, nombre, ingredientes, precio,idd):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.idd = idd

class Bebida(Comida):
    def __init__(self, nombre, ingredientes, precio,sabor):
        super().__init__(nombre, ingredientes, precio,idd)
        self.sabor = sabor

menuComida=[]
menuBebida=[]
pagosrealizados=[]
pos=0
valor=0
valor2=0
calificaciones=[]
pos=0
valor=0
valor2=0
print("      Menu de caja      ")
opcion=int(input("Porfavor digite el numero de la operacion que desea realizar:\n1.Registrar un producto\n2.Registrar un pago\n3.Calificar servicio\n4.Consultar pagos totales\n5.Salir"))
while True:
    if opcion==1:
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
            menuBebida.append(Bebida(nombre,ingredientes,precio,idd,sabor))

    elif opcion==2:
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
                
            nbebida = input("Cuantas bebidas consumieron: ")
            if nbebida==0:
                valor2=0
            else:
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
            cantidad_ingresada=int(input("Ingrese el monto con el que el cliente hizo el pago (sin puntos): "))
            cambio=cantidad_ingresada-total
            print("El cambio a dar es: ",cambio)
            pagosrealizados.append(total)
            print("Datos registrados correctamente!")
   
    elif opcion==3:
            calificacion=int(input("Como calificaria usted el servicio:\n1.Excelente\n2.Bueno\n3.Ni bueno ni malo\n4.Insuficiente\n5.Pesimo"))
            calificaciones.append(calificacion)
            def sumcalificaciones(calificaciones):
                Excelentes=0   
                Buenos=0
                Nibuenos=0
                Insuficientes=0
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
                Sumac=Excelentes+Buenos+Nibuenos+Insuficientes+Pesimos
                return "Opiniones totales: ",str(Sumac),str("\nExcelente: "),str(Excelentes),str("\nBueno: "),str(Buenos),str("\nNi bueno ni malo: "),str(Nibuenos),str("\nInsuficiente: "),str(Insuficientes),str("\nPesimo: "),str(Pesimos)
            print (sumcalificaciones(calificaciones))  
    elif opcion==4:
        cantidadtotal=0
        for i in pagosrealizados:
            cantidadtotal=cantidadtotal+pagosrealizados[i]
        print("Cantidad de ventas: ",cantidadtotal)
    elif opcion==5:
        print("Gracias por probar este algoritmo de 200 lineas :)")
        break


 

        