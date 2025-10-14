import numpy as np
import matplotlib.pyplot as plt

funcion = input("\033[1;37m"+"Introduce una función de x (por ejemplo: x**2 + 3*x - 5) o 2*exp(x+1): \n"
                "\033[1;33mNota: \033[1;37mPuedes usar sen(x), cos(x), tan(x), exp(x), log(x) \n"
                "======================================================================================\n"
                "")

def f(x):
    return eval(funcion, {"x": x, 
                           "sen": np.sin, 
                           "cos": np.cos, 
                           "tan": np.tan, 
                           "exp": np.exp, 
                           "log": np.log})

x = np.linspace(-10, 10, 400)
y = f(x)


plt.plot(x, y, label=f"y = {funcion}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("■=== Gráfica de la función ===■")
plt.legend()
plt.grid(True)
plt.show()