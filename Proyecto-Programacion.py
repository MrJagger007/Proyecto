print ("Bienvenido al supermercado Los Pollitos")
entrada=int(input("¿Desea hacer una nueva compra? \n1.Si \n2.No \n")) #Pregunta de compra o salida
if entrada==1:
    nombre=input("Estimada persona usuaria, ¿Cual es su nombre?\n")
    dia=int(input("Ingrese la fecha del dia actual: "))
    if dia<=31:
        mes=int(input("Ingrese la fecha del mes actual: "))
        if mes<=12:
            ano=int(input("Ingrese el año actual: "))
            if ano>=2022: #cierre if anidados de toma datos personales cliente
                #----------------------------------------------------
                repeticion=0
                cantidad=0 #cantidad de productos que el cliente va a llevar
                while repeticion==0:
                    print ("Productos disponibles: \n1. Atún enlatado: 1200 \n2. Cartón de Leche: 1100 \n3. Botella de Vinagre: 1800 \n4. Botella de Vino: 15000 \n5. Coca Cola 2.5L : 2000 \n6. Agua Embotellada 1L : 700 \n7. Chocolate Snickers: 950 \n8. Cartón de Huevos: 2600 \n9. Tosty Mix: 1850 \n10. Plátano: 250 \n11. Gomitas Trululu: 750 \n12. Porción Queque Spoon: 3000 \n13. Bolsa de Arroz 1KG: 1950 \n14. Bolsa de Frijoles 1KG: 1450 \n15. Caja de Helado Dos Pinos: 3180 \n16. Paquete Galletas Oreo: 3600 \n17. Ensure Vainilla: 14500 \n18. Lata Red Bull: 1350 \n19. Chocolate M&M: 900 \n20. Paquete Avena: 1100 \n21. Ice Cubes Gum: 2700 \n22. Botella Cloro 800ML: 2100 \n23. Pasta Dental Colgate: 1900 \n24. Enjuage Bucal LISTERINE 600ML: 2400 \n25.Pechuga de Pollo 1KG: 3300")
                    producto=int(input("Digite el numero del producto que desea llevar: "))#solicitud del producto
                    #agregar proceso para validar los precios de los productos y las cantidades que quiere llevar
                    nuevo=int(input("¿Desea agregar otro producto\n1.Si \n2.No \n"))#validar total de productos
                    nuevo1=nuevo
                    while nuevo1==1:
                        
                        cantidad=cantidad+1 #suma la cantidad de productos que el cliente lleva
                        if cantidad<=20:
                            nuevo=1
                        else:
                            nuevo=2
                    
                    vista=int(input("¿Desea volver a ver la vista de los productos disponibles?\n1.Si \n2.No \n"))
                    if vista==1:
                        repeticion=0
                    else:
                        repeticion=1

                #Inicio else anidados de datos invalidos cliente
            else:
                print("Ha elegido un año invalido")
        else:
            print ("Ha elegido un formato de mes invalido")
    else:
        print ("Ha elegido un formato de dia invalido")
else:
    print ("Que tenga un buen dia")
