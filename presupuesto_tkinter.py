import tkinter as tk
from tkinter import ttk, messagebox

# === Datos base ===
materiales = [
    "cemento", "arena", "grava", "varilla", "ladrillo", "bloque",
    "agua", "pintura", "mano de obra", "transporte",
    "supervisión", "administración", "seguridad"
]

# Mensajes de cantidad
contexto_cantidad = {
    "cemento": "¿Cuántos sacos de cemento se usarán?",
    "arena": "¿Cuántos m³ de arena se necesitan?",
    "grava": "¿Cuántos m³ de grava se utilizarán?",
    "varilla": "¿Cuántas varillas se requieren?",
    "ladrillo": "¿Cuántos ladrillos se colocarán?",
    "bloque": "¿Cuántos bloques se usarán?",
    "agua": "¿Cuántos litros de agua se necesitan?",
    "pintura": "¿Cuántos litros de pintura se aplicarán?",
    "mano de obra": "¿Cuántos días de trabajo se estiman?",
    "transporte": "¿Cuántos viajes de transporte se necesitan?",
    "supervisión": "¿Cuántos días de supervisión se requerirán?",
    "administración": "¿Cuántos días de administración se consideran?",
    "seguridad": "¿Cuántos días de servicio de seguridad se contratarán?"
}

# Mensajes de precio
contexto_precio = {
    "cemento": "Costo por saco de cemento ($):",
    "arena": "Costo por m³ de arena ($):",
    "grava": "Costo por m³ de grava ($):",
    "varilla": "Costo por varilla ($):",
    "ladrillo": "Costo por ladrillo ($):",
    "bloque": "Costo por bloque ($):",
    "agua": "Costo por litro de agua ($):",
    "pintura": "Costo por litro de pintura ($):",
    "mano de obra": "Costo por día de trabajo ($):",
    "transporte": "Costo por viaje de transporte ($):",
    "supervisión": "Costo por día de supervisión ($):",
    "administración": "Costo por día de administración ($):",
    "seguridad": "Costo por día de servicio de seguridad ($):"
}

# === Funciones de cálculo ===
def determinar_tipo(nombre):
    directos = ["cemento", "arena", "grava", "varilla", "ladrillo",
                "bloque", "agua", "pintura", "mano de obra", "transporte"]
    indirectos = ["supervisión", "administración", "seguridad"]

    if nombre.lower() in directos:
        return "Directo"
    elif nombre.lower() in indirectos:
        return "Indirecto"
    else:
        return "Directo"

def agregar_material():
    nombre = material_var.get()
    if not nombre:
        messagebox.showwarning("Aviso", "Selecciona un material.")
        return
    try:
        cantidad = float(entry_cantidad.get())
        precio = float(entry_precio.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
        return

    tipo = determinar_tipo(nombre)
    subtotal = cantidad * precio
    conceptos.append({
        "nombre": nombre.capitalize(),
        "tipo": tipo,
        "cantidad": cantidad,
        "precio_unitario": precio,
        "subtotal": subtotal
    })
    materiales.remove(nombre)
    actualizar_lista()
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    messagebox.showinfo("Agregado", f"{nombre.capitalize()} agregado como gasto {tipo}.")

def actualizar_lista():
    menu_materiales["menu"].delete(0, "end")
    for m in materiales:
        menu_materiales["menu"].add_command(label=m.capitalize(), command=tk._setit(material_var, m))
    if materiales:
        material_var.set(materiales[0])
        actualizar_contexto()
    else:
        material_var.set("")
        label_cantidad.config(text="Sin materiales restantes.")
        label_precio.config(text="")

def actualizar_contexto(*args):
    nombre = material_var.get()
    if nombre:
        label_cantidad.config(text=contexto_cantidad.get(nombre, "Cantidad:"))
        label_precio.config(text=contexto_precio.get(nombre, "Precio unitario ($):"))

def mostrar_resultado():
    if not conceptos:
        messagebox.showwarning("Aviso", "No hay materiales agregados.")
        return

    total_directo = sum(c["subtotal"] for c in conceptos if c["tipo"] == "Directo")
    total_indirecto = sum(c["subtotal"] for c in conceptos if c["tipo"] == "Indirecto")
    utilidad = (total_directo + total_indirecto) * 0.10
    total_final = total_directo + total_indirecto + utilidad

    resultado = "========== DESGLOSE ==========\n\n"
    resultado += "🔹 GASTOS DIRECTOS:\n"
    for c in conceptos:
        if c["tipo"] == "Directo":
            resultado += f" - {c['nombre']}: {c['cantidad']} x ${c['precio_unitario']:.2f} = ${c['subtotal']:.2f}\n"
    resultado += f"\nTotal Directos: ${total_directo:,.2f}\n\n"

    resultado += "🔸 GASTOS INDIRECTOS:\n"
    for c in conceptos:
        if c["tipo"] == "Indirecto":
            resultado += f" - {c['nombre']}: {c['cantidad']} x ${c['precio_unitario']:.2f} = ${c['subtotal']:.2f}\n"
    resultado += f"\nTotal Indirectos: ${total_indirecto:,.2f}\n\n"

    resultado += "========== RESUMEN ==========\n"
    resultado += f"Costos directos:   ${total_directo:,.2f}\n"
    resultado += f"Costos indirectos: ${total_indirecto:,.2f}\n"
    resultado += f"Utilidad (10%):    ${utilidad:,.2f}\n"
    resultado += f"💵 TOTAL FINAL:    ${total_final:,.2f}\n"

    text_resultado.delete(1.0, tk.END)
    text_resultado.insert(tk.END, resultado)

# === Ventana principal ===
root = tk.Tk()
root.title("Presupuesto de Obra Civil")
root.geometry("700x600")

conceptos = []

# --- Selección de material ---
tk.Label(root, text="Material:").pack(pady=5)
material_var = tk.StringVar()
material_var.trace("w", actualizar_contexto)
menu_materiales = ttk.OptionMenu(root, material_var, materiales[0], *materiales)
menu_materiales.pack()

# --- Campos dinámicos ---
label_cantidad = tk.Label(root, text="")
label_cantidad.pack(pady=5)
entry_cantidad = ttk.Entry(root)
entry_cantidad.pack(pady=5)

label_precio = tk.Label(root, text="")
label_precio.pack(pady=5)
entry_precio = ttk.Entry(root)
entry_precio.pack(pady=5)

# --- Botones ---
ttk.Button(root, text="Agregar Material", command=agregar_material).pack(pady=10)
ttk.Button(root, text="Calcular Presupuesto", command=mostrar_resultado).pack(pady=5)

# --- Resultados ---
text_resultado = tk.Text(root, width=80, height=20)
text_resultado.pack(pady=10)

actualizar_contexto()
root.mainloop()
