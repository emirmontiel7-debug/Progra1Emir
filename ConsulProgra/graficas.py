import os
import pandas as pd
import matplotlib.pyplot as plt

archivo_consultas = "D:/Python/ConsulProgra/registro_consultas.xlsx"

def cargar_datos_consultas():
    if not os.path.exists(archivo_consultas):
        print(f"No se encontró el archivo de consultas: {archivo_consultas}")
        return None

    try:
        df = pd.read_excel(archivo_consultas)
        # Asegurar que existan las columnas necesarias
        if 'Diagnostico' not in df.columns or 'Fecha' not in df.columns:
            print("El archivo de consultas no tiene las columnas requeridas ('Diagnostico' y 'Fecha').")
            return None
        return df
    except Exception as e:
        print(f"Error al leer los datos de consultas para las gráficas: {e}")
        return None


def grafica_distribucion_enfermedades():
    df = cargar_datos_consultas()
    if df is None or df.empty:
        print("No hay datos de consultas para graficar.")
        from tkinter import messagebox
        messagebox.showinfo("Sin Datos", "Aún no hay consultas registradas para graficar.")
        return

    # Usamos directamente la columna Diagnostico
    conteo = df['Diagnostico'].value_counts().head(10)
    if conteo.empty:
        print("No hay diagnósticos válidos para graficar.")
        return

    plt.figure(figsize=(10, 6))
    conteo.plot(kind='bar', color='#2E86C1')
    plt.title('Distribución de Padecimientos (Consultas)', fontsize=16)
    plt.xlabel('Diagnóstico Inteligente')
    plt.ylabel('Cantidad de consultas')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def grafica_tendencia_temporal():
    df = cargar_datos_consultas()
    if df is None or df.empty:
        print("No hay datos de consultas para graficar.")
        from tkinter import messagebox
        messagebox.showinfo("Sin Datos", "Aún no hay consultas registradas para graficar.")
        return

    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Fecha'])
    if df.empty:
        print("No hay fechas válidas en las consultas.")
        return

    df['Periodo'] = df['Fecha'].dt.to_period('M').dt.to_timestamp()

    top_diagnosticos = df['Diagnostico'].value_counts().nlargest(5).index
    df_top = df[df['Diagnostico'].isin(top_diagnosticos)]
    serie = df_top.groupby(['Periodo', 'Diagnostico']).size().unstack(fill_value=0)
    
    if serie.empty:
        print("No hay datos agrupados para la tendencia temporal.")
        from tkinter import messagebox
        messagebox.showinfo("Sin Datos", "No hay suficientes datos agrupados en el tiempo.")
        return

    plt.figure(figsize=(12, 7))
    for diagnostico in serie.columns:
        plt.plot(serie.index, serie[diagnostico], marker='o', label=diagnostico)

    plt.title('Tendencia temporal de padecimientos (Consultas)', fontsize=16)
    plt.xlabel('Periodo')
    plt.ylabel('Consultas registradas')
    plt.xticks(rotation=45)
    plt.legend(title='Diagnóstico', loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()