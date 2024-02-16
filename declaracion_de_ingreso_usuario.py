def main():
    print("Por favor, introduce los siguientes datos en dólares:")
    valor_cif_item = 1269.87
    ad_valorem = 76.19
    iva = 255.75
    valor_dolar = 886.34
    precio_unitario_envio = 124.59

    # Calcular el total del envío
    total_envio = precio_unitario_envio * valor_dolar

    # Inicializar la variable para almacenar la suma total
    total_suma = 0

    # Inicializar la variable para almacenar el valor total agregado
    valor_agregado_final = 0

    # Inicializar la variable para almacenar el total en DIN
    total_DIN = ad_valorem + valor_cif_item

    # Inicializar la variable para almacenar el costo sin envío en dólares
    TOTAL_forestry = 0

    # Ingreso de productos y cantidades
    productos = [("a", 3, 126.11), ("b", 6, 39.31), ("c", 1, 255.71), ("d", 1, 320.17)]

    # Calcular la suma total de los valores de los productos
    for _, cantidad, valor_unitario in productos:
        total_suma += cantidad * valor_unitario * valor_dolar

    # Muestra los datos de declaración de ingreso
    print("\nVALORES INGRESADOS POR PANTALLA:")
    print("==================================")
    print("Valor CIF ITEM:", valor_cif_item)
    print("AD Valorem:", ad_valorem)
    print("IVA:", iva)
    print("Valor Dolar:", valor_dolar)
    print("Precio unitario del envío en dólares:", precio_unitario_envio)
    print("==================================")

    # Muestra los productos ingresados y su valor en pesos chilenos
    print("\nPRODUCTOS INGRESADOS:")
    for producto, cantidad, valor_unitario in productos:
        valor_total_producto = valor_unitario * valor_dolar * cantidad
        print("Producto: {}, Cantidad: {}, Valor unitario en dólares: {}, Valor total en pesos chilenos: ${:,.2f}"
              .format(producto, cantidad, valor_unitario, valor_total_producto))

        # Calcular el valor que se agrega al producto en función de su porcentaje
        porcentaje = (valor_unitario * valor_dolar * cantidad / total_suma)
        valor_agregado = total_envio * porcentaje
        valor_agregado_final += valor_agregado * cantidad
        valor_agregado_por_unidad = valor_agregado / cantidad
        print("Valor agregado al producto {}: ${:,.2f}, Valor agregado por unidad: ${:,.2f}"
              .format(producto, valor_agregado, valor_agregado_por_unidad))

    # Calcular costo total sin envío
    costo_total_sin_envio = sum([cantidad * valor_unitario * valor_dolar for _, cantidad, valor_unitario in productos])

    # Almacenar el costo sin envío en dólares
    TOTAL_forestry = costo_total_sin_envio

    # Calcular costo total con envío
    costo_total_con_envio = costo_total_sin_envio + total_envio

    print("\nSuma de los valores totales sin envío en pesos chilenos: ${:,.2f}".format(costo_total_sin_envio))
    print("Suma de los valores totales sin envío en dólares: ${:,.2f}".format(costo_total_sin_envio / valor_dolar))
    print("\nSuma de los valores totales con envío en pesos chilenos: ${:,.2f}".format(costo_total_con_envio))
    print("Suma de los valores totales con envío en dólares: ${:,.2f}".format(costo_total_con_envio / valor_dolar))

    # Calcular y mostrar los porcentajes para cada producto
    print("\nPorcentajes a distribuir para cada producto:")
    for producto, cantidad, valor_unitario in productos:
        porcentaje = (valor_unitario * valor_dolar * cantidad / total_suma) * 100
        print("Producto: {}, Porcentaje: {:.1f}%".format(producto, porcentaje))

    # Mostrar el valor total agregado a todos los productos
    print("\nValor total agregado a todos los productos: ${:,.2f}".format(valor_agregado_final))

    # Mostrar el total en DIN en USD
    print("\nTotal en DIN: USD ${:,.2f}".format(total_DIN))
    # Mostrar el total en DIN en CLP
    print("\nTotal en DIN: CLP ${:,.1f}".format(total_DIN * valor_dolar))

    # Mostrar el costo sin envío en dólares
    print("\nTOTAL forestry: USD ${:,.2f} ".format(costo_total_con_envio / valor_dolar))
    # Mostrar el costo sin envío en CLP
    print("\nTOTAL forestry: CLP ${:,.2f} ".format(costo_total_con_envio / valor_dolar * valor_dolar))


if __name__ == "__main__":
    main()
