# Clase base que representa un producto general
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre  # Atributo privado
        self._precio = precio  # Atributo privado
        self._cantidad = cantidad  # Atributo privado

    def mostrar_info(self):
        # Muestra la información del producto
        print(f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}")

    def obtener_precio(self):
        return self._precio

    def reducir_stock(self, cantidad):
        if self._cantidad >= cantidad:
            self._cantidad -= cantidad
            return True
        return False

# Clase que representa una prenda de ropa, hereda de Producto
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla  # Atributo privado

    def mostrar_info(self):
        # Muestra la información de la prenda, incluyendo la talla
        super().mostrar_info()
        print(f"Talla: {self._talla}")

# Clase que representa una camisa, hereda de Ropa
class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

# Clase que representa un pantalón, hereda de Ropa
class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

# Clase que representa un zapato, hereda de Producto
class Zapato(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla  # Atributo privado

    def mostrar_info(self):
        # Muestra la información del zapato, incluyendo la talla
        super().mostrar_info()
        print(f"Talla: {self._talla}")

# Clase que representa la tienda
class Tienda:
    def __init__(self):
        self._inventario = []  # Lista para almacenar los productos disponibles

    def agregar_producto(self, producto):
        # Agrega un producto al inventario
        self._inventario.append(producto)

    def mostrar_inventario(self):
        # Muestra la información de todos los productos en el inventario
        for producto in self._inventario:
            producto.mostrar_info()

    def buscar_producto(self, nombre_producto):
        # Busca un producto en el inventario por nombre
        for producto in self._inventario:
            if producto._nombre == nombre_producto:
                return producto
        return None

# Clase que representa el carrito de compras
class Carrito:
    def __init__(self):
        self._productos = []  # Lista para almacenar los productos en el carrito

    def agregar_al_carrito(self, producto, cantidad):
        # Agrega un producto al carrito de compras
        if producto.reducir_stock(cantidad):
            self._productos.append((producto, cantidad))
            print(f"{cantidad} {producto._nombre}(s) agregado(s) al carrito.")
        else:
            print("Stock insuficiente para agregar al carrito.")

    def mostrar_carrito(self):
        # Muestra el contenido del carrito de compras
        print("Carrito de Compras:")
        total = 0
        for producto, cantidad in self._productos:
            producto.mostrar_info()
            print(f"Cantidad: {cantidad}")
            total += producto.obtener_precio() * cantidad
        print(f"Total a pagar: ${total}")

# Ejemplo de uso del sistema
tienda = Tienda()

# Crear instancias de productos
camisa = Camisa("Camisa", 50, 10, "M")
pantalon = Pantalon("Pantalón", 70, 5, "L")
zapato = Zapato("Zapato", 100, 8, 42)

# Agregar productos al inventario de la tienda
tienda.agregar_producto(camisa)
tienda.agregar_producto(pantalon)
tienda.agregar_producto(zapato)

# Mostrar el inventario de la tienda
tienda.mostrar_inventario()

# Crear una instancia del carrito de compras
carrito = Carrito()

# Interacción con el usuario
while True:
    print("\nOpciones:")
    print("1. Mostrar inventario")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tienda.mostrar_inventario()
    elif opcion == "2":
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        producto = tienda.buscar_producto(nombre_producto)
        if producto:
            carrito.agregar_al_carrito(producto, cantidad)
        else:
            print("Producto no encontrado.")
    elif opcion == "3":
        carrito.mostrar_carrito()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
