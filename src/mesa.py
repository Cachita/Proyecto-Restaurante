class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = False
        self.clientes = {}

    def ocupar(self, cliente):
        self.estado = True
        self.clientes[cliente.nombre] = cliente

    def desocupar(self):
        self.estado = False
        self.clientes.clear()

    def esta_disponible(self):
        return not self.estado

    def hacer_pedido(self, cliente, pedido):
        if cliente.nombre in self.clientes:
            self.clientes[cliente.nombre].agregar_plato(pedido)
            return True  # Indica que el pedido se realizó correctamente
        else:
            return False  # Indica que no hay cliente registrado en esta mesa

    def mostrar_pedido(self, cliente):
        if cliente.nombre in self.clientes:
            cliente.ver_pedido()
        else:
            messagebox.showinfo("Pedido", "No hay pedido registrado para este cliente en esta mesa.")

    def calcular_total(self, cliente, incluir_propina=False):
        if cliente.nombre in self.clientes:
            total = self.clientes[cliente.nombre].calcular_total()
            return total
        else:
            return 0
