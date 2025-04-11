import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

# Definir a variável e a função simbólica
x = symbols('x')
f = 2*x + 1  # Exemplo de função

# Converter a função simbólica em uma função numérica
f_lambdified = lambdify(x, f, 'numpy')

# Criar valores para o eixo X
x_vals = np.linspace(-3, 3, 400)  # De -3 a 3 com 400 pontos
y_vals = f_lambdified(x_vals)

# Criar o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='$f(x) = 2*x + 1$', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title('Gráfico de $f(x) = 2*x + 1$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
