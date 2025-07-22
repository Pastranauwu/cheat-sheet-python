# Crear
mi_lista = [1, 2, 3, "hola", True]

# Indexación y slicing
mi_lista[0]         # 1
mi_lista[-1]        # True
mi_lista[1:4]       # [2, 3, "hola"]

# Métodos útiles
mi_lista.append(99)       # Añade al final
mi_lista.insert(1, 2) # Inserta en índice 1
mi_lista.remove("hola")   # Elimina el primer "hola"
mi_lista.pop()            # Quita el último elemento
mi_lista.index(2)         # Índice del valor 2
mi_lista.count(3)         # Cuántas veces aparece 3
mi_lista.sort()           # Ordena (solo si todos son comparables)
mi_lista.reverse()        # Invierte la lista


len(mi_lista)  
2 in mi_lista
nueva = mi_lista + [10, 11]
repetida = mi_lista * 2


# Crear
mi_tupla = (1, 2, 3)
solo_uno = (5,)  # ¡Ojo con la coma!

# Acceso igual que listas
mi_tupla[0]
mi_tupla[1:3]

# Inmutables
# mi_tupla[0] = 99  ❌ Error

# Métodos útiles
mi_tupla.count(2)
mi_tupla.index(3)



# Crear
persona = {"nombre": "Ana", "edad": 30}

# Acceso
persona["nombre"]
persona.get("correo", "No disponible")

# Modificar / Agregar
persona["edad"] = 31
persona["correo"] = "ana@mail.com"

# Eliminar
del persona["edad"]
persona.pop("correo", None)

# Recorrer
for clave in persona:
    print(clave, persona[clave])

for clave, valor in persona.items():
    print(clave, valor)

persona.keys()
persona.values()
persona.items()
persona.update({"edad": 25, "ciudad": "CDMX"})


# Con parámetros opcionales
def suma(a, b=5):
    return a + b

# Con *args y **kwargs
def imprimir_todo(*args, **kwargs):
    print(args)
    print(kwargs)
    
cuadrados = [x**2 for x in range(5)]
pares = [x for x in range(10) if x % 2 == 0]

cuadrados = {x: x**2 for x in range(5)}


try:
    # Código que puede fallar
    x = int(input("Dame un número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Eso no es un número.")
    

with open("archivo.txt", "r") as f:
    contenido = f.read()

with open("nuevo.txt", "w") as f:
    f.write("Hola mundo")
    

doble = lambda x: x * 2
print(doble(4))  # 8


for i, letra in enumerate("hola"):
    print(i, letra)

a = [1, 2, 3]
b = ["a", "b", "c"]
for x, y in zip(a, b):
    print(x, y)
    
    
def decorador(func):
    def envuelto():
        print("Antes")
        func()
        print("Después")
    return envuelto

@decorador
def saluda():
    print("Hola")

saluda()