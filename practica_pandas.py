import pandas as pd

# 1. Creamos un "Diccionario" con datos de varios productos
datos_negocio = {
    'Producto': ['Remeras', 'Pantalones', 'Gorras', 'Medias'],
    'Costos_Fijos': [10000, 15000, 5000, 2000],
    'Costo_Variable': [50, 80, 30, 10],
    'Precio_Venta': [120, 200, 70, 25]
}

# 2. Convertimos los datos en un DATAFRAME (Es como una hoja de Excel)
df = pd.DataFrame(datos_negocio)

# 3. CALCULOS MASIVOS: Pandas hace la cuenta para todas las filas a la vez
# Calculamos el Margen y el Punto de Equilibrio
df['Margen'] = df['Precio_Venta'] - df['Costo_Variable']
df['Punto_Equilibrio'] = df['Costos_Fijos'] / df['Margen']

# 4. Mostramos los resultados
print("--- TABLA DE PRODUCTOS ---")
print(df)

# 5. Filtrado: ¿Qué productos necesitan vender más de 100 unidades?
print("\n--- PRODUCTOS CON PUNTO DE EQUILIBRIO ALTO ---")
print(df[df['Punto_Equilibrio'] > 100])