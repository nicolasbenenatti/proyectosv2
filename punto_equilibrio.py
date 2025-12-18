import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        costos_fijos = float(entry_costos_fijos.get())
        costo_variable = float(entry_costo_variable.get())
        precio_venta = float(entry_precio_venta.get())

        if precio_venta <= costo_variable:
            messagebox.showwarning("Advertencia", "No hay margen de ganancia. Revisá los precios.")
            return

        margen = precio_venta - costo_variable
        punto_equilibrio = costos_fijos / margen
        porcentaje = (margen / costo_variable) * 100

        resultado = (
            f"Margen de contribución por unidad: ${margen:.2f}\n"
            f"Porcentaje de ganancia: {porcentaje:.2f}%\n"
            f"Punto de equilibrio: {punto_equilibrio:.0f} unidades\n"
            f"Ganancia neta por unidad: ${margen:.2f}"
        )

        resultado_label.config(text=resultado)

    except ValueError:
        messagebox.showerror("Error", "Ingresar valores numéricos válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Punto de Equilibrio")

# Layout
tk.Label(ventana, text="Costos fijos mensuales ($):").grid(row=0, column=0, sticky="e")
entry_costos_fijos = tk.Entry(ventana)
entry_costos_fijos.grid(row=0, column=1)

tk.Label(ventana, text="Costo variable unitario ($):").grid(row=1, column=0, sticky="e")
entry_costo_variable = tk.Entry(ventana)
entry_costo_variable.grid(row=1, column=1)

tk.Label(ventana, text="Precio de venta unitario ($):").grid(row=2, column=0, sticky="e")
entry_precio_venta = tk.Entry(ventana)
entry_precio_venta.grid(row=2, column=1)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(ventana, text="", justify="left", font=("Arial", 10), fg="navy")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
