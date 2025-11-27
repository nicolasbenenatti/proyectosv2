def calcular_punto_equilibrio():
    print("🍕 Calculadora de Punto de Equilibrio para Pizzería 🍕")
    
    # Entrada de datos
    costos_fijos = float(input("👉 Ingresá tus costos fijos mensuales ($): "))
    costo_pizza = float(input("👉 Ingresá el costo de hacer una pizza ($): "))
    precio_venta = float(input("👉 Ingresá el precio de venta de una pizza ($): "))

    # Validación
    if precio_venta <= costo_pizza:
        print("⚠️ No hay ganancia por pizza. Revisá tus precios.")
        return

    # Cálculos
    ganancia_por_pizza = precio_venta - costo_pizza
    punto_equilibrio = costos_fijos / ganancia_por_pizza
    porcentaje_ganancia = (ganancia_por_pizza / costo_pizza) * 100

    # Resultados
    print("\n📈 Resultados:")
    print(f"✅ Ganancia por pizza: ${ganancia_por_pizza:.2f}")
    print(f"✅ Porcentaje de ganancia por pizza: {porcentaje_ganancia:.2f}%")
    print(f"✅ Punto de equilibrio: {punto_equilibrio:.0f} pizzas (para cubrir costos)")
    print(f"✅ Cada pizza vendida después del punto de equilibrio te deja: ${ganancia_por_pizza:.2f}")

# Ejecutar
calcular_punto_equilibrio()
