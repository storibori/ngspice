import numpy as np
import matplotlib.pyplot as plt

# Cargar datos desde el archivo
data = np.loadtxt("graf_id_vs_vgs_e-mosfet.data")

# Separar columnas: VGS en la primera columna, ID en la segunda
VGS = data[:, 0]
ID = data[:, 1]

# Calcular la transconductancia gm como la derivada numérica de ID respecto a VGS
gm = np.gradient(ID, VGS)

# Mostrar el valor máximo de gm como referencia
gm_max = np.max(gm)
print(f"Valor máximo de gm: {gm_max:.6f} S")

# Graficar gm vs VGS
plt.figure(figsize=(8, 6))
plt.plot(VGS, gm, label='g_m = dId/dVgs', color='r')
plt.xlabel("VGS (V)")
plt.ylabel("g_m (S)")
plt.title("Transconductancia g_m vs VGS")
plt.legend()
plt.grid()
plt.show()