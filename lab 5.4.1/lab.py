import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные (x, y и их ошибки)
x_data = np.array([0,
50,
100,
150,
200,
250,
300,
350,
400,
450,
475,
500,
525,
550,
575,
600,
625,
650,
675,
700,
725])
y_data = np.array([981,
991,
1004,
1015,
1000,
916,
807,
704,
605,
502,
456,
410,
363,
324,
277,
240,
191,
156,
114,
80,
55])
x_data = 757.5 - x_data

# Определяем функцию для аппроксимации (логистическая функция)
def exp_func(x, A, B, x0):
    return A * x + B

# Начальные предположения для параметров A, x0
initial_params = [50, 50, 200]

# Подгонка функции к данным
popt, pcov = curve_fit(exp_func, x_data, y_data, p0=initial_params)

# Полученные параметры A, x0
A, B, x0 = popt
print(A, x0)

# Производная от аппроксимации (аналитически)
def exp_derivative(x, A, B, x0):
    return A + x - x

# Масштабированная производная
def scaled_derivative(x, A, B, x0, scale=-150):
    return scale * exp_derivative(x, A, B, x0)

# Построение графика
plt.figure(figsize=(8, 6))
plt.ylim(-100, 1200)
plt.xlim(00, 800)

# Наносим экспериментальные данные с погрешностями
plt.errorbar(x_data, y_data, fmt='o', label='I(p)', color='blue', capsize=5)


# Касательная линия в точке x = 8

# Подписи осей
plt.xlabel('p, торр')
plt.ylabel('I, пА')

# Легенда
plt.legend()

# Сетка
plt.grid(True)

# Показываем график
plt.show()
