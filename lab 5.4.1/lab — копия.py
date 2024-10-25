import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные (x, y и их ошибки)
x_data = np.array([350,
375,
400,
425,
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
725,
750])
n_data = np.array([5,
21,
15,
15,
60,
160,
344,
268,
1059,
954,
3702,
2664,
4000,
8540,
4394,
6620,
7057])
t_data = np.array([20,
60,
100,
40,
100,
30,
41.5,
20,
44.4,
20,
43.8,
20,
21.2,
36.4,
15.9,
22,
20])
x_data = 757.2 - x_data
y_data = n_data / t_data
y_err = y_data * n_data ** 0.5 / n_data

# Определяем функцию для аппроксимации (логистическая функция)
def exp_func(x, A, B, x0):
    return A / (1 + np.exp((x - x0) / B))

# Начальные предположения для параметров A, x0
initial_params = [50, 50, 200]

# Подгонка функции к данным
popt, pcov = curve_fit(exp_func, x_data, y_data, p0=initial_params)

# Полученные параметры A, x0
print(pcov)
A, B, x0 = popt
print(A, x0)

# Производная от аппроксимации (аналитически)
def exp_derivative(x, A, B, x0):
    return -(A * np.exp((x - x0) / B) ) / (np.exp((x - x0) / B) + 1) ** 2 / B

# Масштабированная производная
def scaled_derivative(x, A, B, x0, scale=-150):
    return scale * exp_derivative(x, A, B, x0)

# Построение графика
plt.figure(figsize=(8, 6))
plt.ylim(-100, 500)
plt.xlim(00, 500)

# Наносим экспериментальные данные с погрешностями
plt.errorbar(x_data, y_data, yerr=y_err, fmt='o', label='N(x)', color='blue', capsize=5)

# Наносим аппроксимацию
x_fit = np.linspace(-100, 400, 500)
y_fit = exp_func(x_fit, A, B, x0)
plt.plot(x_fit, y_fit, label='Аппроксимация dN/dx (x)', color='red')

# Наносим масштабированную производную
y_deriv = scaled_derivative(x_fit, A, B, x0)
plt.plot(x_fit, y_deriv, label='С * dN/dx (x)', color='black', linestyle='--')

# Вертикальная линия по центру кривой
center_x = x0  # Центр логистической функции
plt.axvline(x=center_x, color='green', linestyle='--', label=f'x = {center_x:.2f}')

# Значение производной в точке x = 8
x_point = round(x0, 2)
slope_at_point = exp_derivative(x_point, A, B, x0)

# Уравнение касательной линии в точке x = 8
def tangent_line(x, slope, x0, y0):
    return slope * (x - x0) + y0

# Касательная линия в точке x = 8
y_tangent = tangent_line(x_fit, slope_at_point, x_point, exp_func(x_point, A, B, x0))
plt.plot(x_fit, y_tangent, 'b--', label=f'Касательная в x={x_point}')

# Вертикальная линия в точке пересечения касательной с осью x
x_cross = x_point - exp_func(x_point, A, B, x0) / slope_at_point

# Обозначения пересечений с осью x
plt.text(x_cross + 0.2, 0, f'{x_cross:.2f}', color='blue', fontsize=10, verticalalignment='top')
plt.text(center_x + 0.2, 0, f'{center_x:.2f}', color='green', fontsize=10, verticalalignment='top')

# Подписи осей
plt.xlabel('p, torr')
plt.ylabel('N, имп / сек')

# Легенда
plt.legend()

# Сетка
plt.grid(True)

# Показываем график
plt.show()
