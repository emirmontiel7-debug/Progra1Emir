import pandas as pd
import os
import matplotlib.pyplot as plt

archivo_excel ="D:/Python/ConsulProgra/registro_pacientes.xlsx"
archivo_consultas = "D:/Python/ConsulProgra/registro_consultas.xlsx"
archivo_admins = "D:/Python/ConsulProgra/registro_admins.xlsx"
lista_p = []

def inicializar_db_admins():
    if not os.path.exists(archivo_admins):
        df_nuevo = pd.DataFrame({"Username": ["admin"], "Password": ["admin123"]})
        df_nuevo.to_excel(archivo_admins, index=False)
        print("Base de datos de administradores inicializada con usuario por defecto.")

def validar_admin_db(username, password):
    inicializar_db_admins()
    try:
        df = pd.read_excel(archivo_admins)
        # Convertimos a string por seguridad
        df['Username'] = df['Username'].astype(str)
        df['Password'] = df['Password'].astype(str)
        
        match = df[(df['Username'] == str(username)) & (df['Password'] == str(password))]
        return not match.empty
    except Exception as e:
        print(f"Error al validar admin: {e}")
        return False

def agregar_admin_db(username, password):
    inicializar_db_admins()
    try:
        df = pd.read_excel(archivo_admins)
        df['Username'] = df['Username'].astype(str)
        
        if str(username) in df['Username'].values:
            return False, "El nombre de usuario ya existe."
            
        nuevo_admin = pd.DataFrame({"Username": [str(username)], "Password": [str(password)]})
        df_resultante = pd.concat([df, nuevo_admin], ignore_index=True)
        df_resultante.to_excel(archivo_admins, index=False)
        return True, "Administrador agregado exitosamente."
    except Exception as e:
        return False, f"Error al agregar: {e}"

def obtener_admins_db():
    inicializar_db_admins()
    try:
        df = pd.read_excel(archivo_admins)
        return df['Username'].astype(str).tolist()
    except Exception:
        return []

def eliminar_admin_db(username):
    inicializar_db_admins()
    try:
        df = pd.read_excel(archivo_admins)
        df['Username'] = df['Username'].astype(str)
        
        if len(df) <= 1:
            return False, "No puedes eliminar al único administrador del sistema."
            
        if str(username) not in df['Username'].values:
            return False, "El usuario no existe."
            
        df = df[df['Username'] != str(username)]
        df.to_excel(archivo_admins, index=False)
        return True, "Administrador eliminado correctamente."
    except Exception as e:
        return False, f"Error al eliminar: {e}"


class Paciente:
    def __init__(self, id_paciente, nombre, edad, genero, historial_medico, fecha):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.historial_medico = historial_medico
        self.fecha=fecha

    def obtener_reporte(self):
        return (f"ID: {self.id_paciente}\n"
                f"Fecha: {self.fecha}\n",
                f"NOMBRE: {self.nombre}\n"
                f"EDAD: {self.edad} años\n"
                f"GÉNERO: {self.genero}\n"
                f"HISTORIAL: {self.historial_medico}")


def normalizar_columnas_excel(df):
    """Normaliza nombres de columnas comunes del Excel para evitar errores de codificación."""
    columnas = [str(c).strip() for c in df.columns]
    rename_map = {}

    for c in columnas:
        clave = c.replace('�', 'e').replace('É', 'E').replace('é', 'e').replace(' ', '').lower()
        if clave == 'genero' or clave == 'género':
            rename_map[c] = 'Género'
        elif clave == 'historial':
            rename_map[c] = 'Historial'
        elif clave == 'fecha':
            rename_map[c] = 'Fecha'
        elif clave == 'nombre':
            rename_map[c] = 'Nombre'
        elif clave == 'id':
            rename_map[c] = 'ID'
        elif clave == 'edad':
            rename_map[c] = 'Edad'

    if rename_map:
        df = df.rename(columns=rename_map)
    df.columns = [str(c).strip() for c in df.columns]
    return df


def guardar_en_excel(p_obj):
    # Usamos los nombres correctos del objeto
    nuevos_datos = {
        "ID": [p_obj.id_paciente],
        "Nombre": [p_obj.nombre],
        "Edad": [p_obj.edad],
        "Género": [p_obj.genero],
        "Historial": [p_obj.historial_medico],
        "Fecha": [p_obj.fecha]
    }
    df_nuevo = pd.DataFrame(nuevos_datos)
    
    if os.path.exists(archivo_excel):
        try:
            df_existente = pd.read_excel(archivo_excel)
            if "Fecha" not in df_existente.columns:
                df_existente["Fecha"] = ""
            df_resultante = pd.concat([df_existente, df_nuevo], ignore_index=True)
            df_resultante.to_excel(archivo_excel, index=False)
            print("Datos agregados al Excel.")
        except Exception as e:
            print(f"Error al escribir en Excel: {e}")
    else:
        df_nuevo.to_excel(archivo_excel, index=False)
        print(f"Archivo {archivo_excel} creado.")
    
class Consulta(Paciente):
    def __init__(self, id_paciente, id_consulta, fecha, sintomas, diagnostico, tratamiento):
        # Buscamos al paciente por ID en la lista global para rellenar los datos heredados de Paciente
        nombre = "N/A"
        edad = "N/A"
        genero = "N/A"
        historial_medico = "N/A"
        p_fecha = "N/A"
        
        for p in lista_p:
            if str(p.id_paciente).strip() == str(id_paciente).strip():
                nombre = p.nombre
                edad = p.edad
                genero = p.genero
                historial_medico = p.historial_medico
                p_fecha = p.fecha
                break
                
        super().__init__(id_paciente, nombre, edad, genero, historial_medico, p_fecha)
        self.id_consulta = id_consulta
        self.fecha = fecha
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def genera_receta(self):
        return f"""
============================================================
              RECETA MÉDICA - HOSPITAL GENERAL
============================================================
ID Paciente:        {self.id_paciente}
Nombre Paciente:    {self.nombre}
Edad:               {self.edad} años
Género:             {self.genero}
------------------------------------------------------------
ID Consulta:        {self.id_consulta}
Fecha de Consulta:  {self.fecha}
------------------------------------------------------------
SÍNTOMAS REPORTADOS:
{self.sintomas}

DIAGNÓSTICO MÉDICO:
{self.diagnostico}

TRATAMIENTO Y RECOMENDACIONES:
{self.tratamiento}
------------------------------------------------------------
Este documento es de carácter informativo.
Consulte a su médico de cabecera ante cualquier duda.
============================================================
"""

class Gestion_datos:
    def __init__(self, t_pacientes=None, t_consultas=None):
        self.t_pacientes = t_pacientes
        self.t_consultas = t_consultas

    def calcular_todo(self):
        reporte_enfermedades = "Aún no hay suficientes datos."
        reporte_paciente_top = "Aún no hay suficientes datos."
        reporte_edad_promedio = "Aún no hay suficientes datos."
        
        try:
            if os.path.exists(archivo_consultas) and os.path.exists(archivo_excel):
                df_consultas = pd.read_excel(archivo_consultas)
                df_pacientes = pd.read_excel(archivo_excel)
                df_pacientes = normalizar_columnas_excel(df_pacientes)
                
                # 1. Enfermedades más comunes
                if 'Diagnostico' in df_consultas.columns and not df_consultas.empty:
                    top_enfermedades = df_consultas['Diagnostico'].value_counts().head(3)
                    reporte_enfermedades = "\n".join([f"• {enf}: {cant} consultas" for enf, cant in top_enfermedades.items()])
                    
                    # 3. Edad promedio por enfermedad (Top 3)
                    df_consultas['ID'] = df_consultas['ID'].astype(str)
                    df_pacientes['ID'] = df_pacientes['ID'].astype(str)
                    
                    df_merged = pd.merge(df_consultas, df_pacientes, on='ID', how='inner')
                    if 'Edad' in df_merged.columns:
                        df_merged['Edad'] = pd.to_numeric(df_merged['Edad'], errors='coerce')
                        df_edades = df_merged.dropna(subset=['Edad'])
                        
                        if not df_edades.empty:
                            lista_promedios = []
                            for enf in top_enfermedades.index:
                                df_enf = df_edades[df_edades['Diagnostico'] == enf]
                                if not df_enf.empty:
                                    prom = df_enf['Edad'].mean()
                                    lista_promedios.append(f"• {enf}: {prom:.1f} años en promedio")
                            
                            if lista_promedios:
                                reporte_edad_promedio = "\n".join(lista_promedios)
                    
                # 2. Paciente con mayor número de consultas
                if 'ID' in df_consultas.columns and not df_consultas.empty:
                    top_id = df_consultas['ID'].value_counts().index[0]
                    max_consultas = df_consultas['ID'].value_counts().iloc[0]
                    
                    paciente_row = df_pacientes[df_pacientes['ID'] == str(top_id)]
                    if not paciente_row.empty:
                        nombre_p = paciente_row.iloc[0]['Nombre']
                        reporte_paciente_top = f"Paciente: {nombre_p} (ID: {top_id})\nTotal de consultas: {max_consultas}"
                    else:
                        reporte_paciente_top = f"ID: {top_id} (No encontrado en registro general)\nTotal de consultas: {max_consultas}"
                        
        except Exception as e:
            print(f"Error calculando reportes: {e}")
            
        return reporte_enfermedades, reporte_paciente_top, reporte_edad_promedio

    def Buscar_paciente(self, query):
        query = query.strip().lower()
        if not query:
            return lista_p
        
        resultados = []
        for p in lista_p:
            nombre = str(p.nombre or "").lower()
            id_paciente = str(p.id_paciente or "").lower()
            genero = str(p.genero or "").lower()
            historial = str(p.historial_medico or "").lower()
            if query in nombre or query in id_paciente or query in genero or query in historial:
                resultados.append(p)
                
        return resultados

class analisis_datos:
    def __init__(self, datos=None):
        self.datos = datos

    def _cargar_datos_consultas(self):
        if not os.path.exists(archivo_consultas):
            print(f"No se encontró el archivo de consultas: {archivo_consultas}")
            return None
        try:
            df = pd.read_excel(archivo_consultas)
            if 'Diagnostico' not in df.columns or 'Fecha' not in df.columns:
                print("El archivo de consultas no tiene las columnas requeridas ('Diagnostico' y 'Fecha').")
                return None
            return df
        except Exception as e:
            print(f"Error al leer los datos de consultas para las gráficas: {e}")
            return None

    def Grafica_distribuccion_enfermedades(self):
        df = self._cargar_datos_consultas()
        if df is None or df.empty:
            print("No hay datos de consultas para graficar.")
            from tkinter import messagebox
            messagebox.showinfo("Sin Datos", "Aún no hay consultas registradas para graficar.")
            return

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
    
    def Grafica_tendencia_temporal(self):
        df = self._cargar_datos_consultas()
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

# -- FUERA DEL PROGRAMA --  
def obtener_siguiente_id():
    # Esta función lee el Excel para saber en qué número se quedó
    if os.path.exists(archivo_excel):
        try:
            df = pd.read_excel(archivo_excel)
            # El siguiente ID será el total de filas + 1
            return len(df) + 1
        except Exception:
            return 1
    return 1

def buscar_paciente_por_nombre(nombre_completo):
    if os.path.exists(archivo_excel):
        df = pd.read_excel(archivo_excel)
        # Buscamos si el nombre ya está en la columna "Nombre"
        if nombre_completo in df['Nombre'].values:
            # Devolvemos los datos del paciente encontrado
            return df[df['Nombre'] == nombre_completo].iloc[0]
    return None

def actualizar_paciente_en_excel(nombre_completo, edad, genero, historial_medico, fecha=None):
    """Actualiza los datos de un paciente existente sin cambiar su ID"""
    if os.path.exists(archivo_excel):
        try:
            df = pd.read_excel(archivo_excel)
            # Verificamos si el paciente existe
            if nombre_completo in df['Nombre'].values:
                # Actualizamos los datos del paciente
                df.loc[df['Nombre'] == nombre_completo, 'Edad'] = edad
                df.loc[df['Nombre'] == nombre_completo, 'Género'] = genero
                df.loc[df['Nombre'] == nombre_completo, 'Historial'] = historial_medico
                if fecha is not None:
                    if 'Fecha' not in df.columns:
                        df['Fecha'] = ""
                    df.loc[df['Nombre'] == nombre_completo, 'Fecha'] = fecha
                df.to_excel(archivo_excel, index=False)
                print(f"[OK] Paciente '{nombre_completo}' actualizado correctamente.")
                return True
        except Exception as e:
            print(f"[ERROR] Error al actualizar paciente: {e}")
            return False
    return False

def cargar_pacientes_desde_excel():
    """Carga todos los pacientes del Excel en la lista de memoria"""
    global lista_p
    lista_p.clear()  # Limpiar la lista existente
    
    if os.path.exists(archivo_excel):
        try:
            df = pd.read_excel(archivo_excel)
            df = normalizar_columnas_excel(df)
            for _, fila in df.iterrows():
                p = Paciente(
                    id_paciente=fila.get('ID', ''),
                    nombre=fila.get('Nombre', ''),
                    edad=fila.get('Edad', ''),
                    genero=fila.get('Género', ''),
                    historial_medico=fila.get('Historial', ''),
                    fecha=fila.get('Fecha', 'N/A')
                )
                lista_p.append(p)
            print(f"[OK] Se cargaron {len(lista_p)} pacientes desde Excel.")
        except Exception as e:
            print(f"[ERROR] Error al cargar pacientes: {e}")
    return lista_p

def actualizar_consultas_excel(id_paciente):
    if os.path.exists(archivo_excel):
        df = pd.read_excel(archivo_excel)
        # Si no existe la columna de consultas, la creamos
        if 'Consultas' not in df.columns:
            df['Consultas'] = 1
        
        # Localizamos al paciente por su ID y le sumamos 1 a su celda de Consultas
        df.loc[df['ID'] == id_paciente, 'Consultas'] += 1
        df.to_excel(archivo_excel, index=False)
        print(f"Consulta sumada al paciente {id_paciente}")