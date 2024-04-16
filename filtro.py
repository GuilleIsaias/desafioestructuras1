import sys

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}


def filtro(p_precio, umbral, tipo):
    if tipo == "mayor":
        productos = [k for k, v in p_precio.items() if v > umbral]
        print(f'Los productos mayores a {umbral} son: {productos}')
    elif tipo == "menor":
        productos = [k for k, v in p_precio.items() if v < umbral]
        print(f'Los productos menores a {umbral} son: {productos}')
    else:
        print("Lo sentimos, no es una operación válida")

if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    filtro(precios, umbral, "mayor")
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    tipo = sys.argv[2]
    filtro(precios, umbral, tipo)
else:
    print("Lo sentimos, no es una operación válida")
