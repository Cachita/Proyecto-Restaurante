import tkinter as tk
from restaurante import Restaurante
from restaurante_app import RestauranteApp
from mesa import Mesa
from cliente import Cliente
from plato import Plato
import os 

def main():
    # Crear mesas
    mesas = [Mesa(1, 4), Mesa(2, 4), Mesa(3, 4), Mesa(4, 4),
             Mesa(5, 4), Mesa(6, 4), Mesa(7, 4), Mesa(8, 4)]

    # Crear menú
    menu = [Plato("Hamburguesa", 8000.0, ["Carne", "Pan", "Lechuga", "Tomate", "Salsas de la casa"]),
            Plato("Pizza de peperoni", 7000.0, ["Masa madre", "Queso", "Salsa", "Pepperoni"]),
            Plato("Pizza perro", 7000.0, ["Masa madre", "Chorizo", "Salsa tártara", "Salsa de piña", "Papita chongo", "Queso rayado"]),
            Plato("Ensalada", 8000.0, ["Lechuga", "Tomate", "Pepino", "Zanahoria"]),
            Plato("Sopa de Mondongo", 8000.0, ["Mondongo", "Yuca", "Papa", "Mazorca", "Cebollín", "Ajo", "Cilantro"]),
            Plato("Pizza de pollo", 7000.0, ["Pollo", "Yuca", "Papa", "Mazorca", "Cebollín", "Ajo", "Cilantro"]),
            Plato("Salchipapa sencilla", 10000.0, ["Papa", "Salchicha", "Salsa de tomate", "Mayonesa", "Queso", "Salsa de la casa", "Papita chongo"]),
            Plato("Salchipollo", 12000.0, ["Papa", "Pollo", "Salsa de tomate", "Mayonesa", "Queso", "Salsa de la casa", "Papita chongo"]),
            Plato("Salchipapa ranchera", 10000.0, ["Papa", "Salchicha ranchera", "Chorizo", "Butifarra", "Salsa de tomate", "Mayonesa", "Queso", "Salsa de la casa", "Papita chongo"]),
            Plato("Arroz con pollo", 15000.0, ["Arroz", "Pollo", "Verduras"]),
            Plato("Arroz chino", 18000.0, ["Arroz", "Pollo", "Verduras", "Huevo", "Salsa de soja"]),
            Plato("Pasta carbonara", 22000.0, ["Pasta", "Bacon", "Huevo", "Queso"]),
            Plato("Pasta bolognesa", 21000.0, ["Pasta", "Carne molida", "Tomate", "Cebolla"]),
            Plato("Arroz paisa", 25000.0, ["Arroz", "Carne", "Chorizo", "Plátano", "Aguacate"]),
            Plato("Bandeja paisa", 30000.0, ["Carne", "Chorizo", "Chicharrón", "Huevo", "Arroz", "Frijoles", "Aguacate"]),
            Plato("Jugo de Tomate", 3000.0, ["Tomate de árbol", "Azucar", "Hielo"]),
            Plato("Jugo de Corozo", 4000.0, ["Corozo", "Azucar", "Hielo"]),
            Plato("Agua", 2000.0, ["Agua"])]

    # Crear restaurante
    restaurante = Restaurante(mesas, menu)

    root = tk.Tk()
    root.title("Restaurante")
    root.configure(bg="#f0f0f0")

    #Esto va con el import os
    dir_actual = os.getcwd()
    # Agregar imagen
    img_path = os.path.join(dir_actual, "restaurant_icon.png")
    img = tk.PhotoImage(file=img_path)
    resized_img = img.subsample(2, 2)  # Redimensionar la imagen

    img_label = tk.Label(root, image=resized_img, bg="#f0f0f0")
    img_label.image = resized_img
    img_label.pack()

    app = RestauranteApp(root, restaurante)
    root.after(1000, app.actualizar_mesas)
    root.mainloop()

if __name__ == "__main__":
    main()