def calcular_punto_equilibrio():
    print("Calculadora de Punto de Equilibrio\n")

    # Entrada de datos
    try:
        costos_fijos = float(input("Ingresar costos fijos mensuales ($): "))
        costo_variable_unitario = float(input("Ingresar costo variable unitario por producto ($): "))
        precio_venta_unitario = float(input("Ingresar precio de venta unitario ($): "))
    except ValueError:
        print("Error: Ingresar valores numéricos válidos.")
        return

    # Validación
    if precio_venta_unitario <= costo_variable_unitario:
        print("No hay margen de ganancia. Revisar precios o costos.")
        return

    # Cálculos
    margen_contribucion = precio_venta_unitario - costo_variable_unitario
    punto_equilibrio_unidades = costos_fijos / margen_contribucion
    porcentaje_ganancia = (margen_contribucion / costo_variable_unitario) * 100

    # Resultados
    print("\nResultados:")
    print(f"Margen de contribución por unidad: ${margen_contribucion:.2f}")
    print(f"Porcentaje de ganancia sobre costo variable: {porcentaje_ganancia:.2f}%")
    print(f"Punto de equilibrio: {punto_equilibrio_unidades:.0f} unidades (para cubrir los costos fijos)")
    print(f"Ganancia neta por unidad vendida después del punto de equilibrio: ${margen_contribucion:.2f}")

if __name__ == "__main__":
    calcular_punto_equilibrio()
