import matplotlib.pyplot as plt
import numpy as np

# Función para leer los datos de los archivos .data
def leer_datos(fichero):
    datos = np.loadtxt(fichero)
    return datos[:, 0], datos[:, 1]  # Retorna las dos columnas (Id, Vgs o Id, Vds)

# Leer los datos de los dos archivos
x_vgs, id_vgs = leer_datos('graf_id_vs_vgs.data')
x_vds, id_vds = leer_datos('graf_id_vs_vds.data')

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# Gráfica de Id vs Vgs
ax[0].plot(x_vgs, id_vgs, label='Id vs Vgs', color='b')
ax[0].set_title('Gráfica de Id vs Vgs')
ax[0].set_xlabel('Vgs')
ax[0].set_ylabel('Id')
ax[0].grid(True)

# Resaltar puntos que cortan el eje X (Id = 0)
corte_x_vgs = x_vgs[np.isclose(id_vgs, 0, atol=1e-6)]  # Corta en Id=0
ax[0].scatter(corte_x_vgs, np.zeros_like(corte_x_vgs), color='red', label='Corte en eje X', zorder=5)

# Gráfica de Id vs Vds
ax[1].plot(x_vds, id_vds, label='Id vs Vds', color='g')
ax[1].set_title('Gráfica de Id vs Vds')
ax[1].set_xlabel('Vds')
ax[1].set_ylabel('Id')
ax[1].grid(True)

# Resaltar puntos que cortan el eje X (Id = 0)
corte_x_vds = x_vds[np.isclose(id_vds, 0, atol=1e-6)]  # Corta en Id=0
ax[1].scatter(corte_x_vds, np.zeros_like(corte_x_vds), color='red', label='Corte en eje X', zorder=5)

# Añadir leyenda a las gráficas
ax[0].legend()
ax[1].legend()

# Ajustar el espacio entre las gráficas
plt.tight_layout()

# Mostrar las gráficas
plt.show()
