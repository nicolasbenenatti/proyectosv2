import pandas as pd

# Leer archivo Excel
archivo = "envios.xlsx"
df = pd.read_excel(archivo)

# Filtrar solo los envíos demorados
demorados = df[df["Estado"] == "Demorado"]

# Mostrar cantidad total de demoras
print(f"Total de envíos demorados: {len(demorados)}")

# Agrupar por sucursal
por_sucursal = demorados.groupby("Sucursal")["ID Envío"].count()
print("\nDemoras por sucursal:")
print(por_sucursal)

# Agrupar por motivo de demora
por_motivo = demorados.groupby("Motivo Demora")["ID Envío"].count()
print("\nDemoras por motivo:")
print(por_motivo)

# Exportar los resúmenes a un nuevo archivo Excel
with pd.ExcelWriter("resumen_demoras.xlsx") as writer:
    demorados.to_excel(writer, sheet_name="Detalle Demorados", index=False)
    por_sucursal.to_frame(name="Cantidad").to_excel(writer, sheet_name="Por Sucursal")
    por_motivo.to_frame(name="Cantidad").to_excel(writer, sheet_name="Por Motivo")

print("\nResumen exportado a 'resumen_demoras.xlsx'")
