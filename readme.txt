Cosas a tener en cuenta del código.

-= Main.py =-
- En la línea 7 se usó la instrucción "import os" -> Esto se hizo con la finalidad de buscar de forma automática la imagen para después no tener que dar la ruta de origen.
- La línea 42 "dir_actual = os.getcwd()" va de la mano con la línea 7.
- En la línea 44 va la instrucción de la imagen "img_path = os.path.join(dir_actual, "restaurant_icon.png")", si se desea cambiar, eso es a gusto propio de cada quien.

En dado caso que quieran modificar la imagen y la ruta para colocar una ruta en específico, lo pueden hacer. Deben eliminar "import os", "dir_actual = os.getcwd()" y para modificar la instrucción "img_path = os.path.join(dir_actual, "restaurant_icon.png")".
Podemos hacer lo siguiente: img_path = "C:/Users/(usuario)/(ruta)/Restaurante proyecto python/restaurant_icon.png" y con eso debería funcionar.

-= Nota =-
Si se desea cambiar la imagen, se debe tener en cuenta que el ejecutable debe estar en la misma ruta que dicha imagen, de lo contrario, marcará un error.