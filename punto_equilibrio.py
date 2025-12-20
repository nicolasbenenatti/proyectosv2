import tkinter as tk
from tkinter import messagebox, ttk

def calcular():
    try:
        costos_fijos = float(entry_costos_fijos.get())
        costo_variable = float(entry_costo_variable.get())
        precio_venta = float(entry_precio_venta.get())

        if precio_venta <= costo_variable:
            messagebox.showwarning("Advertencia", "El precio de venta debe ser mayor al costo variable.")
            return

        margen = precio_venta - costo_variable
        punto_e = costos_fijos / margen
        
        # Animación simple de barra de progreso
        progress['value'] = 0
        ventana.update_idletasks()
        progress['value'] = 100
        
        res_text = (
            f"💰 Margen: ${margen:.2f}\n"
            f"📈 Punto de Equilibrio: {punto_e:.0f} unidades\n"
            f"💵 Facturación necesaria: ${punto_e * precio_venta:.2f}"
        )
        label_res.config(text=res_text, fg="#2e7d32")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresá solo números.")

ventana = tk.Tk()
ventana.title("Calculadora Pro v4")
ventana.geometry("300x400")
ventana.configure(bg="#eceff1")

tk.Label(ventana, text="PUNTO DE EQUILIBRIO", font=("Arial", 12, "bold"), bg="#eceff1").pack(pady=10)

# Campos
campos = [("Costos Fijos", "entry_costos_fijos"), ("Costo Variable", "entry_costo_variable"), ("Precio Venta", "entry_precio_venta")]
for txt, var in campos:
    tk.Label(ventana, text=txt, bg="#eceff1").pack()
    globals()[var] = tk.Entry(ventana, justify="center")
    globals()[var].pack(pady=5)

tk.Button(ventana, text="CALCULAR", command=calcular, bg="#1565c0", fg="white", width=15).pack(pady=20)

progress = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=5)

label_res = tk.Label(ventana, text="", bg="#eceff1", font=("Arial", 10, "bold"))
label_res.pack(pady=10)

ventana.mainloop()