import pandas as pd
import sqlite3

df = pd.read_excel("C:/Users/Usuario/Desktop/Escriotrio Nico/PROYECTOS/Análisis de ventas y rentabilidad/Ventas y rentabilidad.xlsx")

conn = sqlite3.connect("base_de_Datos.db")


df.to_sql("ventas_tabla", conn, if_exists="replace", index=False)

conn.close()

print("Datos importados")