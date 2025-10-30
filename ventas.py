def registrar_ventas(matriz_stock, centros, insumos):
    print("\n REGISTROS DE VENTAS")
    
    for i in range(len(centros)):
        print(i, "-", centros[i])
    num_centros = int(input("Elige el numero del centro donde se realiza la venta: "))
    for j in range(len(insumos)):
        print(j, "-", insumos[j])
    num_insumos = int(input("Elegi el numero del insumo vendido: "))
    
    cantidad_vendidas = int(input("Ingresa la cantidad vendidas"))
    
    if cantidad_vendidas <= matriz_stock[num_centros[num_insumos]]:
        matriz_stock[num_centros]
        [num_insumos] = matriz_stock[num_centros]
        [num_insumos] - cantidad_vendidas
        print("Venta registrada correctamente.")
        print("Numero de stock de", insumos[num_insumos], "en", centros[num_centros], "es", matriz_stock[num_centros][num_insumos])
    else:
        print("Error: no hay suficientes stock para realizar la ventas.")
    
    return matriz_stock