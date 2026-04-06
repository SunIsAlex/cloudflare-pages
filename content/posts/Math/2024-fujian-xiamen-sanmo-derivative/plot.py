import numpy as np
import matplotlib.pyplot as plt

# 1. x 取值（避开 -1）
x = np.linspace(-0.99, 3, 500)

# 2. 真值
y_true = np.log(1 + x)
# 3. Padé 近似
y_approx = (3*x**2 + 6*x) / (x**2 + 6*x + 6)

# 4. 百分误差
error_percent = (y_approx - y_true) / y_true * 100

# 5. 画图
plt.plot(x, error_percent)
plt.xlabel("x")
plt.ylabel("Percentage Error (%)")
plt.title("ln(1+x) vs Pade [2/2]")
plt.grid()

plt.show()