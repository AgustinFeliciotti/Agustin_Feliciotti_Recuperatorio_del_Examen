def cargas_stock(centros, insumos):
   
    matriz = []
    for i in range(len(centros)):
        fila = [0, 0, 0, 0, 0]
        matriz += [fila]
    
    print("CARGA DE STOCK")
    for i in range (len(centros)):
        print("Centro:", centros[i])
        for j in range(len(insumos)):
            cantidad = int(input("ingrese cantidad de " + insumos[j] + ": "))
            matriz[i][j] = cantidad
            
    print("\n STOCK CARGADO")
    for i in range(len(centros)):
        print("centro:", centros[i])
        for j in range(len(insumos)):
            print(insumos[j], ":", matriz[i][j])
    
    return matriz

def mostrar_centro_mayor_stock(matriz, centros):
    print("\n CENTRO CON MAS DE 10.000 UNIDADES")
    
    for i in range(len(centros)):
        total = 0
        for j in range(len(matriz[i])):
            total = total + matriz
            
        if total > 10000:
            print(centros[i], "tiene", total, "unidades en total:")
            
def mostrar_insumos_mayor_stock(matriz, insumos):
    print("\n INSUMOS CON MAS DE 7000 UNIDADES")
    for j in range(len(insumos)):
        total = 0
        for i in range(len(matriz)):
            total = total + matriz[i][j]
        if total > 7000:
            print(insumos[j], "tiene", total, "unidades totales.")
                
def centro_con_mas_de_cada_insumo(matriz, centros, insumos):
    print("\n CENTROS CON MAYOR CANTIDAD DE CADA INSUMO")
    for j in range(len(insumos)):
        mayor = 0
        pos = 0
        for i in range(len(centros)):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
                pos = i
        print("El centro con mas", insumos[j], "es", centros[pos], "con", mayor, "Unidades.")