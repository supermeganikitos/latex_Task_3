import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
g = 9.81  # ускорение свободного падения, м/с^2
m = 1.0  # масса тела, кг
k = 0.1  # коэффициент сопротивления, кг/м

# Начальные условия
x0, y0, z0 = 0.0, 0.0, 0.0  # начальные координаты, м
vx0, vy0, vz0 = 20.0, 0.0, 20.0  # начальные скорости, м/с
t0, t_end = 0.0, 5.0  # временной интервал, с
h = 0.01  # шаг интегрирования, с


def system(t, state, with_drag=True):
    """
    Функция, возвращающая производные состояния системы.

    Параметры:
    t -- время
    state -- вектор состояния [x, y, z, vx, vy, vz]
    with_drag -- учитывать ли сопротивление воздуха

    Возвращает:
    производные состояния [vx, vy, vz, ax, ay, az]
    """
    x, y, z, vx, vy, vz = state

    # Скорость и её модуль
    v = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)

    # Ускорения
    if with_drag and v > 0:
        ax = -k * vx * v / m
        ay = -k * vy * v / m
        az = -g - k * vz * v / m
    else:
        ax = 0.0
        ay = 0.0
        az = -g

    return np.array([vx, vy, vz, ax, ay, az])


def euler_method(system, state0, t0, t_end, h, with_drag=True):
    """
    Метод Эйлера для интегрирования системы ОДУ.
    """
    n_steps = int((t_end - t0) / h)
    states = np.zeros((n_steps + 1, len(state0)))
    times = np.linspace(t0, t_end, n_steps + 1)
    states[0] = state0

    for i in range(n_steps):
        derivative = system(times[i], states[i], with_drag)
        states[i + 1] = states[i] + h * derivative

    return times, states


def rk4_method(system, state0, t0, t_end, h, with_drag=True):
    """
    Метод Рунге-Кутты 4-го порядка для интегрирования системы ОДУ.
    """
    n_steps = int((t_end - t0) / h)
    states = np.zeros((n_steps + 1, len(state0)))
    times = np.linspace(t0, t_end, n_steps + 1)
    states[0] = state0

    for i in range(n_steps):
        state = states[i]
        t = times[i]

        k1 = system(t, state, with_drag)
        k2 = system(t + h / 2, state + h / 2 * k1, with_drag)
        k3 = system(t + h / 2, state + h / 2 * k2, with_drag)
        k4 = system(t + h, state + h * k3, with_drag)

        states[i + 1] = state + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return times, states


# Решение задачи различными методами
initial_state = np.array([x0, y0, z0, vx0, vy0, vz0])

# Аналитическое решение (без сопротивления)
t_analytical = np.linspace(t0, t_end, 500)
x_analytical = x0 + vx0 * t_analytical
z_analytical = z0 + vz0 * t_analytical - 0.5 * g * t_analytical ** 2

# Численное решение методом Эйлера
t_euler, state_euler = euler_method(system, initial_state, t0, t_end, h, with_drag=False)

# Численное решение методом RK4
t_rk4, state_rk4 = rk4_method(system, initial_state, t0, t_end, h, with_drag=False)

# Решение с учетом сопротивления воздуха методом RK4
t_drag, state_drag = rk4_method(system, initial_state, t0, t_end, h, with_drag=True)

print("Расчет завершен успешно!")
print(f"Количество шагов интегрирования: {len(t_euler)}")
print(f"Конечное положение (RK4, без сопротивления): x = {state_rk4[-1, 0]:.2f} м, z = {state_drag[-1, 2]:.2f} м")