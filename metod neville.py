import numpy as np
import matplotlib.pyplot as plt

def neville(x, y, x_interpolate):
    n = len(x)
    Q = np.zeros((n, n))  # Matriz de interpolación inicializada con ceros

    for i in range(n):
        Q[i, 0] = y[i]  # Se asigna el valor y[i] en la columna 0 de la matriz

    for i in range(1, n):
        for j in range(1, i + 1):
            # Fórmula de interpolación de Neville
            Q[i, j] = ((x_interpolate - x[i - j]) * Q[i, j - 1] - (x_interpolate - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])

    return Q

x = np.array([1.0, 1.3, 1.6, 1.9, 2.2])  # Valores conocidos de x
y = np.array([0.7651977, 0.6200860, 0.4554022, 0.28148186, 0.1103626])  # Valores correspondientes de y
x_interpolate = 1.5  # Valor de x para el cual se desea interpolar y

# Calcula la matriz de interpolación
interpolation_matrix = neville(x, y, x_interpolate)
interpolated_value = interpolation_matrix[-1, -1]  # Obtiene el valor interpolado de la última celda de la matriz

print("Interpolated value:", interpolated_value)

# Gráfica de los puntos de datos
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y, color='red')

# Genera los puntos interpolados para trazar la curva de interpolación
x_interpolate_array = np.linspace(min(x), max(x), 100)
y_interpolate_array = np.array([neville(x, y, xi)[-1, -1] for xi in x_interpolate_array])
plt.plot(x_interpolate_array, y_interpolate_array, color='blue', label='Interpolacion')

# Marca el punto interpolado en la gráfica
plt.scatter(x_interpolate, interpolated_value, color='green', label='Punto de interpolacion')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolacion usando el metodo Neville')
plt.show()

print("Matriz de interpolacion: ")
print(interpolation_matrix)
