from mesa import Mesa
from cliente import Cliente
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox, ttk

class Restaurante:
    def __init__(self, mesas, menu):
        self.mesas = mesas
        self.menu = menu

    def mesas_disponibles(self, numero_personas):
        mesas_disponibles = []
        for mesa in self.mesas:
            if mesa.esta_disponible() and mesa.capacidad >= numero_personas:
                mesas_disponibles.append(mesa)
        return mesas_disponibles

    def atender_cliente(self, mesa, nombre_cliente, numero_personas):
        if mesa.esta_disponible():
            cliente = Cliente(nombre_cliente)
            mesa.ocupar(cliente)
            messagebox.showinfo("Mesa Asignada", f"Se ha asignado la mesa {mesa.numero} a {cliente.nombre}.")
            return cliente
        else:
            messagebox.showerror("Mesa Ocupada", f"La mesa {mesa.numero} está ocupada.")
            return None

    def mostrar_menu(self):
        menu_window = tk.Toplevel()
        menu_window.title("Menú")
        menu_window.configure(bg="#f0f0f0")

        label = tk.Label(menu_window, text="**Menú**", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        label.pack()

        # Usamos un scroll para el menú
        scrollbar = tk.Scrollbar(menu_window, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        menu_frame = tk.Frame(menu_window, bg="#f0f0f0")
        menu_frame.pack()

        # Creamos un treeview para mostrar el menú con scroll
        menu_tree = ttk.Treeview(menu_frame, yscrollcommand=scrollbar.set)
        menu_tree.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar.config(command=menu_tree.yview)

        # Configuramos las columnas
        menu_tree["columns"] = ("Precio", "Ingredientes")
        menu_tree.column("#0", width=150, minwidth=150, anchor=tk.W)
        menu_tree.column("Precio", width=100, minwidth=100, anchor=tk.CENTER)
        menu_tree.column("Ingredientes", width=400, minwidth=400, anchor=tk.W)

        # Configuramos los encabezados
        menu_tree.heading("#0", text="Plato", anchor=tk.W)
        menu_tree.heading("Precio", text="Precio", anchor=tk.CENTER)
        menu_tree.heading("Ingredientes", text="Ingredientes", anchor=tk.W)

        for plato in self.menu:
            menu_tree.insert("", tk.END, text=plato.nombre, values=(plato.precio, ', '.join(plato.ingredientes)))

    def hacer_pedido(self, mesa, cliente, pedido):
        mesa.hacer_pedido(cliente, pedido)

    def ver_pedido(self, mesa, cliente):
        mesa.mostrar_pedido(cliente)

    def finalizar(self, cliente, mesa):
        if cliente.nombre in mesa.clientes:
            incluir_propina = messagebox.askyesno("Propina", "¿Desea incluir propina?")
            self.mostrar_factura(cliente, mesa, incluir_propina)
            mesa.desocupar()
        else:
            messagebox.showinfo("Error", "No hay cliente registrado en esta mesa.")

    def mostrar_factura(self, cliente, mesa, incluir_propina):
        subtotal = mesa.calcular_total(cliente, False)
        iva = subtotal * 0.19
        propina = subtotal * 0.10 if incluir_propina else 0
        total = subtotal + iva + propina

        factura_window = tk.Toplevel()
        factura_window.title("Factura")
        factura_window.configure(bg="#f0f0f0")

        label = tk.Label(factura_window, text=f"Factura - Mesa {mesa.numero} - Cliente: {cliente.nombre}", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        label = tk.Label(factura_window, text="Pedido:", font=("Helvetica", 12), bg="#f0f0f0")
        label.pack()

        for plato in cliente.pedido:
            label = tk.Label(factura_window, text=plato.nombre + f" - ${plato.precio}", font=("Helvetica", 12), bg="#f0f0f0")
            label.pack()

        subtotal_label = tk.Label(factura_window, text="Subtotal: $" + str(subtotal), font=("Helvetica", 12), bg="#f0f0f0")
        subtotal_label.pack()

        iva_label = tk.Label(factura_window, text="IVA (19%): $" + str(iva), font=("Helvetica", 12), bg="#f0f0f0")
        iva_label.pack()

        if incluir_propina:
            propina_label = tk.Label(factura_window, text="Propina (10%): $" + str(propina), font=("Helvetica", 12), bg="#f0f0f0")
            propina_label.pack()

        total_label = tk.Label(factura_window, text="Total: $" + str(total), font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        total_label.pack()
