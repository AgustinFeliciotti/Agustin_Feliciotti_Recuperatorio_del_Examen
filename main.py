import stock
import ventas


centros = ["Buenos aires", "San Juan", "jujuy", "Neuquen"]
insumos = ["Guantes", "mascarillas", "jeringas", "alcohol en gel", "Test", "rapidos"]

def menu():
    print("MENU PRINCIPAL")
    print("1. Carga stock de insumos")
    print("2. Mostrar centros con mas de 10000 unidades")
    print("3. Mostrar centro con mas de 7000 unidades")
    print("4. Centros con mayor cantidad de cada insumo")
    print("5. Registrar ventas")
    print("6. salir")
    
matriz_stock = []
opcion = -1
while opcion != 0: 
    
    menu()
    opcion =  int(input("Eligi una opcion: "))
    if opcion == 1:
        matriz_stock = stock.cargas_stock(centros,insumos)
    elif opcion == 2:
        stock.mostrar_centro_mayor_stock(matriz_stock, centros)
    elif opcion == 3:
        stock.mostrar_insumos_mayor_stock(matriz_stock, insumos)
    elif opcion == 4:
        stock.centro_con_mas_de_cada_insumo(matriz_stock, centros, insumos)
    elif opcion == 5:
        matriz_stock = ventas.registrar_ventas(matriz_stock, centros, insumos)
    elif opcion == 0:
        print("Saliendo del programa... ")
    else:
        print("Opcion no valida.")