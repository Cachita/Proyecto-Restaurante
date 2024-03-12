import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, master, restaurante):
        self.master = master
        self.restaurante = restaurante

        self.label = tk.Label(master, text="Donde El Mono", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.label.pack()

        self.mesas_frame = tk.Frame(master, bg="#f0f0f0")
        self.mesas_frame.pack()

        self.botones_mesas = []
        row_num = 0
        col_num = 0
        for mesa in self.restaurante.mesas:
            estado = "Disponible" if mesa.esta_disponible() else "Ocupada"
            color = "#00b894" if mesa.esta_disponible() else "#ff6b6b"
            boton_mesa = tk.Button(self.mesas_frame, text=f"Mesa {mesa.numero} - {estado}", font=("Helvetica", 14), bg=color, fg="white", padx=10, pady=5, bd=0, relief=tk.RAISED, state=tk.NORMAL if mesa.esta_disponible() else tk.DISABLED)
            boton_mesa.config(command=lambda m=mesa: self.seleccionar_mesa(m))
            boton_mesa.bind("<Enter>", lambda event, button=boton_mesa: self.hover_in(button))
            boton_mesa.bind("<Leave>", lambda event, button=boton_mesa: self.hover_out(button))
            boton_mesa.grid(row=row_num, column=col_num, padx=10, pady=10)
            self.botones_mesas.append(boton_mesa)
            col_num += 1
            if col_num > 1:
                col_num = 0
                row_num += 1

    def hover_in(self, button):
        button.config(bg="#2ecc71")  # Cambiar el color al pasar el ratón

    def hover_out(self, button):
        estado = button["text"].split(" - ")[-1]
        color = "#00b894" if estado == "Disponible" else "#ff6b6b"
        button.config(bg=color)  # Restaurar el color original al salir del ratón

    def actualizar_mesas(self):
        for mesa, boton in zip(self.restaurante.mesas, self.botones_mesas):
            estado = "Disponible" if mesa.esta_disponible() else "Ocupada"
            color = "#00b894" if mesa.esta_disponible() else "#ff6b6b"
            boton.config(text=f"Mesa {mesa.numero} - {estado}", bg=color, state=tk.NORMAL if mesa.esta_disponible() else tk.DISABLED)
        self.master.after(1000, self.actualizar_mesas)

    def seleccionar_mesa(self, mesa):
        if mesa.esta_disponible():
            ventana_cliente = tk.Toplevel()
            ventana_cliente.title("Registro de Cliente")
            ventana_cliente.configure(bg="#f0f0f0")

            label_nombre = tk.Label(ventana_cliente, text="Nombre del cliente:", font=("Helvetica", 12), bg="#f0f0f0")
            label_nombre.pack()

            entry_nombre = tk.Entry(ventana_cliente, font=("Helvetica", 12))
            entry_nombre.pack()

            label_personas = tk.Label(ventana_cliente, text="Número de personas:", font=("Helvetica", 12), bg="#f0f0f0")
            label_personas.pack()

            entry_personas = tk.Entry(ventana_cliente, font=("Helvetica", 12))
            entry_personas.pack()

            button_registrar = tk.Button(ventana_cliente, text="Registrar", font=("Helvetica", 12), bg="#00b894", fg="white", padx=10, pady=5, command=lambda: self.registrar_cliente(mesa, entry_nombre.get(), entry_personas.get(), ventana_cliente))
            button_registrar.pack()
        else:
            cliente = self.restaurante.atender_cliente(mesa, "", 0)
            if cliente:
                self.mostrar_opciones_cliente(cliente, mesa)

    def registrar_cliente(self, mesa, nombre, num_personas, ventana):
        if nombre.strip() != "" and num_personas.isdigit():
            num_personas = int(num_personas)
            if num_personas <= 4:
                cliente = self.restaurante.atender_cliente(mesa, nombre, num_personas)
                if cliente:
                    ventana.destroy()
                    self.mostrar_opciones_cliente(cliente, mesa)
            else:
                messagebox.showerror("Error", "El número de personas debe ser menor a 5 por mesa.")
        else:
            messagebox.showerror("Error", "Ingrese un nombre válido y un número válido de personas.")

    def mostrar_opciones_cliente(self, cliente, mesa):
        ventana_opciones = tk.Toplevel()
        ventana_opciones.title(f"Opciones para {cliente.nombre}")
        ventana_opciones.configure(bg="#f0f0f0")

        label_bienvenida = tk.Label(ventana_opciones, text=f"Bienvenido/a {cliente.nombre} a Donde El Mono", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label_bienvenida.pack()

        button_ver_menu = tk.Button(ventana_opciones, text="Ver Menú", font=("Helvetica", 12), bg="#00b894", fg="white", padx=10, pady=5, command=lambda: self.restaurante.mostrar_menu())
        button_ver_menu.pack()

        button_hacer_pedido = tk.Button(ventana_opciones, text="Hacer Pedido", font=("Helvetica", 12), bg="#00b894", fg="white", padx=10, pady=5, command=lambda: self.hacer_pedido(cliente, mesa))
        button_hacer_pedido.pack()

        button_ver_pedido = tk.Button(ventana_opciones, text="Ver Pedido", font=("Helvetica", 12), bg="#00b894", fg="white", padx=10, pady=5, command=lambda: self.restaurante.ver_pedido(mesa, cliente))
        button_ver_pedido.pack()

        button_finalizar = tk.Button(ventana_opciones, text="Finalizar", font=("Helvetica", 12), bg="#ff6b6b", fg="white", padx=10, pady=5, command=lambda: self.restaurante.finalizar(cliente, mesa))
        button_finalizar.pack()

    def hacer_pedido(self, cliente, mesa):
        ventana_pedido = tk.Toplevel()
        ventana_pedido.title(f"Hacer pedido para {cliente.nombre}")
        ventana_pedido.configure(bg="#f0f0f0")

        label_pedido = tk.Label(ventana_pedido, text="Seleccione los platos que desea y la cantidad:", font=("Helvetica", 14), bg="#f0f0f0")
        label_pedido.pack()

        platos_frame = tk.Frame(ventana_pedido, bg="#f0f0f0")
        platos_frame.pack()

        # Lista para almacenar las variables de cantidad
        cantidad_vars = []

        for plato in self.restaurante.menu:
            label_plato = tk.Label(platos_frame, text=f"{plato.nombre} - ${plato.precio}", font=("Helvetica", 12), bg="#f0f0f0")
            label_plato.grid(row=len(cantidad_vars), column=0, padx=(5, 0), pady=(5, 0), sticky="w")

            label_cantidad = tk.Label(platos_frame, text="Cantidad:", font=("Helvetica", 12), bg="#f0f0f0")
            label_cantidad.grid(row=len(cantidad_vars), column=1, padx=(5, 0), pady=(5, 0), sticky="e")

            cantidad_var = tk.StringVar()
            entry_cantidad = tk.Entry(platos_frame, textvariable=cantidad_var, font=("Helvetica", 12), width=5)
            entry_cantidad.grid(row=len(cantidad_vars), column=2, padx=(0, 5), pady=(5, 0), sticky="w")

            cantidad_vars.append((plato, cantidad_var))

        button_confirmar = tk.Button(ventana_pedido, text="Confirmar Pedido", font=("Helvetica", 12), bg="#00b894", fg="white", padx=10, pady=5, command=lambda: self.confirmar_pedido(cliente, mesa, ventana_pedido, cantidad_vars))
        button_confirmar.pack()

    def confirmar_pedido(self, cliente, mesa, ventana, cantidad_vars):
        platos_seleccionados = []

        for (plato, cantidad_var) in cantidad_vars:
            cantidad = cantidad_var.get()
            if cantidad.isdigit() and int(cantidad) > 0:
                platos_seleccionados.extend([plato] * int(cantidad))

        if len(platos_seleccionados) > 0:
            for plato in platos_seleccionados:
                self.restaurante.hacer_pedido(mesa, cliente, plato)
            ventana.destroy()
            messagebox.showinfo("Pedido Confirmado", "Se ha realizado el pedido correctamente.")
        else:
            messagebox.showerror("Error", "Debe ingresar una cantidad válida (mayor a 0) para confirmar el pedido.")