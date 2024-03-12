import tkinter as tk

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedido = []

    def agregar_plato(self, plato):
        self.pedido.append(plato)

    def ver_pedido(self):
        pedido_window = tk.Toplevel()
        pedido_window.title("Pedido")
        pedido_window.configure(bg="#f0f0f0")

        label = tk.Label(pedido_window, text=f"Pedido de {self.nombre}", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        for plato in self.pedido:
            label = tk.Label(pedido_window, text=plato.nombre + f" - ${plato.precio}", font=("Helvetica", 12), bg="#f0f0f0")
            label.pack()

        total_label = tk.Label(pedido_window, text="Total: $" + str(self.calcular_total()), font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        total_label.pack()

    def calcular_total(self):
        total = sum(plato.precio for plato in self.pedido)
        return total