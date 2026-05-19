from backenP import *
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from datetime import datetime #obetener la fecha del dia que se realiza la consulta
import os

# ═══════════════════════════════════════════════════════════════
#   SISTEMA DE DISEÑO PREMIUM — CLÍNICA MÉDICA
#   Paleta: Navy + Teal + Blanco + Dorado
# ═══════════════════════════════════════════════════════════════

# ─── PALETA PRINCIPAL ───────────────────────────────────────────
C_BG_DARK    = "#0A1628"   # Navy profundo (header, sidebar)
C_BG_MED     = "#112240"   # Navy medio (paneles secundarios)
C_BG_LIGHT   = "#F0F4F8"   # Gris azulado claro (fondo de ventana)
C_BG_CARD    = "#FFFFFF"   # Blanco puro (tarjetas)
C_TEAL       = "#00B4D8"   # Teal brillante (acentos, líneas)
C_TEAL_DARK  = "#0077A8"   # Teal oscuro (hover)
C_GOLD       = "#F4A825"   # Dorado (destacar información clave)
C_GREEN      = "#00C896"   # Verde esmeralda (éxito, guardar)
C_GREEN_DARK = "#00A07A"   # Verde oscuro (hover guardar)
C_RED        = "#E63946"   # Rojo coral (eliminar, alerta)
C_RED_DARK   = "#C1121F"   # Rojo oscuro (hover eliminar)
C_TEXT_WHITE = "#FFFFFF"   # Texto sobre fondo oscuro
C_TEXT_DARK  = "#1A1A2E"   # Texto principal oscuro
C_TEXT_MED   = "#3D5A80"   # Texto secundario azul

# ─── COLORES LEGACY (mantener compatibilidad) ───────────────────
BG_APP          = C_BG_LIGHT
BG_CARD         = C_BG_CARD
TEXT_MAIN       = C_TEXT_DARK
TEXT_SEC        = C_TEXT_MED
BTN_PRIMARY     = C_TEAL
BTN_PRIMARY_ACT = C_TEAL_DARK
BTN_SUCCESS     = C_GREEN
BTN_SUCCESS_ACT = C_GREEN_DARK
BTN_DANGER      = C_RED
BTN_DANGER_ACT  = C_RED_DARK
BTN_DARK        = C_BG_MED
BTN_DARK_ACT    = C_BG_DARK

# ─── TIPOGRAFÍA ─────────────────────────────────────────────────
FONT_H1      = ("Century Gothic", 36, "bold")
FONT_H2      = ("Century Gothic", 24, "bold")
FONT_H3      = ("Segoe UI", 16, "bold")
FONT_H4      = ("Segoe UI", 13, "bold")
FONT_P       = ("Segoe UI", 12)
FONT_P_BOLD  = ("Segoe UI", 12, "bold")
FONT_SMALL   = ("Segoe UI", 10)
FONT_MONO    = ("Consolas", 11)

# ─── HELPERS DE ESTILO ──────────────────────────────────────────
def estilo_ventana(ventana, titulo="", ancho=None, alto=None, centrar=True):
    """Aplica fondo y centrado estándar a cualquier ventana Toplevel o Tk."""
    ventana.configure(bg=C_BG_LIGHT)
    if ancho and alto and centrar:
        sx = ventana.winfo_screenwidth()
        sy = ventana.winfo_screenheight()
        x = (sx // 2) - (ancho // 2)
        y = (sy // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def header_frame(parent, texto, subtexto="", icono="🏥", comando_regresar=None):
    """Crea el header azul marino estándar con icono, título y subtítulo."""
    hf = tk.Frame(parent, bg=C_BG_DARK)
    hf.pack(fill="x")
    # Franja de color teal de 4px
    tk.Frame(hf, bg=C_TEAL, height=4).pack(fill="x")
    inner = tk.Frame(hf, bg=C_BG_DARK)
    inner.pack(fill="x", padx=30, pady=18)
    
    text_frame = tk.Frame(inner, bg=C_BG_DARK)
    text_frame.pack(side="left")
    
    tk.Label(text_frame, text=f"{icono}  {texto}", font=FONT_H2,
             fg=C_TEXT_WHITE, bg=C_BG_DARK).pack(anchor="w")
    if subtexto:
        tk.Label(text_frame, text=subtexto, font=FONT_SMALL,
                 fg=C_TEAL, bg=C_BG_DARK).pack(anchor="w", pady=(2, 0))
                 
    if comando_regresar:
        boton_peligro(inner, "REGRESAR", comando_regresar, ancho=12, icono="←").pack(side="right", padx=10, pady=5)
        
    return hf

def card_frame(parent, pady_outer=10, padx_outer=30):
    """Crea un frame blanco con borde teal sutil (tarjeta)."""
    cf = tk.Frame(parent, bg=C_BG_CARD,
                  highlightbackground=C_TEAL,
                  highlightthickness=1)
    cf.pack(fill="x", padx=padx_outer, pady=pady_outer)
    return cf

def boton_primario(parent, texto, comando, ancho=20, icono=""):
    """Botón teal principal con cursor mano."""
    txt = f"{icono} {texto}" if icono else texto
    return tk.Button(parent, text=txt, command=comando,
                     font=FONT_P_BOLD, fg=C_TEXT_WHITE, bg=C_TEAL,
                     activeforeground=C_TEXT_WHITE, activebackground=C_TEAL_DARK,
                     width=ancho, pady=10, bd=0, cursor="hand2", relief="flat")

def boton_exito(parent, texto, comando, ancho=20, icono=""):
    txt = f"{icono} {texto}" if icono else texto
    return tk.Button(parent, text=txt, command=comando,
                     font=FONT_P_BOLD, fg=C_TEXT_WHITE, bg=C_GREEN,
                     activeforeground=C_TEXT_WHITE, activebackground=C_GREEN_DARK,
                     width=ancho, pady=10, bd=0, cursor="hand2", relief="flat")

def boton_peligro(parent, texto, comando, ancho=20, icono=""):
    txt = f"{icono} {texto}" if icono else texto
    return tk.Button(parent, text=txt, command=comando,
                     font=FONT_P_BOLD, fg=C_TEXT_WHITE, bg=C_RED,
                     activeforeground=C_TEXT_WHITE, activebackground=C_RED_DARK,
                     width=ancho, pady=10, bd=0, cursor="hand2", relief="flat")

def separador(parent, color=C_TEAL, grosor=2, padx=30, pady=8):
    """Línea separadora de color."""
    tk.Frame(parent, bg=color, height=grosor).pack(fill="x", padx=padx, pady=pady)

def campo_entrada(parent, label_texto, ancho=30, show=None):
    """Crea un label + entry estilizados y devuelve el Entry."""
    tk.Label(parent, text=label_texto, font=FONT_H4,
             fg=C_TEXT_MED, bg=C_BG_LIGHT).pack(anchor="w", padx=40, pady=(10, 2))
    e = tk.Entry(parent, font=FONT_P, width=ancho,
                 bg=C_BG_CARD, fg=C_TEXT_DARK,
                 insertbackground=C_TEAL,
                 highlightbackground=C_TEAL, highlightthickness=1,
                 relief="flat", bd=5,
                 show=show if show else "")
    e.pack(padx=40, pady=(0, 5), ipady=6)
    return e
# ════════════════════════════════════════════════════════════════


# Variable global para la ventana principal
ventanaInicial = None

id_cont = obtener_siguiente_id() # Aquí guardamos los diccionarios de pacientes
id_cont = 1   # Contador para el ID automático

def ventana_calcular_todo():
    gestion = Gestion_datos()
    reporte_enfermedades, reporte_paciente_top, reporte_edad_promedio = gestion.calcular_todo()

    vt = tk.Toplevel()
    vt.title("Reportes Analíticos — Clínica")
    estilo_ventana(vt, ancho=860, alto=640)

    header_frame(vt, "REPORTES ANALÍTICOS", "Resumen estadístico del sistema médico", "📊")

    canvas = tk.Canvas(vt, bg=C_BG_LIGHT, highlightthickness=0)
    scroll = ttk.Scrollbar(vt, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    canvas.pack(fill="both", expand=True)
    frame_reportes = tk.Frame(canvas, bg=C_BG_LIGHT)
    canvas.create_window((0, 0), window=frame_reportes, anchor="nw")
    frame_reportes.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    paneles = [
        ("🦠  Enfermedades Más Frecuentes",    reporte_enfermedades,  C_TEAL),
        ("👤  Paciente con Más Consultas",      reporte_paciente_top,  C_GOLD),
        ("📅  Edad Promedio por Enfermedad",    reporte_edad_promedio, C_GREEN),
    ]
    for titulo_p, contenido_p, color_p in paneles:
        cf = tk.Frame(frame_reportes, bg=C_BG_CARD,
                      highlightbackground=color_p, highlightthickness=2)
        cf.pack(fill="x", padx=30, pady=10)
        # Barra lateral de color
        tk.Frame(cf, bg=color_p, width=6).pack(side="left", fill="y")
        inner = tk.Frame(cf, bg=C_BG_CARD)
        inner.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        tk.Label(inner, text=titulo_p, font=FONT_H4,
                 fg=color_p, bg=C_BG_CARD).pack(anchor="w")
        tk.Frame(inner, bg=color_p, height=1).pack(fill="x", pady=4)
        tk.Label(inner, text=contenido_p, font=FONT_P,
                 fg=C_TEXT_DARK, bg=C_BG_CARD, justify="left",
                 wraplength=700).pack(anchor="w")

    pie = tk.Frame(vt, bg=C_BG_DARK)
    pie.pack(fill="x", side="bottom")
    boton_peligro(pie, "REGRESAR", vt.destroy, ancho=15, icono="←").pack(pady=12, padx=20, side="right")


def ventana_agregar_admin(parent):
    v_add = tk.Toplevel(parent)
    v_add.title("Nuevo Administrador")
    estilo_ventana(v_add, ancho=440, alto=400)
    v_add.grab_set()

    header_frame(v_add, "NUEVO ADMIN", "Registrar credenciales de acceso", "🛡️")

    e_user = campo_entrada(v_add, "👤  Nombre de Usuario", ancho=28)
    e_pass = campo_entrada(v_add, "🔒  Contraseña", ancho=28, show="*")

    lbl_msg = tk.Label(v_add, text="", bg=C_BG_LIGHT, font=FONT_SMALL)
    lbl_msg.pack(pady=4)

    def guardar():
        u = e_user.get().strip()
        p = e_pass.get().strip()
        if not u or not p:
            lbl_msg.config(text="⚠ Todos los campos son obligatorios.", fg=C_RED)
            return
        exito, msg = agregar_admin_db(u, p)
        if exito:
            lbl_msg.config(text=f"✔ {msg}", fg=C_GREEN)
            v_add.after(1500, v_add.destroy)
        else:
            lbl_msg.config(text=f"✖ {msg}", fg=C_RED)

    btn_frame = tk.Frame(v_add, bg=C_BG_LIGHT)
    btn_frame.pack(pady=14)
    boton_exito(btn_frame, "GUARDAR", guardar, ancho=12, icono="💾").pack(side="left", padx=5)
    boton_peligro(btn_frame, "REGRESAR", v_add.destroy, ancho=12, icono="←").pack(side="left", padx=5)


def ventana_eliminar_admin(parent, admin_actual):
    v_del = tk.Toplevel(parent)
    v_del.title("Eliminar Administrador")
    estilo_ventana(v_del, ancho=440, alto=380)
    v_del.grab_set()

    header_frame(v_del, "ELIMINAR ADMIN", "Revocar acceso de un administrador", "🗑️")

    admins = obtener_admins_db()
    tk.Label(v_del, text="Selecciona el administrador a eliminar:",
             font=FONT_H4, fg=C_TEXT_MED, bg=C_BG_LIGHT).pack(anchor="w", padx=40, pady=(20, 4))

    style = ttk.Style()
    style.configure("Med.TCombobox", font=("Segoe UI", 12))
    combo = ttk.Combobox(v_del, values=admins, state="readonly",
                         font=FONT_P, width=28, style="Med.TCombobox")
    combo.pack(padx=40, pady=(0, 10), ipady=6)
    if admins:
        combo.current(0)

    lbl_msg = tk.Label(v_del, text="", bg=C_BG_LIGHT, font=FONT_SMALL)
    lbl_msg.pack(pady=4)

    def borrar():
        u = combo.get()
        if not u:
            return
        if u == admin_actual:
            lbl_msg.config(text="⚠ No puedes eliminar tu propia sesión activa.", fg=C_GOLD)
            return
        exito, msg = eliminar_admin_db(u)
        if exito:
            lbl_msg.config(text=f"✔ {msg}", fg=C_GREEN)
            combo['values'] = obtener_admins_db()
            combo.set('')
        else:
            lbl_msg.config(text=f"✖ {msg}", fg=C_RED)

    btn_frame = tk.Frame(v_del, bg=C_BG_LIGHT)
    btn_frame.pack(pady=14)
    boton_peligro(btn_frame, "ELIMINAR", borrar, ancho=12, icono="🗑️").pack(side="left", padx=5)
    boton_primario(btn_frame, "REGRESAR", v_del.destroy, ancho=12, icono="←").pack(side="left", padx=5)


def ventana_dashboard_admin(ventana_aviso, username):
    ventana_aviso.destroy()
    ven = tk.Tk()
    ven.title("Panel de Administración — Clínica")
    ven.state('zoomed')
    ven.configure(bg=C_BG_LIGHT)

    # ── Header ───────────────────────────────────────────────────
    hf = tk.Frame(ven, bg=C_BG_DARK)
    hf.pack(fill="x")
    tk.Frame(hf, bg=C_TEAL, height=4).pack(fill="x")
    hdr_inner = tk.Frame(hf, bg=C_BG_DARK)
    hdr_inner.pack(fill="x", padx=30, pady=16)
    tk.Label(hdr_inner, text="🏥  PANEL DE ADMINISTRACIÓN",
             font=FONT_H2, fg=C_TEXT_WHITE, bg=C_BG_DARK).pack(side="left")
    boton_peligro(hdr_inner, "REGRESAR", lambda: [ven.destroy(), ventana_2()], ancho=12, icono="←").pack(side="right", padx=10)
    tk.Label(hdr_inner, text=f"👤  {username}  •  {datetime.now().strftime('%d/%m/%Y %H:%M')}",
             font=FONT_SMALL, fg=C_TEAL, bg=C_BG_DARK).pack(side="right", padx=15)

    # ── Contenedor central ────────────────────────────────────────
    centro = tk.Frame(ven, bg=C_BG_LIGHT)
    centro.pack(expand=True)

    def tarjeta_boton(parent, icono, titulo, subtitulo, comando, color):
        """Tarjeta de acción con icono, título y descripción."""
        f = tk.Frame(parent, bg=C_BG_CARD,
                     highlightbackground=color, highlightthickness=2,
                     cursor="hand2")
        f.pack(pady=10)
        tk.Frame(f, bg=color, width=6).pack(side="left", fill="y")
        body = tk.Frame(f, bg=C_BG_CARD)
        body.pack(side="left", padx=20, pady=18)
        tk.Label(body, text=f"{icono}  {titulo}", font=FONT_H4,
                 fg=color, bg=C_BG_CARD).pack(anchor="w")
        tk.Label(body, text=subtitulo, font=FONT_SMALL,
                 fg=C_TEXT_MED, bg=C_BG_CARD).pack(anchor="w")
        f.bind("<Button-1>", lambda e: comando())
        for w in [f, body] + list(body.winfo_children()):
            try:
                w.bind("<Button-1>", lambda e: comando())
            except Exception:
                pass
        return f

    # Columna izquierda — Funciones generales
    col1 = tk.Frame(centro, bg=C_BG_LIGHT)
    col1.grid(row=0, column=0, padx=30, pady=20, sticky="n")
    tk.Label(col1, text="┌  FUNCIONES GENERALES", font=FONT_H4,
             fg=C_TEAL, bg=C_BG_LIGHT).pack(anchor="w", pady=(0, 6))
    tk.Frame(col1, bg=C_TEAL, height=2).pack(fill="x", pady=(0, 10))
    tarjeta_boton(col1, "📊", "CALCULAR TODO",
                  "Ver reportes analíticos del sistema",
                  ventana_calcular_todo, C_TEAL)
    tarjeta_boton(col1, "🔍", "BUSCAR PACIENTE",
                  "Consultar expedientes de pacientes",
                  lambda: ventana_buscar_paciente(ven), C_TEAL)
    tarjeta_boton(col1, "📈", "ANÁLISIS DE DATOS",
                  "Gráficas estadísticas del consultorio",
                  ventana_graficas, C_TEAL)

    # Columna derecha — Gestión del sistema
    col2 = tk.Frame(centro, bg=C_BG_LIGHT)
    col2.grid(row=0, column=1, padx=30, pady=20, sticky="n")
    tk.Label(col2, text="┌  GESTIÓN DEL SISTEMA", font=FONT_H4,
             fg=C_GOLD, bg=C_BG_LIGHT).pack(anchor="w", pady=(0, 6))
    tk.Frame(col2, bg=C_GOLD, height=2).pack(fill="x", pady=(0, 10))
    tarjeta_boton(col2, "🔑", "AGREGAR ADMINISTRADOR",
                  "Registrar nuevo usuario con acceso",
                  lambda: ventana_agregar_admin(ven), C_GREEN)
    tarjeta_boton(col2, "🗑️", "ELIMINAR ADMINISTRADOR",
                  "Revocar acceso a un administrador",
                  lambda: ventana_eliminar_admin(ven, username), C_RED)

    # Pie de página
    pie = tk.Frame(ven, bg=C_BG_DARK)
    pie.pack(fill="x", side="bottom")
    tk.Label(pie, text="🏥  Clínica Médica  —  Sistema de Gestión Interna  —  Acceso Restringido",
             font=FONT_SMALL, fg=C_TEAL, bg=C_BG_DARK).pack(pady=8)

    ven.mainloop()


def filtrar_pacientes(query, tree):
    tree.delete(*tree.get_children())
    gestion = Gestion_datos()
    pacientes = gestion.Buscar_paciente(query)
    for paciente in pacientes:
        tree.insert("", "end", values=(paciente.id_paciente, paciente.nombre, paciente.edad,
                                         paciente.genero, paciente.fecha, paciente.historial_medico))


def ventana_buscar_paciente(parent=None):
    global lista_p
    if parent:
        try:
            parent.attributes('-disabled', True)
        except Exception:
            pass

    if not lista_p:
        cargar_pacientes_desde_excel()

    ventana = tk.Toplevel()
    ventana.title("Buscar Paciente — Expedientes")
    ventana.state('zoomed')
    ventana.configure(bg=C_BG_LIGHT)
    ventana.lift()
    ventana.focus_force()
    if parent:
        ventana.transient(parent)
        ventana.grab_set()

    header_frame(ventana, "EXPEDIENTES DE PACIENTES",
                 "Consulta y filtra registros del sistema", "🔍")

    # ── Barra de búsqueda ────────────────────────────────────────
    barra = tk.Frame(ventana, bg=C_BG_DARK)
    barra.pack(fill="x", padx=0, pady=0)
    tk.Frame(barra, bg=C_BG_MED, height=1).pack(fill="x")
    inner_barra = tk.Frame(barra, bg=C_BG_DARK)
    inner_barra.pack(fill="x", padx=20, pady=10)

    tk.Label(inner_barra, text="🔍", font=("Segoe UI", 14),
             fg=C_TEAL, bg=C_BG_DARK).grid(row=0, column=0, padx=(0, 6))
    entrada_busqueda = tk.Entry(inner_barra, width=40, font=FONT_P,
                                bg=C_BG_MED, fg=C_TEXT_WHITE,
                                insertbackground=C_TEAL,
                                highlightbackground=C_TEAL,
                                highlightthickness=1,
                                relief="flat", bd=6)
    entrada_busqueda.grid(row=0, column=1, ipady=6, padx=(0, 10))

    boton_primario(inner_barra, "BUSCAR",
                   lambda: filtrar_pacientes(entrada_busqueda.get(), tree),
                   ancho=12, icono="🔍").grid(row=0, column=2, padx=4)
    boton_primario(inner_barra, "VER TODOS",
                   lambda: filtrar_pacientes("", tree),
                   ancho=12, icono="📄").grid(row=0, column=3, padx=4)

    def cerrar_ventana_busqueda():
        if parent:
            try:
                parent.attributes('-disabled', False)
            except Exception:
                pass
            parent.deiconify()
        ventana.destroy()

    boton_peligro(inner_barra, "REGRESAR",
                  cerrar_ventana_busqueda, ancho=12, icono="←").grid(row=0, column=4, padx=4)

    # ── Tabla de resultados ───────────────────────────────────────
    tabla_frame = tk.Frame(ventana, bg=C_BG_LIGHT)
    tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Med.Treeview",
                    background=C_BG_CARD, foreground=C_TEXT_DARK,
                    fieldbackground=C_BG_CARD, rowheight=32,
                    font=("Segoe UI", 11))
    style.configure("Med.Treeview.Heading",
                    background=C_BG_DARK, foreground=C_TEAL,
                    font=("Segoe UI", 11, "bold"), relief="flat")
    style.map("Med.Treeview",
              background=[("selected", C_TEAL)],
              foreground=[("selected", C_TEXT_WHITE)])

    columnas = ("ID", "Nombre", "Edad", "Género", "Fecha", "Historial")
    tree = ttk.Treeview(tabla_frame, columns=columnas, show="headings",
                        height=20, style="Med.Treeview")
    anchos = {"ID": 100, "Nombre": 200, "Edad": 70, "Género": 110, "Fecha": 150, "Historial": 280}
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=anchos.get(col, 140), anchor="w")

    vsb = ttk.Scrollbar(tabla_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(tabla_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    tabla_frame.grid_rowconfigure(0, weight=1)
    tabla_frame.grid_columnconfigure(0, weight=1)

    filtrar_pacientes("", tree)
    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana_busqueda)
    ventana.grab_set()
    ventana.wait_window()

def guardar_datos(n, a, e, g, h, etiqueta_aviso):
    global id_cont, lista_p
    nombre_completo = f"{n.get()} {a.get()}"
    paciente_existente = buscar_paciente_por_nombre(nombre_completo)
    
    try:
        if paciente_existente is not None:
            # El paciente ya existe - ACTUALIZAR sus datos sin cambiar el ID
            id_actual = paciente_existente['ID']
            fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
            
            # Actualizar en Excel
            actualizar_paciente_en_excel(nombre_completo, e.get(), g.get(), h.get(), fecha_actual)
            
            # Actualizar en la lista de memoria
            for paciente in lista_p:
                if paciente.nombre == nombre_completo:
                    paciente.edad = e.get()
                    paciente.genero = g.get()
                    paciente.historial_medico = h.get()
                    paciente.fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
                    break
            
            etiqueta_aviso.config(text=f"¡Actualizado: {id_actual}!", fg="#FFA500")
            print(f"[OK] Datos actualizados para: {nombre_completo}")
            
        else:
            # Paciente nuevo - CREAR nuevo registro con ID único
            id_cont = obtener_siguiente_id()
            id_actual = f"PAC-00{id_cont}"
            fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
            
            p = Paciente(
                id_paciente=id_actual, 
                nombre=f"{n.get()} {a.get()}", 
                edad=e.get(), 
                genero=g.get(), 
                historial_medico=h.get(),
                fecha=fecha_actual
            )
            
            # 1. Guarda en el archivo físico
            guardar_en_excel(p)
            
            # 2. Guarda en la lista de la memoria
            lista_p.append(p)
            
            etiqueta_aviso.config(text=f"¡Registrado: {id_actual}!", fg="#27AE60")
            print(f"[OK] Nuevo paciente registrado: {id_actual}")
        
    except Exception as err:
        print(f"[ERROR] Error al guardar: {err}")
        etiqueta_aviso.config(text="Error al registrar", fg="red")

def generar_reporte():
    if not lista_p:
        print("No hay pacientes registrados aún.")
        return

    # Tomamos el último paciente registrado
    p_obj = lista_p[-1]
    
    def guardar_reporte():
        """Función para guardar el reporte en un archivo"""
        archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivo de Texto", "*.txt"), ("PDF", "*.pdf"), ("Todos", "*.*")],
            initialfile=f"Reporte_{p_obj.id_paciente}_{datetime.now().strftime('%d%m%Y_%H%M%S')}"
        )
        
        if archivo:
            try:
                contenido_reporte = f"""
================================================================================
                    HOSPITAL GENERAL DE CU2
        Unidad de Gestión de Datos - Reporte Oficial #HGC-P-1001
================================================================================

REPORTE DE DATOS DEL PACIENTE (DATOS DE IDENTIFICACIÓN)

ID Paciente:        {p_obj.id_paciente}
Nombre:             {p_obj.nombre}
Edad:               {p_obj.edad}
Genero:             {p_obj.genero}
Fecha de Emisión:   {p_obj.fecha}

HISTORIAL MÉDICO:
{p_obj.historial_medico}

================================================================================
ESTE DOCUMENTO ES DE CARÁCTER CONFIDENCIAL
================================================================================
Fin del Reporte - Solo Datos del Instituto de Identificación del Paciente
"""
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write(contenido_reporte)
                print(f"[OK] Reporte guardado exitosamente en: {archivo}")
                from tkinter import messagebox
                messagebox.showinfo("Exito", f"Reporte guardado en:\n{archivo}")
            except Exception as e:
                print(f"[ERROR] Error al guardar: {e}")
                from tkinter import messagebox
                messagebox.showerror("Error", f"No se pudo guardar el reporte:\n{str(e)}")
    
    rep_ventana = tk.Toplevel()
    rep_ventana.title("REPORTE OFICIAL - HOSPITAL CU2")
    rep_ventana.geometry("700x800")
    rep_ventana.configure(bg="#F0F3F4") # Gris muy claro de fondo
    rep_ventana.attributes('-topmost', True)

    
    header = tk.Frame(rep_ventana, bg="white", height=100, bd=1, relief="solid")
    header.pack(fill="x", padx=20, pady=(20, 0))
    
    # Texto del Hospital
    tk.Label(header, text="HOSPITAL GENERAL DE CU2", 
             font=("Helvetica", 18, "bold"), fg="#2E596E", bg="white").place(x=20, y=20)
    tk.Label(header, text="Unidad de Gestión de Datos - Reporte Oficial #HGC-P-1001", 
             font=("Helvetica", 9), fg="#5D6D7E", bg="white").place(x=20, y=55)
    
    # Simulación de Código de Barras (Derecha)
    barras_frame = tk.Frame(header, bg="black", width=120, height=40)
    barras_frame.place(x=540, y=20)
    tk.Label(header, text="Código de Identificación", font=("Arial", 7), bg="white").place(x=540, y=65)

    # Fecha del reporte decorada
    fecha_frame = tk.Frame(header, bg="#EAECEE", bd=1, relief="flat")
    fecha_frame.place(x=540, y=85)
    
    tk.Label(fecha_frame, text=f"FECHA DE EMISIÓN: {p_obj.fecha}", 
             font=("Arial", 8, "bold"), bg="#EAECEE", fg="#2E596E", 
             padx=5, pady=2).pack()

    # --- TÍTULO DE LA SECCIÓN ---
    seccion_titulo = tk.Frame(rep_ventana, bg="#EAECEE", bd=1, relief="solid")
    seccion_titulo.pack(fill="x", padx=20)
    tk.Label(seccion_titulo, text="REPORTE DE DATOS DEL PACIENTE (DATOS DE IDENTIFICACIÓN)", 
             font=("Arial", 10, "bold"), bg="#EAECEE").pack(pady=5)

    # --- CUERPO DEL REPORTE (Datos del Paciente) ---
    hoja = tk.Frame(rep_ventana, bg="white", bd=1, relief="solid")
    hoja.pack(padx=20, pady=0, fill="both", expand=True)

    # Estilo de datos alineados
    def crear_campo(parent, label, valor, y_pos):
        f = tk.Frame(parent, bg="white")
        f.place(x=30, y=y_pos)
        tk.Label(f, text=label, font=("Arial", 11, "bold"), bg="white", fg="black").pack(side="left")
        tk.Label(f, text=valor, font=("Arial", 11), bg="white", fg="#2C3E50").pack(side="left", padx=5)

    crear_campo(hoja, "id_paciente:", p_obj.id_paciente, 30)
    crear_campo(hoja, "Nombre:", p_obj.nombre, 70)
    crear_campo(hoja, "Edad:", p_obj.edad, 110)
    crear_campo(hoja, "Genero:", p_obj.genero, 150)
    
    # Historial Médico con ajuste de texto
    tk.Label(hoja, text="Historial_medico:", font=("Arial", 11, "bold"), 
             bg="white").place(x=30, y=190)
    
    historial_txt = tk.Message(hoja, text=p_obj.historial_medico, font=("Arial", 11), 
                               bg="white", fg="#2C3E50", width=600, anchor="nw")
    historial_txt.place(x=30, y=215)

    # --- PIE DE PÁGINA ---
    tk.Label(hoja, text="Fin del Reporte - Solo Datos del Instituto de Identificación del Paciente", 
             font=("Arial", 9, "italic"), bg="white", fg="#7F8C8D").pack(side="bottom", pady=10)

    # --- SECCIÓN DE DISEÑO ADICIONAL (Control de Documento sin tablas) ---
    control_frame = tk.Frame(rep_ventana, bg="#D5D8DC", bd=1, relief="solid")
    control_frame.pack(fill="x", padx=20, pady=(0, 20))
    
    tk.Label(control_frame, text="ESTE DOCUMENTO ES DE CARÁCTER CONFIDENCIAL", 
             font=("Arial", 8, "bold"), bg="#D5D8DC", fg="#424949").pack(pady=10)
    
    # --- BOTONES ---
    botones_frame = tk.Frame(rep_ventana, bg="#F0F3F4")
    botones_frame.pack(pady=(0, 20))
    
    # Botón de Guardar Reporte
    tk.Button(botones_frame, text="💾 GUARDAR REPORTE", command=guardar_reporte,
              bg="#27AE60", fg="white", font=("Arial", 10, "bold"), 
              bd=0, padx=25, pady=10, cursor="hand2").pack(side="left", padx=10)
    
    # Botón de Cerrar (Regresar)
    tk.Button(botones_frame, text="← REGRESAR", command=rep_ventana.destroy,
              bg="#2E596E", fg="white", font=("Arial", 10, "bold"), 
              bd=0, padx=25, pady=10, cursor="hand2").pack(side="left", padx=10)


def ventana_graficas():
    ventana = tk.Toplevel()
    ventana.title("Análisis de Datos - Gráficas")
    ventana.state('zoomed')
    ventana.configure(bg="#F4F7F6")

    tk.Label(ventana, text="ANÁLISIS DE GRÁFICAS", fg="#000000", bg="#F4F7F6",
             font=("Century Gothic", 36, "bold")).pack(pady=40)

    texto = tk.Label(ventana, text="Selecciona una gráfica para mostrar el análisis de datos del consultorio.",
                     fg="#2C3E50", bg="#F4F7F6", font=("Arial", 14))
    texto.pack(pady=10)

    panel_botones = tk.Frame(ventana, bg="#F4F7F6")
    panel_botones.pack(pady=20)

    analisis = analisis_datos()

    tk.Button(panel_botones, text="Distribución de enfermedades", command=analisis.Grafica_distribuccion_enfermedades,
              font=("Segoe UI", 12, "bold"), fg="white", bg="#27AE60", bd=0, padx=25, pady=12, cursor="hand2").pack(pady=10)

    tk.Button(panel_botones, text="Tendencia temporal por enfermedad", command=analisis.Grafica_tendencia_temporal,
              font=("Segoe UI", 12, "bold"), fg="white", bg="#2E596E", bd=0, padx=25, pady=12, cursor="hand2").pack(pady=10)

    tk.Button(panel_botones, text="← Regresar", command=ventana.destroy,
              font=("Segoe UI", 12, "bold"), fg="white", bg="#A93226", bd=0, padx=25, pady=12, cursor="hand2").pack(pady=10)


def obtener_diagnostico_por_sintomas(sintomas):
    texto = (sintomas or "").strip().lower()
    if not texto or texto == "(describa síntomas aquí...)":
        return (
            "No se detectaron síntomas claros",
            "Por favor describe tus molestias con palabras clave como 'dolor', 'tos', 'náuseas', 'mareo', 'cansancio', etc."
        )

    condiciones = [
        {
            "nombre": "Migraña severa / Cefalea tensional aguda",
            "keywords": ["dolor de cabeza", "cefalea", "jaqueca", "punzadas", "mareo", "luz", "fotofobia", "sienes", "náuseas", "vómito"],
            "tratamiento": "Descanso en un lugar oscuro y sin ruido. Hidratación, compresas frías en la frente y analgésicos de venta libre. Si tienes náuseas constantes y no cede, acude a un neurólogo."
        },
        {
            "nombre": "Intoxicación alimentaria / Infección fuerte",
            "keywords": ["vómito", "náuseas", "dolor de panza", "dolor de estomago", "estómago", "diarrea", "comí algo malo", "asco", "dolor de cabeza"],
            "tratamiento": "Rehidratación inmediata con suero oral en pequeños sorbos. Dieta blanda si se tolera. Si el vómito o dolor intenso no cede en horas, acudir a urgencias."
        },
        {
            "nombre": "Gripe severa / COVID-19 / Infección Viral",
            "keywords": ["fiebre", "escalofríos", "dolor articular", "dolor muscular", "dolor de cuerpo", "cuerpo cortado", "agotamiento", "dolor de cabeza", "náuseas", "pérdida de olfato", "tos seca", "garganta"],
            "tratamiento": "Aislamiento preventivo, reposo en cama, antitérmicos (paracetamol) para la fiebre y dolor, abundante ingesta de líquidos. Vigilancia médica si hay falta de aire."
        },
        {
            "nombre": "Indigestión / Gastritis / Cólicos",
            "keywords": ["dolor de panza", "cólico", "ardor", "acidez", "pesadez", "gases", "inflamación", "agruras"],
            "tratamiento": "Evita comidas pesadas, grasosas o picantes. Hidrátate bien, toma infusiones (como manzanilla) y descansa. Evita acostarte inmediatamente tras comer."
        },
        {
            "nombre": "Dengue / Zika / Chikungunya (Sospecha)",
            "keywords": ["fiebre muy alta", "dolor de ojos", "detrás de los ojos", "dolor de huesos", "dolor de cabeza", "náuseas", "sarpullido", "picazón"],
            "tratamiento": "URGENTE: NO tomar aspirina ni ibuprofeno. Tomar paracetamol para fiebre/dolor, mucho reposo, mantener hidratación extrema y acudir a clínica para análisis."
        },
        {
            "nombre": "Apendicitis (Sospecha de Emergencia)",
            "keywords": ["dolor muy fuerte en la panza", "dolor lado derecho", "ombligo", "náuseas", "vómito", "fiebre leve", "no puedo caminar", "dolor agudo"],
            "tratamiento": "EMERGENCIA MÉDICA: Ir inmediatamente a urgencias médicas. NO tomar analgésicos ni antibióticos, y no comer ni beber nada hasta ser valorado por un cirujano."
        },
        {
            "nombre": "Vértigo / Trastorno del oído",
            "keywords": ["mareo intenso", "todo me da vueltas", "náuseas", "zumbido", "pérdida de equilibrio", "vértigo", "oído", "asco"],
            "tratamiento": "Recostarse inmediatamente y mantener la vista en un punto fijo. Evitar movimientos bruscos de cabeza. Consultar a un otorrinolaringólogo o neurólogo si persiste."
        },
        {
            "nombre": "Resaca / Deshidratación severa",
            "keywords": ["cruda", "resaca", "alcohol", "tomé mucho", "dolor de cabeza", "náuseas", "mareo", "boca seca", "sed extrema"],
            "tratamiento": "Abundante agua y electrolitos. Comida ligera (caldos). Analgésicos suaves como paracetamol (evitar ibuprofeno si hay irritación gástrica). Reposo."
        },
        {
            "nombre": "Alergia respiratoria / Rinitis",
            "keywords": ["picazón en la nariz", "ojos llorosos", "estornudos frecuentes", "alergia", "polvo", "picor nasal", "congestión nasal", "mocos"],
            "tratamiento": "Evitar la exposición al alérgeno. Uso de antihistamínicos según indicación médica. Lavados nasales con solución salina."
        },
        {
            "nombre": "Lumbalgia / Tensión muscular o Estrés",
            "keywords": ["dolor de espalda", "cintura", "lumbago", "rigidez", "tensión", "estrés", "nuca", "cuello", "dolor de cabeza"],
            "tratamiento": "Aplicar calor local, masajes descontracturantes, estiramientos suaves, evitar cargar peso. Aprender a manejar la ansiedad."
        },
        {
            "nombre": "Infección de vías urinarias (Cistitis)",
            "keywords": ["dolor al orinar", "ardor al orinar", "mal de orín", "orinar a cada rato", "sangre en orina", "vejiga"],
            "tratamiento": "Aumentar ingesta de agua natural. No aguantar las ganas de orinar. Requiere examen general de orina y antibiótico recetado por médico."
        },
        {
            "nombre": "Conjuntivitis / Infección ocular",
            "keywords": ["ojos rojos", "lagañas", "ardor en los ojos", "picazón en los ojos", "sensación de arenilla", "ojo inflamado"],
            "tratamiento": "Lavar los ojos con suero fisiológico, evitar frotarse, usar compresas frías y no compartir toallas ni fundas de almohada."
        },
        {
            "nombre": "Ansiedad / Ataque de pánico",
            "keywords": ["taquicardia", "falta de aire", "nerviosismo", "palpitaciones", "opresión en el pecho", "miedo", "angustia", "desesperación", "náuseas por nervios"],
            "tratamiento": "Técnicas de respiración profunda (inhalar en 4s, retener, exhalar en 8s). Buscar un ambiente tranquilo. Buscar ayuda psicológica."
        },
        {
            "nombre": "Problemas de Presión Arterial (Hipertensión/Hipotensión)",
            "keywords": ["zumbido de oídos", "dolor de nuca", "luces en la vista", "lucecitas", "presión", "vértigo", "mareo", "dolor de cabeza"],
            "tratamiento": "Medir la presión arterial inmediatamente. Si es alta, tomar medicamento si está prescrito o ir a urgencias. Si es baja, elevar piernas y tomar líquidos."
        },
        {
            "nombre": "Otitis / Infección del oído",
            "keywords": ["dolor de oído", "oído tapado", "punzadas", "zumbido", "supuración", "secreción", "dolor de cabeza"],
            "tratamiento": "Mantener el oído seco, no introducir cotonetes. Tomar analgésico para el dolor. Requiere revisión médica (otoscopia) para recetar antibiótico si hay infección."
        },
        {
            "nombre": "Anemia / Deficiencia de hierro o Hipoglucemia (Bajón de azúcar)",
            "keywords": ["palidez", "mucho sueño", "debilidad extrema", "fatiga crónica", "cansancio extremo", "temblor", "sudor frío", "mareo", "náuseas"],
            "tratamiento": "Si es hipoglucemia aguda: consumir algo dulce inmediatamente (jugo, dulce). Si es anemia crónica: Aumentar consumo de hierro (carnes rojas, espinacas) y hacer análisis de sangre."
        },
        {
            "nombre": "Asma / Problema bronquial",
            "keywords": ["sibilancias", "silbido al respirar", "pecho apretado", "tos", "me ahogo", "dificultad para respirar"],
            "tratamiento": "Uso de inhalador de rescate si está diagnosticado. Evitar humo, polvo y frío. Si la dificultad persiste y falta el oxígeno, acudir a urgencias de inmediato."
        },
        {
            "nombre": "Dolor dental / Infección bucal",
            "keywords": ["dolor de muela", "dolor de dientes", "encía inflamada", "sangrado de encías", "sensibilidad dental", "caries", "dolor de cabeza por muela"],
            "tratamiento": "Higiene dental suave, enjuagues de agua tibia con sal, analgésico para el dolor y agendar cita urgente con el odontólogo."
        },
        {
            "nombre": "Problemas de sueño / Insomnio",
            "keywords": ["no puedo dormir", "desvelo", "insomnio", "me despierto mucho", "sueño ligero", "dificultad para dormir", "cansancio", "dolor de cabeza"],
            "tratamiento": "Evitar pantallas antes de dormir y cafeína por la tarde. Mantener un horario fijo, cenar ligero y probar con tés relajantes (valeriana, manzanilla)."
        },
        {
            "nombre": "Amigdalitis / Infección de garganta",
            "keywords": ["dolor de garganta", "garganta inflamada", "dificultad para tragar", "placas blancas", "ganglios inflamados", "fiebre", "dolor al tragar"],
            "tratamiento": "Hacer gárgaras con agua tibia y sal. Mantenerse hidratado y tomar alimentos blandos. Requiere revisión médica para determinar si es bacteriana y necesita antibiótico."
        },
        {
            "nombre": "Esguince / Lesión Muscular",
            "keywords": ["dolor articular", "hinchazón", "torcedura", "no puedo mover el pie", "moratón", "hematoma", "dolor al apoyar", "esguince"],
            "tratamiento": "Método RICE: Reposo, Hielo (Ice), Compresión y Elevación. No masajear la zona afectada. Si el dolor es insoportable, realizar radiografía."
        },
        {
            "nombre": "Cálculos Renales (Piedras en el riñón)",
            "keywords": ["dolor de espalda fuerte", "dolor de riñón", "dolor en el costado", "sangre en la orina", "náuseas", "dolor que baja a la ingle"],
            "tratamiento": "Aumentar drásticamente la ingesta de agua. Tomar analgésicos. Si el dolor es incapacitante o hay fiebre, acudir a urgencias inmediatamente."
        },
        {
            "nombre": "Dermatitis / Alergia en la piel",
            "keywords": ["picazón", "ronchas", "piel roja", "erupción", "eccema", "granitos", "picor"],
            "tratamiento": "Evitar rascarse. Aplicar compresas frías o cremas hidratantes sin perfume. Si hay inflamación severa, puede requerir cremas con corticoides bajo receta."
        },
        # ─── NUEVAS CONDICIONES ────────────────────────────────────────────────────
        {
            "nombre": "Diabetes (Sospecha / Descompensación)",
            "keywords": ["mucha sed", "orinar mucho", "vista borrosa", "heridas que no sanan", "hormigueo en pies", "cansancio extremo", "bajón de azúcar", "glucosa alta", "azúcar alta"],
            "tratamiento": "Medir glucosa en sangre de inmediato. Hidratarse bien con agua natural. Evitar azúcares simples. Acudir al médico para ajuste de medicamento o insulina. Si hay confusión o pérdida de conciencia, llamar a emergencias."
        },
        {
            "nombre": "Infarto al Miocardio (EMERGENCIA CARDÍACA)",
            "keywords": ["dolor en el pecho", "presión en el pecho", "dolor que irradia al brazo", "dolor en el brazo izquierdo", "sudor frío", "falta de aire", "náuseas", "mandíbula", "sensación de muerte"],
            "tratamiento": "EMERGENCIA: Llamar al número de emergencias (911) de inmediato. Sentar o recostar al paciente. Si está indicado, dar aspirina 325 mg. NO conducir solo. Cada minuto es crítico."
        },
        {
            "nombre": "Depresión / Trastorno depresivo mayor",
            "keywords": ["tristeza profunda", "no tengo ganas de nada", "me siento vacío", "no quiero levantarme", "lloro sin razón", "sin motivación", "pérdida de apetito", "pensamientos negativos", "me siento solo", "no me importa nada"],
            "tratamiento": "Buscar apoyo psicológico o psiquiátrico de forma urgente. No aislarse. Hablar con alguien de confianza. Mantener rutinas básicas (comer, dormir, salir). Evitar el alcohol. Si hay pensamientos de hacerse daño, acudir a urgencias inmediatamente."
        },
        {
            "nombre": "Sinusitis / Congestión paranasal",
            "keywords": ["congestión nasal", "dolor en la cara", "presión en la frente", "mocos verdes", "mocos amarillos", "goteo nasal", "pérdida del olfato", "dolor al inclinar la cabeza", "cara hinchada"],
            "tratamiento": "Vaporizaciones con agua caliente, lavados nasales con solución salina. Descanso y abundantes líquidos. Si los síntomas duran más de 10 días o hay fiebre alta, consultar al médico para descartar infección bacteriana y recetar antibiótico."
        },
        {
            "nombre": "Gastroenteritis viral (Estómago revuelto fuerte)",
            "keywords": ["diarrea fuerte", "vómito y diarrea", "calambres intestinales", "retortijones", "estómago revuelto", "descompostura", "fiebre leve", "deshidratación"],
            "tratamiento": "Reposo intestinal: comenzar con solo agua y suero oral. Dieta blanda progresiva (arroz, plátano, pan tostado). Evitar lácteos, grasas y picantes. Si la diarrea dura más de 3 días o hay sangre, acudir al médico."
        },
        {
            "nombre": "Hepatitis / Ictericia (Problema hepático)",
            "keywords": ["piel amarilla", "ojos amarillos", "ictericia", "hígado", "orina oscura", "cansancio extremo", "náuseas", "pérdida de apetito", "dolor lado derecho del abdomen"],
            "tratamiento": "URGENTE: Acudir al médico para análisis de sangre (función hepática). Evitar completamente el alcohol. Dieta baja en grasas. El tratamiento varía según la causa (viral, alcohólica, tóxica). No auto-medicarse."
        },
        {
            "nombre": "Insuficiencia renal (Problemas de riñón crónicos)",
            "keywords": ["hinchazón en piernas", "piernas hinchadas", "cara hinchada", "poco orín", "no orino", "cansancio extremo", "náuseas sin causa", "calambres", "piel pálida y seca", "falta de aire al estar acostado"],
            "tratamiento": "URGENTE: Acudir al médico para análisis de función renal. Reducir ingesta de sal, potasio y líquidos según indicación. Controlar presión arterial y glucosa. Si hay paro urinario total, ir a urgencias de inmediato."
        },
        {
            "nombre": "Hipotiroidismo (Tiroides lenta)",
            "keywords": ["mucho frío", "siempre tengo frío", "cabello se me cae", "uñas frágiles", "piel seca", "cansancio todo el día", "aumento de peso sin comer más", "estreñimiento crónico", "lentitud mental", "depresión"],
            "tratamiento": "Consultar al endocrinólogo para análisis de TSH, T3 y T4. El tratamiento es con levotiroxina (hormona tiroidea sintética). Con tratamiento adecuado los síntomas mejoran notablemente. Revisiones periódicas obligatorias."
        },
        {
            "nombre": "Hipertiroidismo (Tiroides acelerada)",
            "keywords": ["nerviosismo extremo", "palpitaciones", "temblor en las manos", "sudoración excesiva", "pérdida de peso sin dieta", "dificultad para dormir", "calor excesivo", "ojos saltones", "diarrea"],
            "tratamiento": "Consultar al endocrinólogo para análisis de función tiroidea. Evitar el estrés y el exceso de cafeína. El tratamiento puede incluir medicamentos antitiroideos, yodo radioactivo o cirugía, según valoración médica."
        },
        {
            "nombre": "Hernia (Inguinal, Umbilical o Hiatal)",
            "keywords": ["bulto en la ingle", "bulto en el ombligo", "protuberancia", "hernia", "dolor al pujar", "acidez intensa", "reflujo severo", "dolor al levantar peso", "bulto que desaparece al acostarse"],
            "tratamiento": "Evitar cargar pesos pesados y esfuerzos bruscos. Si el bulto se vuelve duro, no reduce y hay dolor intenso, es una emergencia quirúrgica. La hernia hiatal requiere tratamiento de reflujo y valoración por gastroenterólogo."
        },
        {
            "nombre": "Gota / Artritis gotosa",
            "keywords": ["dolor en el dedo gordo del pie", "dedo gordo inflamado", "articulación roja e inflamada", "gota", "ácido úrico alto", "dolor intenso al caminar", "rodilla inflamada sin golpe"],
            "tratamiento": "Reposo de la articulación afectada y aplicar hielo. Tomar analgésico/antiinflamatorio (ibuprofeno si no hay contraindicación). Aumentar ingesta de agua. Evitar carnes rojas, mariscos, alcohol y bebidas azucaradas. Consultar médico para controlar el ácido úrico."
        },
        {
            "nombre": "Neumonía / Bronquitis severa",
            "keywords": ["tos con flema", "tos con sangre", "fiebre alta", "dificultad para respirar", "dolor al respirar", "escalofríos", "silbido al respirar", "flema verde o amarilla", "pecho cargado"],
            "tratamiento": "URGENTE: Acudir al médico para radiografía de tórax. Requiere antibióticos específicos recetados por médico. Reposo absoluto, mucho líquido y antitérmicos para la fiebre. Si hay falta de oxígeno o labios azules, llamar emergencias."
        },
        {
            "nombre": "Úlcera péptica / Úlcera gástrica",
            "keywords": ["ardor estomacal intenso", "dolor en el estómago que mejora al comer", "dolor en el estómago en ayunas", "náuseas después de comer", "heces negras", "vómito con sangre", "reflujo constante"],
            "tratamiento": "Evitar aspirina, ibuprofeno, alcohol, café y comidas picantes. Tomar el medicamento antiácido o inhibidor de bomba de protones recetado. Si hay heces negras o vómito con sangre, es una emergencia médica."
        },
        {
            "nombre": "Colitis / Intestino irritable",
            "keywords": ["diarrea crónica", "estreñimiento y diarrea alternados", "cólicos frecuentes", "mucosidad en las heces", "distensión abdominal", "gases frecuentes", "dolor al ir al baño", "urgencia de ir al baño"],
            "tratamiento": "Llevar un diario de alimentos para identificar los desencadenantes. Dieta rica en fibra progresiva. Evitar el estrés. Tomar probióticos. Consultar al gastroenterólogo para descartar enfermedades inflamatorias más serias (Crohn, colitis ulcerosa)."
        },
        {
            "nombre": "Fibromialgia / Dolor crónico generalizado",
            "keywords": ["dolor en todo el cuerpo", "puntos de dolor", "cansancio crónico", "no descansé aunque dormí", "rigidez matutina", "sensibilidad al tacto", "niebla mental", "olvidos frecuentes", "dolor muscular generalizado"],
            "tratamiento": "Ejercicio suave y regular (caminata, natación). Técnicas de relajación y manejo del estrés. Terapia cognitivo-conductual. El médico puede recetar medicamentos específicos (duloxetina, pregabalina). Evitar el sedentarismo."
        },
        {
            "nombre": "Bronquitis aguda (Tos persistente)",
            "keywords": ["tos que no cede", "tos por semanas", "tos con moco", "carraspera", "garganta irritada", "pecho cargado", "voz ronca"],
            "tratamiento": "Mucha hidratación y vapor. Miel con limón para aliviar la tos. Evitar humo y ambientes con polvo. Los antibióticos generalmente no son necesarios si es viral. Si dura más de 3 semanas o hay fiebre alta, consultar al médico."
        },
        {
            "nombre": "Torcedura de cuello / Cervicalgia",
            "keywords": ["no puedo girar el cuello", "cuello tieso", "dolor al mover la cabeza", "tortícolis", "dolor en el cuello y hombros", "cuello agarrotado", "me dormí chueco"],
            "tratamiento": "Aplicar calor local (toalla caliente) 15-20 minutos. Masajes suaves circulares en la zona. Analgésicos de venta libre si el dolor es intenso. Evitar movimientos bruscos. Realizar estiramientos cervicales suaves. Si el dolor se irradia al brazo o hay entumecimiento, consultar médico."
        },
        {
            "nombre": "Hemorroides / Fisura anal",
            "keywords": ["dolor al ir al baño", "sangre en el papel", "sangrado al defecar", "comezón en el ano", "bulto en el ano", "ardor al defecar", "hemorroides"],
            "tratamiento": "Aumentar fibra en la dieta (frutas, verduras, cereales) y beber mucha agua. Evitar estar sentado por periodos muy largos. Baños de asiento con agua tibia. Cremas tópicas de venta libre. Si el sangrado es abundante o persistente, consultar al médico."
        },
        {
            "nombre": "Trastorno de estrés postraumático / Estrés crónico",
            "keywords": ["pesadillas recurrentes", "recuerdos intrusivos", "flashbacks", "evitar ciertos lugares", "sobresaltos frecuentes", "nerviosismo constante", "irritabilidad sin causa", "estrés crónico", "agotamiento emocional"],
            "tratamiento": "Buscar apoyo psicológico especializado (terapia EMDR o cognitivo-conductual). Técnicas de mindfulness y relajación. Mantener rutinas diarias estables. No automedicarse. Apoyarse en redes sociales de confianza. Evitar el aislamiento."
        },
        {
            "nombre": "Pie diabético / Neuropatía periférica",
            "keywords": ["hormigueo en los pies", "entumecimiento en pies y manos", "quemación en los pies", "pies fríos sin razón", "heridas en los pies que no sanan", "callos que no duelen", "pérdida de sensibilidad"],
            "tratamiento": "Revisar los pies diariamente en busca de lesiones. Usar calcetines de algodón y zapatos cómodos. Nunca andar descalzo. Control estricto de glucosa. Acudir al médico para valoración neurológica. Heridas abiertas requieren atención médica urgente."
        },
        {
            "nombre": "Glaucoma / Presión ocular elevada",
            "keywords": ["visión borrosa en los bordes", "pérdida de visión lateral", "halos alrededor de las luces", "dolor ocular intenso", "ojo rojo con náuseas", "visión en túnel", "presión en el ojo"],
            "tratamiento": "URGENTE si hay dolor intenso y pérdida brusca de visión: acudir a urgencias oftalmológicas. El glaucoma agudo puede causar ceguera en horas. El tratamiento incluye gotas oculares para bajar la presión y, en casos severos, cirugía."
        },
        {
            "nombre": "Reflujo gastroesofágico (ERGE)",
            "keywords": ["acidez frecuente", "regurgitación", "sabor ácido en la boca", "ardor que sube a la garganta", "tos nocturna", "ronquera matutina", "dolor en el pecho al comer", "reflujo"],
            "tratamiento": "Evitar comidas grasosas, chocolate, café, alcohol y comidas copiosas. No acostarse hasta 2-3 horas después de comer. Elevar la cabecera de la cama. El médico puede recetar inhibidores de bomba de protones (omeprazol). Perder peso si hay sobrepeso."
        },
        {
            "nombre": "Pancreatitis (Inflamación del páncreas)",
            "keywords": ["dolor muy fuerte en la barra del estómago", "dolor que va hacia la espalda", "náuseas y vómito intensos", "abdomen muy sensible al tacto", "dolor después de comer grasas", "ictericia leve"],
            "tratamiento": "EMERGENCIA MÉDICA: Acudir a urgencias inmediatamente. Requiere hospitalización, ayuno y líquidos intravenosos. NO auto-medicarse ni comer. Evitar el alcohol de manera permanente si es la causa."
        },
        {
            "nombre": "Acidez / Pirosis leve",
            "keywords": ["ardor en el pecho", "agruras", "acidez después de comer", "sabor amargo", "indigestión", "estómago lleno", "pesadez después de comer"],
            "tratamiento": "Tomar antiácidos de venta libre (bicarbonato, omeprazol). Evitar comidas picantes, grasosas, café y alcohol. Comer porciones pequeñas y frecuentes. No acostarse inmediatamente después de comer."
        },
        {
            "nombre": "Síncope / Desmayo (Pérdida de conciencia)",
            "keywords": ["me voy a desmayar", "visión en negro", "casi me caigo", "me desmayé", "pérdida de conciencia", "me quedé en blanco", "mareo súbito al pararme", "debilidad repentina"],
            "tratamiento": "Acostarse con las piernas elevadas hasta recuperarse. Hidratarse lentamente. Evitar levantarse bruscamente. Si el desmayo fue sin causa aparente, dura más de un minuto o se repite, acudir al médico para descartar causa cardíaca o neurológica."
        },
        {
            "nombre": "Sarampión / Varicela / Rubeola (Enfermedades exantemáticas)",
            "keywords": ["manchas rojas en la piel", "sarpullido con fiebre", "granos con líquido", "ampollas", "varicela", "manchas que empiezan en la cara", "ganglios en el cuello", "comezón generalizada con fiebre"],
            "tratamiento": "Aislamiento para evitar contagio. Reposo y mucho líquido. Antipruríticos (loción de calamina) para el picor. Antitérmicos para la fiebre. Cortar uñas cortas para evitar rascado y cicatrices. Consultar al médico, especialmente en adultos o embarazadas."
        },
        {
            "nombre": "Conjuntivitis alérgica / Ojo seco",
            "keywords": ["ojos llorosos todo el tiempo", "ardor en los ojos", "ojos resecos", "sensación de cuerpo extraño en el ojo", "ojo irritado sin lagañas", "picazón en los ojos", "visión borrosa que mejora al parpadear"],
            "tratamiento": "Lubricantes oculares (lágrimas artificiales) sin conservadores. Evitar el alérgeno causante. Antihistamínicos orales o colirios antihistamínicos. Compresas frías. Evitar lentes de contacto durante el episodio agudo."
        },
        {
            "nombre": "Contractura muscular / Calambre severo",
            "keywords": ["músculo agarrotado", "calambre", "espasmo muscular", "músculo duro como piedra", "dolor repentino en la pantorrilla", "músculo que se contrae solo", "contractura", "tirón muscular"],
            "tratamiento": "Estiramiento suave y sostenido del músculo afectado. Aplicar calor local (si es contractura) o hielo (si es por golpe). Masaje suave en la zona. Hidratarse bien. Si los calambres son frecuentes, puede ser deficiencia de magnesio o potasio, consultar al médico."
        },
        {
            "nombre": "Psoriasis / Dermatitis seborreica",
            "keywords": ["placas en la piel", "escamas en la piel", "piel engrosada y roja", "caspa severa", "descamación en cuero cabelludo", "piel plateada", "picor crónico", "codos y rodillas con parches"],
            "tratamiento": "Uso de cremas hidratantes sin fragancia constantemente. Champú medicado para cuero cabelludo. Evitar rascado y jabones agresivos. El dermatólogo puede recetar corticosteroides tópicos o tratamientos biológicos en casos severos. Evitar el estrés que puede desencadenar brotes."
        },
        {
            "nombre": "Arritmia / Taquicardia",
            "keywords": ["corazón acelerado", "palpitaciones fuertes", "latidos irregulares", "corazón que se salta un latido", "mareo con palpitaciones", "falta de aire con palpitaciones", "sensación de aleteo en el pecho"],
            "tratamiento": "Si es primer episodio o prolongado: acudir al médico. Maniobra de Valsalva: inhalar profundo, aguantar y pujar como si fuera al baño. Evitar cafeína, alcohol, tabaco y estrés. Electrocardiograma necesario para diagnóstico exacto. Si hay desmayo o dolor en pecho, es emergencia."
        },
        {
            "nombre": "Quemadura solar / Golpe de calor",
            "keywords": ["piel roja por el sol", "quemadura de sol", "ampollas por el sol", "piel que pela", "golpe de calor", "temperatura muy alta del cuerpo", "confusión por calor", "deshidratación por calor"],
            "tratamiento": "Para quemadura solar: aplicar aloe vera o crema hidratante fría, evitar el sol, tomar mucha agua. Para golpe de calor: pasar a la sombra inmediatamente, mojar con agua fría, aplicar compresas en cuello y axilas. Si hay confusión o pérdida de conciencia, llamar emergencias."
        }
    ]

    coincidencias = []
    for condicion in condiciones:
        # Cuenta cuántas palabras clave DISTINTAS coinciden
        puntaje = sum(1 for k in condicion["keywords"] if k in texto)
        if puntaje > 0:
            coincidencias.append((puntaje, condicion))

    if coincidencias:
        # Ordenamos los padecimientos de mayor a menor coincidencias
        coincidencias.sort(key=lambda x: x[0], reverse=True)
        mejor = coincidencias[0][1]
        
        # Lógica de diagnósticos combinados: Si los 2 primeros tienen un puntaje similar (ej. síntomas mezclados)
        if len(coincidencias) > 1 and coincidencias[1][0] >= coincidencias[0][0] - 1 and coincidencias[1][0] > 1:
            segundo = coincidencias[1][1]
            return (
                f"{mejor['nombre']} o {segundo['nombre']}",
                f"SÍNTOMAS COMBINADOS DETECTADOS.\n\n"
                f"Opción 1 ({mejor['nombre']}):\n{mejor['tratamiento']}\n\n"
                f"Opción 2 ({segundo['nombre']}):\n{segundo['tratamiento']}"
            )
        
        return (
            f"{mejor['nombre']}",
            f"{mejor['tratamiento']}"
        )

    return (
        "Malestar no específico o cuadro complejo",
        "No logramos identificar tu padecimiento con exactitud. Sugerimos descanso, hidratación y seguimiento médico si los síntomas persisten o empeoran."
    )


def mostrar_resultado_diagnostico(sintomas, id_paciente, fecha, parent_window=None):
    titulo, tratamiento = obtener_diagnostico_por_sintomas(sintomas)
    
    # Extraemos la primera parte del diagnóstico para la gráfica
    diag_principal = titulo.split(' o ')[0].split(' / ')[0].strip()
    
    # Generamos un ID de consulta único simulado para pasar al objeto Consulta
    id_consulta = "CONS-" + datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Instanciamos la clase Consulta del backend usando backenP de manera explícita para evitar la colisión
    import backenP
    consulta_obj = backenP.Consulta(id_paciente, id_consulta, fecha, sintomas.strip(), diag_principal, tratamiento)
    receta_texto = consulta_obj.genera_receta()
    
    resultado = tk.Toplevel()
    resultado.title("Diagnóstico Médico Inteligente")
    resultado.geometry("800x600")
    resultado.configure(bg="#F0F4F8") # Fondo azul muy suave
    resultado.resizable(False, False)

    # Header elegante
    header = tk.Frame(resultado, bg="#2C3E50", height=100)
    header.pack(fill="x")
    tk.Label(header, text="ANÁLISIS MÉDICO COMPLETADO", font=("Segoe UI", 22, "bold"), fg="white", bg="#2C3E50").pack(pady=25)

    # Contenedor principal estilo tarjeta (Card)
    card_frame = tk.Frame(resultado, bg="white", bd=0, relief="flat", highlightbackground="#D5DBDB", highlightthickness=2)
    card_frame.pack(fill="both", expand=True, padx=40, pady=30)

    # Título del diagnóstico
    tk.Label(card_frame, text="Posible Diagnóstico:", font=("Segoe UI", 12, "bold"), fg="#7F8C8D", bg="white").pack(anchor="w", padx=30, pady=(25, 0))
    tk.Label(card_frame, text=titulo, font=("Century Gothic", 20, "bold"), fg="#E74C3C", bg="white", wraplength=650, justify="left").pack(anchor="w", padx=30, pady=(5, 15))

    # Línea separadora
    separator = tk.Frame(card_frame, bg="#EAEDED", height=2)
    separator.pack(fill="x", padx=30, pady=5)

    # Tratamiento sugerido
    tk.Label(card_frame, text="Tratamiento y Recomendaciones:", font=("Segoe UI", 12, "bold"), fg="#7F8C8D", bg="white").pack(anchor="w", padx=30, pady=(15, 0))
    tk.Label(card_frame, text=tratamiento, font=("Segoe UI", 14), fg="#34495E", bg="white", wraplength=650, justify="left").pack(anchor="w", padx=30, pady=(5, 20))

    # Pie de la tarjeta (Disclaimer)
    tk.Label(card_frame, text="Esta es una aplicación web, puede tener ciertos errores.",
             font=("Segoe UI", 10, "italic"), fg="#E67E22", bg="white", wraplength=650, justify="left").pack(anchor="w", padx=30, pady=(10, 20))

    # Contenedor de botones
    frame_botones = tk.Frame(resultado, bg="#F0F4F8")
    frame_botones.pack(pady=(0, 20))

    def guardar_pdf():
        archivo = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf"), ("Archivo de Texto", "*.txt"), ("Todos", "*.*")],
            initialfile=f"Receta_{id_paciente}_{datetime.now().strftime('%d%m%Y_%H%M%S')}"
        )
        if archivo:
            try:
                try:
                    from fpdf import FPDF
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Courier", size=10)
                    for linea in receta_texto.split('\n'):
                        linea_clean = linea.encode('latin-1', 'replace').decode('latin-1')
                        pdf.cell(0, 6, text=linea_clean, ln=1)
                    pdf.output(archivo)
                except ImportError:
                    # Si no tiene fpdf, lo guardamos como texto simulando pdf
                    with open(archivo, 'w', encoding='utf-8') as f:
                        f.write(receta_texto)
                from tkinter import messagebox
                messagebox.showinfo("Éxito", f"Receta guardada en:\n{archivo}")
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", f"No se pudo guardar la receta:\n{str(e)}")

    def finalizar_consulta():
        resultado.destroy()
        if parent_window:
            parent_window.destroy()
        mostrar_ventana_inicial()

    btn_guardar = tk.Button(frame_botones, text="GUARDAR COMO PDF", command=guardar_pdf,
              font=("Segoe UI", 11, "bold"), fg="white", bg="#27AE60", activebackground="#1E8449", activeforeground="white",
              bd=0, padx=20, pady=10, cursor="hand2")
    btn_guardar.pack(side="left", padx=10)

    btn_finalizar = tk.Button(frame_botones, text="FINALIZAR CONSULTA", command=finalizar_consulta,
              font=("Segoe UI", 11, "bold"), fg="white", bg="#E74C3C", activebackground="#C0392B", activeforeground="white",
              bd=0, padx=20, pady=10, cursor="hand2")
    btn_finalizar.pack(side="left", padx=10)

    btn_cerrar = tk.Button(frame_botones, text="CERRAR VENTANA", command=resultado.destroy,
              font=("Segoe UI", 11, "bold"), fg="white", bg="#2980B9", activebackground="#1A5276", activeforeground="white",
              bd=0, padx=20, pady=10, cursor="hand2")
    btn_cerrar.pack(side="left", padx=10)


def destruir_ventana(ventana_actual):
    ventana_actual.destroy()

def guardar_consulta_excel(id_paciente, fecha, sintomas, etiqueta_info):
    if not sintomas.strip() or sintomas.strip() == "(Describa síntomas aquí...)":
        etiqueta_info.config(text="Por favor ingresa los síntomas antes de guardar.", fg="red")
        return

    diagnostico, tratamiento = obtener_diagnostico_por_sintomas(sintomas)
    # Extraemos solo la primera parte del diagnóstico para la gráfica
    diag_principal = diagnostico.split(' o ')[0].split(' / ')[0].strip()

    archivo_consultas = "D:/Python/ConsulProgra/registro_consultas.xlsx"
    import pandas as pd
    import os
    
    nuevos_datos = {
        "ID": [id_paciente],
        "Fecha": [fecha],
        "Sintomas": [sintomas.strip()],
        "Diagnostico": [diag_principal]
    }
    df_nuevo = pd.DataFrame(nuevos_datos)
    
    if os.path.exists(archivo_consultas):
        try:
            df_existente = pd.read_excel(archivo_consultas)
            df_resultante = pd.concat([df_existente, df_nuevo], ignore_index=True)
            df_resultante.to_excel(archivo_consultas, index=False)
            etiqueta_info.config(text="Consulta guardada exitosamente en el registro.", fg="#27AE60")
        except Exception as e:
            etiqueta_info.config(text=f"Error al guardar: {e}", fg="red")
    else:
        try:
            df_nuevo.to_excel(archivo_consultas, index=False)
            etiqueta_info.config(text="Archivo de consultas creado y guardado.", fg="#27AE60")
        except Exception as e:
            etiqueta_info.config(text=f"Error al crear archivo: {e}", fg="red")


def Consulta(ventana_aviso):
    ventana_aviso.destroy()
    v4 = tk.Tk()
    v4.title("Registro de Consulta")
    v4.state('zoomed')
    v4.configure(bg="#F4F7F6")

    # Título principal directamente en la ventana
    titulo = tk.Label(v4, text="FORMULARIO DE REGISTRO DE CONSULTA MÉDICA", 
                      font=("Century Gothic", 25, "bold"), fg="#2C3E50", bg="#F4F7F6")
    titulo.pack(pady=30)

    # --- CAMPOS DE ENTRADA ---
    # id_paciente
    tk.Label(v4, text="id_paciente:", font=("Arial", 14, "bold"), bg="#F4F7F6").pack()
    e2 = tk.Entry(v4, width=40, font=("Arial", 12), bg="#C6C9CB")
    e2.pack(pady=5)
    e2.insert(0, "XXXXXXX")

    # fecha
    tk.Label(v4, text="fecha:", font=("Arial", 14, "bold"), bg="#F4F7F6").pack()
    e3 = tk.Entry(v4, width=40, font=("Arial", 12), bg="#C6C9CB")
    e3.pack(pady=5)
    from datetime import datetime
    e3.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M")) # Fecha actual automática

    # sintomas
    tk.Label(v4, text="síntomas:", font=("Arial", 14, "bold"), bg="#F4F7F6").pack()
    t1 = tk.Text(v4, width=60, height=8, font=("Arial", 12), bg="#C6C9CB")
    t1.pack(pady=10)
    t1.insert("1.0", "(Describa síntomas aquí...)")

    botones_consulta = tk.Frame(v4, bg="#F4F7F6")
    botones_consulta.pack(pady=20)

    etiqueta_info = tk.Label(v4, text="Escribe tu molestia en el campo de síntomas y presiona DIAGNÓSTICO.",
                              font=("Arial", 12, "italic"), fg="#2C3E50", bg="#F4F7F6")
    etiqueta_info.pack(pady=(0, 10))

    btn_regresar = tk.Button(botones_consulta, text="← REGRESAR", font=("Segoe UI", 14, "bold"),
                    fg="white", bg="#E74C3C", padx=30, pady=10, bd=0, cursor="hand2",
                    command=lambda: funciPacientes(v4))
    btn_regresar.pack(side="left", padx=10)

    btn_guardar = tk.Button(botones_consulta, text="GUARDAR CONSULTA", font=("Segoe UI", 14, "bold"),
                    fg="white", bg="#636668", padx=40, pady=10, bd=0, cursor="hand2",
                    command=lambda: guardar_consulta_excel(e2.get(), e3.get(), t1.get("1.0", "end"), etiqueta_info))
    btn_guardar.pack(side="left", padx=10)

    btn_diagnostico = tk.Button(botones_consulta, text="DIAGNÓSTICO", font=("Segoe UI", 14, "bold"),
                    fg="white", bg="#2E86C1", padx=40, pady=10, bd=0,
                    command=lambda: mostrar_resultado_diagnostico(t1.get("1.0", "end"), e2.get(), e3.get(), v4), cursor="hand2")
    btn_diagnostico.pack(side="left", padx=10)

    v4.mainloop()



def transicionConsulta(ventana_a_cerrar):
    try:
        if ventana_a_cerrar is not None and ventana_a_cerrar.winfo_exists():
            ventana_a_cerrar.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass
    aviso = tk.Tk()
    aviso.title("Iniciando...")
    estilo_ventana(aviso, ancho=480, alto=180)
    aviso.overrideredirect(True)
    tk.Frame(aviso, bg=C_TEAL, height=4).pack(fill="x")
    tk.Label(aviso, text="📋  Iniciando consulta médica...",
             fg=C_TEXT_DARK, bg=C_BG_LIGHT,
             font=("Century Gothic", 22, "bold")).pack(expand=True)
    tk.Label(aviso, text="Preparando formulario de síntomas",
             fg=C_TEXT_MED, bg=C_BG_LIGHT, font=FONT_SMALL).pack(pady=(0, 10))
    aviso.after(1800, lambda: Consulta(aviso))
    aviso.mainloop()


def validar_admin(username_entry, password_entry, ventana_admin):
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if validar_admin_db(username, password):
        transicion_admin_exito(ventana_admin, username)
    else:
        # Si es incorrecta, mostramos un mensaje en rojo
        lbl_error = tk.Label(ventana_admin, text="❌ Credenciales Incorrectas", 
                             fg="red", bg="#F4F7F6", font=("Arial", 12, "bold"))
        lbl_error.pack(pady=10)
        # El mensaje se borra después de 2 segundos para no amontonarse
        ventana_admin.after(2000, lbl_error.destroy)

def transicion_admin_exito(ventana_a_cerrar, username):
    try:
        if ventana_a_cerrar is not None and ventana_a_cerrar.winfo_exists():
            ventana_a_cerrar.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass
    aviso = tk.Tk()
    aviso.title("Acceso Concedido")
    estilo_ventana(aviso, ancho=460, alto=180)
    aviso.overrideredirect(True)
    tk.Frame(aviso, bg=C_GREEN, height=4).pack(fill="x")
    tk.Label(aviso, text="✔  ACCESO CONCEDIDO",
             fg=C_GREEN, bg=C_BG_LIGHT,
             font=("Century Gothic", 24, "bold")).pack(expand=True)
    tk.Label(aviso, text=f"Bienvenido, {username}",
             fg=C_TEXT_MED, bg=C_BG_LIGHT, font=FONT_P).pack(pady=(0, 10))
    aviso.after(1500, lambda: ventana_dashboard_admin(aviso, username))
    aviso.mainloop()

def ven1Admin(ventana_a_cerrar):
    try:
        if ventana_a_cerrar is not None and ventana_a_cerrar.winfo_exists():
            ventana_a_cerrar.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass
    ven3 = tk.Tk()
    ven3.title("Acceso Administrador — Clínica")
    ven3.state('zoomed')
    ven3.configure(bg=C_BG_DARK)

    # Header de toda la pantalla
    tk.Frame(ven3, bg=C_TEAL, height=5).pack(fill="x")
    tk.Label(ven3, text="🏥", font=("Segoe UI", 60),
             fg=C_TEAL, bg=C_BG_DARK).pack(pady=(60, 10))
    tk.Label(ven3, text="ACCESO DE ADMINISTRADOR",
             fg=C_TEXT_WHITE, bg=C_BG_DARK,
             font=("Century Gothic", 32, "bold")).pack()
    tk.Label(ven3, text="Sistema de Gestión Interna — Personal Autorizado",
             fg=C_TEAL, bg=C_BG_DARK, font=FONT_SMALL).pack(pady=(4, 40))

    # Card de login
    card = tk.Frame(ven3, bg=C_BG_MED,
                    highlightbackground=C_TEAL, highlightthickness=1)
    card.pack(ipadx=40, ipady=30)

    tk.Label(card, text="👤  USUARIO", font=FONT_H4,
             fg=C_TEAL, bg=C_BG_MED).pack(anchor="w", padx=30, pady=(20, 4))
    entrada_usuario = tk.Entry(card, width=28, font=("Segoe UI", 16),
                               bg=C_BG_DARK, fg=C_TEXT_WHITE,
                               insertbackground=C_TEAL,
                               highlightbackground=C_TEAL, highlightthickness=1,
                               relief="flat", bd=8, justify="center")
    entrada_usuario.pack(padx=30, ipady=6)
    entrada_usuario.focus_set()

    tk.Label(card, text="🔒  CONTRASEÑA", font=FONT_H4,
             fg=C_TEAL, bg=C_BG_MED).pack(anchor="w", padx=30, pady=(16, 4))
    entrada_password = tk.Entry(card, width=28, font=("Segoe UI", 16),
                                bg=C_BG_DARK, fg=C_TEXT_WHITE,
                                insertbackground=C_TEAL,
                                highlightbackground=C_TEAL, highlightthickness=1,
                                relief="flat", bd=8, justify="center", show="*")
    entrada_password.pack(padx=30, ipady=6)
    entrada_password.bind("<Return>", lambda e: validar_admin(entrada_usuario, entrada_password, ven3))

    lbl_err = tk.Label(card, text="", bg=C_BG_MED, font=FONT_SMALL)
    lbl_err.pack(pady=8)

    def _validar():
        u = entrada_usuario.get().strip()
        p = entrada_password.get().strip()
        if validar_admin_db(u, p):
            transicion_admin_exito(ven3, u)
        else:
            lbl_err.config(text="❌ Credenciales incorrectas", fg=C_RED)
            ven3.after(2000, lambda: lbl_err.config(text=""))

    tk.Button(card, text="  INGRESAR AL SISTEMA  ",
              command=_validar,
              font=("Century Gothic", 14, "bold"),
              fg=C_BG_DARK, bg=C_TEAL,
              activeforeground=C_BG_DARK, activebackground=C_TEAL_DARK,
              bd=0, pady=12, cursor="hand2", relief="flat").pack(pady=(20, 10), padx=30, fill="x")

    boton_peligro(card, "REGRESAR",
                  lambda: [ven3.destroy(), ventana_2()],
                  ancho=28, icono="←").pack(pady=(0, 10), padx=30, fill="x")

    tk.Frame(ven3, bg=C_BG_DARK, height=1).pack(fill="x", pady=20)
    tk.Label(ven3, text="🔒  Conexión segura  —  Solo personal autorizado",
             fg=C_TEXT_MED, bg=C_BG_DARK, font=FONT_SMALL).pack()
    ven3.mainloop()

    
def funciPacientes(ventana_a_cerrar):
    try:
        if ventana_a_cerrar is not None and ventana_a_cerrar.winfo_exists():
            ventana_a_cerrar.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass
    ven3 = tk.Tk()
    ven3.title("Portal del Paciente — Clínica")
    ven3.state('zoomed')
    ven3.configure(bg=C_BG_LIGHT)

    header_frame(ven3, "PORTAL DEL PACIENTE",
                 "Selecciona la acción que deseas realizar", "👤",
                 comando_regresar=lambda: [ven3.destroy(), ventana_2()])

    centro = tk.Frame(ven3, bg=C_BG_LIGHT)
    centro.pack(expand=True)

    acciones = [
        ("📄", "OBTENER REPORTE",   "Generar reporte oficial del expediente",   generar_reporte,            C_TEAL),
        ("🩺", "INICIAR CONSULTA",  "Registrar nueva consulta médica",          lambda: transicionConsulta(ven3), C_GREEN),
        ("✏️",  "EDITAR INFORMACIÓN","Actualizar datos del expediente",          lambda: ven1Paciente(ven3),  C_GOLD),
    ]
    for icono, titulo, desc, cmd, color in acciones:
        f = tk.Frame(centro, bg=C_BG_CARD,
                     highlightbackground=color, highlightthickness=2, cursor="hand2")
        f.pack(fill="x", pady=10, padx=60)
        tk.Frame(f, bg=color, width=8).pack(side="left", fill="y")
        body = tk.Frame(f, bg=C_BG_CARD, cursor="hand2")
        body.pack(side="left", padx=20, pady=20, fill="both", expand=True)
        
        lbl_title = tk.Label(body, text=f"{icono}  {titulo}", font=FONT_H3,
                             fg=color, bg=C_BG_CARD, cursor="hand2")
        lbl_title.pack(anchor="w")
        
        lbl_desc = tk.Label(body, text=desc, font=FONT_SMALL,
                            fg=C_TEXT_MED, bg=C_BG_CARD, cursor="hand2")
        lbl_desc.pack(anchor="w")
        
        btn = tk.Button(f, text="→", font=("Segoe UI", 18, "bold"),
                        fg=color, bg=C_BG_CARD, bd=0, cursor="hand2",
                        command=lambda c=cmd: c(), activebackground=C_BG_CARD,
                        activeforeground=C_TEAL_DARK)
        btn.pack(side="right", padx=20)
        
        # Vincular el evento de clic a cada elemento de la tarjeta para que sea totalmente interactiva
        f.bind("<Button-1>", lambda e, c=cmd: c())
        body.bind("<Button-1>", lambda e, c=cmd: c())
        lbl_title.bind("<Button-1>", lambda e, c=cmd: c())
        lbl_desc.bind("<Button-1>", lambda e, c=cmd: c())

    pie = tk.Frame(ven3, bg=C_BG_DARK)
    pie.pack(fill="x", side="bottom")
    tk.Label(pie, text="🏥  Clínica Médica — Portal de Pacientes",
             font=FONT_SMALL, fg=C_TEAL, bg=C_BG_DARK).pack(pady=8)
    ven3.mainloop()

def ven1Paciente(ventana_a_cerrar):
    try:
        if ventana_a_cerrar is not None and ventana_a_cerrar.winfo_exists():
            ventana_a_cerrar.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass
    ven3 = tk.Tk()
    ven3.title("Registro de Paciente — Clínica")
    ven3.state('zoomed')
    ven3.configure(bg=C_BG_LIGHT)

    header_frame(ven3, "REGISTRO DE PACIENTE",
                 "Complete los datos del expediente médico", "📁")

    # ── Formulario en tarjeta central ─────────────────────────────
    card = tk.Frame(ven3, bg=C_BG_CARD,
                    highlightbackground=C_TEAL, highlightthickness=1)
    card.pack(padx=120, pady=15, fill="x", expand=True)

    frame_form = tk.Frame(card, bg=C_BG_CARD)
    frame_form.pack(padx=40, pady=15)

    campos = [
        ("\U0001f464  Nombre(s)",     0),
        ("\U0001f464  Apellidos",     1),
        ("\U0001f4c5  Edad",          2),
        ("\U0001f4dd  Historial Médico", 4),
    ]
    entradas = {}
    for lbl_txt, row in campos:
        tk.Label(frame_form, text=lbl_txt, font=FONT_H4,
                 fg=C_TEXT_MED, bg=C_BG_CARD).grid(
                     row=row, column=0, sticky="e", padx=(0, 16), pady=6)
        e = tk.Entry(frame_form, width=42, font=FONT_P,
                     bg=C_BG_LIGHT, fg=C_TEXT_DARK,
                     insertbackground=C_TEAL,
                     highlightbackground=C_TEAL, highlightthickness=1,
                     relief="flat", bd=6)
        e.grid(row=row, column=1, pady=6, ipady=6)
        entradas[row] = e
    entrada_nombre    = entradas[0]
    entrada_apellido  = entradas[1]
    entrada_edad      = entradas[2]
    entrada_historial = entradas[4]

    tk.Label(frame_form, text="\u2640♂️  Género", font=FONT_H4,
             fg=C_TEXT_MED, bg=C_BG_CARD).grid(row=3, column=0, sticky="e", padx=(0, 16), pady=6)
    entrada_genero = ttk.Combobox(frame_form, width=40, font=FONT_P,
                                  state="readonly",
                                  values=["Masculino", "Femenino", "Prefiero no decirlo"])
    entrada_genero.grid(row=3, column=1, pady=6, ipady=6)
    entrada_genero.set("Seleccionar género")

    # Status
    lbl_status = tk.Label(card, text="", font=FONT_P_BOLD, bg=C_BG_CARD)
    lbl_status.pack(pady=4)

    # Botones
    frame_btns = tk.Frame(card, bg=C_BG_CARD)
    frame_btns.pack(pady=(0, 15))
    boton_peligro(frame_btns, "REGRESAR",
                  lambda: [ven3.destroy(), ventana_2()],
                  ancho=12, icono="←").pack(side="left", padx=10)
    boton_exito(frame_btns, "REGISTRAR DATOS",
                lambda: guardar_datos(entrada_nombre, entrada_apellido,
                                      entrada_edad, entrada_genero,
                                      entrada_historial, lbl_status),
                ancho=20, icono="💾").pack(side="left", padx=10)
    boton_primario(frame_btns, "SIGUIENTE →",
                   lambda: funciPacientes(ven3),
                   ancho=18).pack(side="left", padx=10)

    ven3.mainloop()
def ventana_2():
    global ventanaInicial
    try:
        if ventanaInicial is not None and ventanaInicial.winfo_exists():
            ventanaInicial.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass
    ven2 = tk.Tk()
    ven2.title("Selección de Perfil — Clínica")
    ven2.state('zoomed')
    ven2.configure(bg=C_BG_DARK)

    tk.Frame(ven2, bg=C_TEAL, height=5).pack(fill="x")
    tk.Label(ven2, text="🏥", font=("Segoe UI", 70),
             fg=C_TEAL, bg=C_BG_DARK).pack(pady=(50, 6))
    tk.Label(ven2, text="¿Quién eres?",
             fg=C_TEXT_WHITE, bg=C_BG_DARK,
             font=("Century Gothic", 38, "bold")).pack()
    tk.Label(ven2, text="Selecciona tu perfil para continuar",
             fg=C_TEAL, bg=C_BG_DARK, font=FONT_P).pack(pady=(4, 50))

    frame_botones = tk.Frame(ven2, bg=C_BG_DARK)
    frame_botones.pack()

    perfiles = [
        ("🛡️", "ADMINISTRADOR",
         "Gestión interna y reportes",
         lambda: ven1Admin(ven2), C_TEAL),
        ("🩺", "PACIENTE",
         "Registro y consulta médica",
         lambda: ven1Paciente(ven2), C_GREEN),
    ]
    for icono, titulo, desc, cmd, color in perfiles:
        pf = tk.Frame(frame_botones, bg=C_BG_MED,
                      highlightbackground=color, highlightthickness=2,
                      cursor="hand2", width=340)
        pf.pack(side="left", padx=30, ipadx=20, ipady=30)
        
        lbl_icon = tk.Label(pf, text=icono, font=("Segoe UI", 46),
                            fg=color, bg=C_BG_MED, cursor="hand2")
        lbl_icon.pack(pady=(20, 6))
        
        lbl_title = tk.Label(pf, text=titulo, font=("Century Gothic", 20, "bold"),
                             fg=C_TEXT_WHITE, bg=C_BG_MED, cursor="hand2")
        lbl_title.pack()
        
        lbl_desc = tk.Label(pf, text=desc, font=FONT_SMALL,
                            fg=C_TEXT_MED, bg=C_BG_MED, cursor="hand2")
        lbl_desc.pack(pady=(2, 16))
        
        tk.Button(pf, text=f"Ingresar como {titulo.title()}",
                  command=lambda c=cmd: c(), font=FONT_P_BOLD,
                  fg=C_BG_DARK, bg=color,
                  activeforeground=C_BG_DARK, activebackground=C_TEAL_DARK,
                  bd=0, pady=10, cursor="hand2", relief="flat"
                  ).pack(fill="x", padx=20, pady=(0, 20))
                  
        # Vincular el evento de clic a toda la tarjeta y sus elementos
        pf.bind("<Button-1>", lambda e, c=cmd: c())
        lbl_icon.bind("<Button-1>", lambda e, c=cmd: c())
        lbl_title.bind("<Button-1>", lambda e, c=cmd: c())
        lbl_desc.bind("<Button-1>", lambda e, c=cmd: c())

    # Botón Regresar
    boton_peligro(ven2, "REGRESAR", lambda: [ven2.destroy(), mostrar_ventana_inicial()], ancho=18, icono="←").pack(pady=15)

    tk.Frame(ven2, bg=C_BG_DARK, height=2).pack(fill="x", pady=20)
    tk.Label(ven2, text="🔒  Clínica Médica — Sistema de Gestión Interna",
             fg=C_TEXT_MED, bg=C_BG_DARK, font=FONT_SMALL).pack()
    ven2.mainloop()



def mostrar_ventana_inicial():
    global ventanaInicial
    try:
        if ventanaInicial is not None and ventanaInicial.winfo_exists():
            ventanaInicial.destroy()
    except (NameError, AttributeError, tk.TclError):
        pass

    ventanaInicial = tk.Tk()
    ventanaInicial.title("Clínica Médica — Sistema Profesional")
    ventanaInicial.state('zoomed')
    ventanaInicial.configure(bg=C_BG_DARK)

    # Franja teal superior
    tk.Frame(ventanaInicial, bg=C_TEAL, height=5).pack(fill="x")

    # Imagen de portada
    try:
        imagen_original = Image.open("D:/Python/ConsulProgra/imagenProye.png")
        imagen_resize = imagen_original.resize((520, 260))
        imagen_final = ImageTk.PhotoImage(imagen_resize)
        lbl_img = tk.Label(ventanaInicial, image=imagen_final, bg=C_BG_DARK,
                           highlightbackground=C_TEAL, highlightthickness=3)
        lbl_img.image = imagen_final
        lbl_img.pack(pady=(50, 20))
        print("Imagen cargada con éxito")
    except Exception as e:
        print(f"Error real: {e}")
        tk.Label(ventanaInicial, text="🏥", font=("Segoe UI", 80),
                 fg=C_TEAL, bg=C_BG_DARK).pack(pady=(60, 10))

    # Título principal
    tk.Label(ventanaInicial,
             text="Consultorio y Tratamiento Online",
             fg=C_TEXT_WHITE, bg=C_BG_DARK,
             font=("Century Gothic", 38, "bold")).pack(pady=(10, 4))
    tk.Label(ventanaInicial,
             text="Diagnóstico inteligente • Gestión de pacientes • Reportes analíticos",
             fg=C_TEAL, bg=C_BG_DARK, font=FONT_P).pack(pady=(0, 40))

    # Botón de inicio
    tk.Button(
        ventanaInicial,
        text="  ▶   INICIAR SISTEMA  ",
        command=ventana_2,
        font=("Century Gothic", 16, "bold"),
        fg=C_BG_DARK, bg=C_TEAL,
        activeforeground=C_BG_DARK, activebackground=C_TEAL_DARK,
        padx=60, pady=18, bd=0, relief="flat", cursor="hand2"
    ).pack(pady=10)

    # Pie
    tk.Frame(ventanaInicial, bg=C_BG_MED, height=1).pack(fill="x", pady=30)
    tk.Label(ventanaInicial,
             text="🔒  Acceso seguro  •  Datos protegidos  •  Sistema v2.0",
             fg=C_TEXT_MED, bg=C_BG_DARK, font=FONT_SMALL).pack()

    ventanaInicial.mainloop()

# Cargar pacientes existentes del Excel al iniciar el programa
cargar_pacientes_desde_excel()

if __name__ == "__main__":
    mostrar_ventana_inicial()