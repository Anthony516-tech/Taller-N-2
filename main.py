def read(filename):
    with open(filename, 'r', encoding="utf-8") as file:

        for linea in file:
            datos = linea.strip().split(",")  

            # Introducimos los datos de la línea del CSV en la matriz:
            data.append(datos)

# Función para buscar el saldo de un cliente por su nombre:
def buscar_saldo(nombre):

    # Ciclo para recorrer la matriz
    for i, linea in enumerate(data):
        if i == 1:
            continue
    
        # Buscamos en la columna o posición donde van los nombres:
        if linea[2] == nombre:
            saldo = linea[3]
            return saldo
    
    return None

# Función para buscar saldos mayores a 50:
def buscar_saldo_mayor50():

    # Ciclo para recorrer la matriz
    for i, linea in enumerate(data):
        if i == 1:
            continue
    
        # Buscamos en la columna o posición donde van los saldos:
        if linea[3] > 50:
            cliente = linea[2]
            clientes.append(cliente)

# Función para ordenar los clientes por su saldo:
def ordenar_saldo():

    # Ciclo para recorrer la matriz
    for i, linea in enumerate(data):
        if i == 1:
            continue

        tupla = linea[2], linea[3]
        clientes_completos.append(tupla)  
    
    # Ordenamos los clientes:
    for cliente in clientes_completos:
        clientes_ordenados.append(cliente[1])
    
    for i, saldo in enumerate(clientes_ordenados):
        if saldo > clientes_ordenados[i + 1]:
            t = clientes_ordenados[i + 1]
            clientes_ordenados[i + 1] = saldo
            saldo = t
            



# Creamos matriz donde se va a guardar la información:
data = []

# Leemos el archivo CSV:
read("clientes.csv")


# Buscamos el saldo del cliente por su nombre
nombre = input("Ingrese el nombre del cliente al que quiere averiguar su saldo: ")
saldo = buscar_saldo(nombre)
print(f"El saldo del cliente {nombre} es: {saldo} \n")

clientes = []
# Buscamos los clientes con saldos mayores a 50:
buscar_saldo_mayor50()
print("Los clientes con un saldo mayor a 50 son: \n")
for cliente in clientes:
    print(cliente, "\n")

clientes_completos = []
clientes_ordenados = []
# Organizamos los clientes según su saldo:
ordenar_saldo()
print("Los clientes organizados ascendentemente por su saldo son:")
for cliente in clientes_ordenados:
    print(cliente, "\n")





