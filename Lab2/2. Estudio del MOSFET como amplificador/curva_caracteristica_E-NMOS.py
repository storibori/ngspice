import matplotlib.pyplot as plt
import numpy as np

# Función para leer los datos de los archivos .data y separar bloques por líneas vacías
def leer_datos_multiple(fichero):
    with open(fichero, 'r') as file:
        contenido = file.read()
        
    # Dividir en bloques de datos separados por líneas vacías
    bloques = contenido.strip().split('\n\n')
    
    # Crear una lista para guardar los datos de cada bloque
    datos = []
    
    for bloque in bloques:
        # Leer cada bloque como una matriz de números
        datos_bloque = np.loadtxt(bloque.splitlines())
        datos.append(datos_bloque)
    
    return datos

# Leer los datos de los dos archivos
bloques_vgs = leer_datos_multiple('graf_id_vs_vgs_e-mosfet.data')
bloques_vds = leer_datos_multiple('graf_id_vs_vds_e-mosfet.data')

# Crear una figura para una única gráfica
plt.figure(figsize=(8, 6))

# Graficar los bloques de datos de Vgs con enumeradores en la leyenda
for i, bloque in enumerate(bloques_vgs):
    x_vgs = bloque[:, 0]
    id_vgs = bloque[:, 1]
    plt.plot(x_vgs, id_vgs, label=f'ID vs VGS', color='b')

# Graficar los bloques de datos de Vds con enumeradores en la leyenda
for i, bloque in enumerate(bloques_vds):
    x_vds = bloque[:, 0]
    id_vds = bloque[:, 1]
    plt.plot(x_vds, id_vds, label=f'VGS {i}', color='g')

# Etiquetas y título
plt.title('Gráficas de Id vs Vgs y Id vs Vds')
plt.xlabel('Voltaje (V)')
plt.ylabel('Corriente (Id)')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()