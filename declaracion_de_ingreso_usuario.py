def main():
    # Initializating financial parameters
    valor_cif_item = 1269.87
    ad_valorem = 76.19
    iva = 255.75
    valor_dolar = 886.34
    precio_unitario_envio = 124.59

    # Calculate the total value of the shipment
    total_envio = precio_unitario_envio * valor_dolar

    # Initialize variables for totals
    total_suma = 0
    valor_agregado_final = 0

    # Initialize variables for total in DIN
    total_DIN = ad_valorem + valor_cif_item

    # Initialize variable for cost without shipping in dollars
    costo_total_sin_envio = 0

    # Product data
    productos = [
        ("a", 3, 126.11),
        ("b", 6, 39.31),
        ("c", 1, 255.71),
        ("d", 1, 320.17)
    ]

    # Calculate the total value of the products in dollars
    for _, cantidad, valor_unitario in productos:
        total_suma += cantidad * valor_unitario * valor_dolar

    # Display input values
    print("\nVALORES INGRESADOS POR PANTALLA:")
    print("==================================")
    print(f"Valor CIF ITEM: {valor_cif_item}")
    print(f"AD Valorem: {ad_valorem}")
    print(f"IVA: {iva}")
    print(f"Valor Dolar: {valor_dolar}")
    print(f"Precio unitario del envío en dólares: {precio_unitario_envio}")
    print("==================================")

    # Display products and their values in CLP
    print("\nPRODUCTOS INGRESADOS:")
    for producto, cantidad, valor_unitario in productos:
        valor_total_producto = valor_unitario * valor_dolar * cantidad
        print(f"Producto: {producto}, Cantidad: {cantidad}, Valor unitario en dólares: {valor_unitario}, "
              f"Valor total en pesos chilenos: ${valor_total_producto:,.2f}")

        # Calculate the value added to the product based on its percentage
        porcentaje = (valor_total_producto / total_suma)
        valor_agregado = total_envio * porcentaje
        valor_agregado_final += valor_agregado * cantidad
        valor_agregado_por_unidad = valor_agregado / cantidad
        print(f"Valor agregado al producto {producto}: ${valor_agregado:,.2f}, "
              f"Valor agregado por unidad: ${valor_agregado_por_unidad:,.2f}")

    # Calculate total cost without shipping in dollars
    costo_total_sin_envio = sum([cantidad * valor_unitario * valor_dolar for _, cantidad, valor_unitario in productos])

    # Display totals in both USD and CLP
    print(f"================================")
    print(f"================================")
    print(f"Suma de los valores totales sin envío en pesos chilenos: ${costo_total_sin_envio:,.2f}")
    print(f"Suma de los valores totales sin envío en dólares: ${costo_total_sin_envio / valor_dolar:,.2f}")
    print(f"================================")
    print(f"================================")
    print(f"Suma de los valores totales con envío en pesos chilenos: ${costo_total_sin_envio + total_envio:,.2f}")
    print(f"Suma de los valores totales con envío en dólares: ${(costo_total_sin_envio + total_envio) / valor_dolar:,.2f}")

    # Display percentages for each product
    print(f"================================")
    print(f"================================")
    print("Porcentajes a distribuir para cada producto:")
    for producto, cantidad, valor_unitario in productos:
        porcentaje = (valor_unitario * valor_dolar * cantidad / total_suma) * 100
        print(f"Producto: {producto}, Porcentaje: {porcentaje:.1f}%")
    print(f"================================")
    print(f"================================")

    # Display total value added to all products
    print(f"Valor total agregado a todos los productos: ${valor_agregado_final:,.2f}")

    # Display total in DIN in both USD and CLP
    print(f"================================")
    print(f"================================")
    print(f"Total en DIN: USD ${total_DIN:,.2f}")
    print(f"Total en DIN: CLP ${total_DIN * valor_dolar:,.1f}")
    
    print(f"================================")
    print(f"================================")

    # Display total cost without shipping in both USD and CLP
    print(f"TOTAL forestry: USD ${(costo_total_sin_envio + total_envio) / valor_dolar:,.2f}")
    print(f"TOTAL forestry: CLP ${costo_total_sin_envio:,.2f}")
    print(f"================================")
    print(f"================================")
    
    # Display the difference between DIN and Forestry
    diferencia_en_usd = total_DIN - (costo_total_sin_envio + total_envio) / valor_dolar
    print(f"DIFERENCIA: USD ${diferencia_en_usd:,.1f}")

    # Display the difference between DIN and Forestry in CLP
    diferencia_en_clp = diferencia_en_usd * valor_dolar
    print(f"DIFERENCIA: CLP ${diferencia_en_clp:,.1f}")
    print(f"================================")
    
    # Calculate neto value
    neto = (costo_total_sin_envio + total_envio) + diferencia_en_clp
    neto_iva = neto * 1.19;

    # Display neto value in both USD and CLP
    print(f"================================")
    print(f"Valor Neto en CLP: ${neto:,.1f}")
    print(f"NETO con IVA: ${neto_iva:,.1f}")
    print(f"================================")
    print(f"================================")


# Display the difference between DIN and Forestry in CLP
    diferencia_en_clp = diferencia_en_usd * valor_dolar
    print(f"DIFERENCIA: CLP ${diferencia_en_clp:,.1f}")
    print(f"================================")

    # Calculate the value to be distributed among products
    cantidad_productos = len(productos)
    valor_a_repartir = diferencia_en_clp / cantidad_productos

    # Display the value to be distributed among products
    print(f"Valor a repartir entre los productos: CLP ${valor_a_repartir:,.1f}")
    print(f"================================")


if __name__ == "__main__":
    main()
