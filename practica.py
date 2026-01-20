import sqlite3
import pandas as pd

def inicializar_db():
    # Conecta (o crea) la base de datos
    conexion = sqlite3.connect("mi_empresa.db")
    cursor = conexion.cursor()
    # Crea la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            monto REAL NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexion.commit()
    conexion.close()

def agregar_gasto(item, monto):
    conexion = sqlite3.connect("mi_empresa.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO gastos (item, monto) VALUES (?, ?)", (item, monto))
    conexion.commit()
    conexion.close()
    print(f"✅ '{item}' guardado en la base de datos.")

def ver_con_pandas():
    # El superpoder: Leer SQL directamente con Pandas
    conexion = sqlite3.connect("mi_empresa.db")
    df = pd.read_sql_query("SELECT * FROM gastos", conexion)
    conexion.close()
    
    if df.empty:
        print("\nLa base de datos está vacía.")
    else:
        print("\n--- REPORTE DESDE BASE DE DATOS (PANDAS) ---")
        print(df)

# --- FLUJO PRINCIPAL ---
inicializar_db()

while True:
    print("\n1. Agregar Gasto | 2. Ver Reporte Pandas | 3. Salir")
    opcion = input("Elegí: ")

    if opcion == "1":
        nom = input("Item: ")
        pre = float(input("Precio: "))
        agregar_gasto(nom, pre)
    elif opcion == "2":
        ver_con_pandas()
    elif opcion == "3":
        break