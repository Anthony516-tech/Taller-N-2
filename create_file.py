import pandas as pd

# Creamos el archivo:
datos = {
    'Cédula' : [12345, 54321],
    'Nombre' : ["Jose", "Dario"],
    'Saldo' : [50.43, 43.12]
}

df = pd.DataFrame(datos)

df.to_csv('clientes.csv')