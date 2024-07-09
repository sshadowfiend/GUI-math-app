from math import exp


a1 = 0.25
a2 = 0.1
u1 = 20
u2 = 40
b = 0.75
u = 75
tn = 0
tk = 40
t1 = 20


def main_func(n: int) -> tuple:

    dt = (tk - tn) / (n - 1)
    t = [i * dt for i in range(n)]
    uvx, uvix = [], []

    for i in range(n):
        if t[i] <= t1:
            uvx.append(u * (1 - exp(-a1 * t[i])))
        else:
            uvx.append(u * (1 - exp(-a1 * t1)) * exp(-b * (t[i] - t1)))

    for i in range(n):
        if uvx[i] < u1:
            uvix.append(a2 * uvx[i] ** 2)
        else:
            uvix.append(u2)

    for i in range(n):
        t[i] = float("%.2f" % t[i])
        uvx[i] = float("%.2f" % uvx[i])
        uvix[i] = float("%.2f" % uvix[i])

    return t, uvx, uvix


def calculate_impulse_len(n: int, u_: list[float]) -> float:
    dt = (tk - tn) / (n - 1)
    dl = 0
    umax = max(u_)
    umin = min(u_)
    a = umax - umin  # амплитуда сигнала
    uimp = umin + a / 2
    for i in range(n):
        if u_[i] >= uimp:
            dl += dt

    return float("%.2f" % dl)


t_ref, uvx_ref, uvix_ref = main_func(1000)
ref_par_uvx = calculate_impulse_len(1000, uvx_ref)
ref_par_uvix = calculate_impulse_len(1000, uvix_ref)


def par_error_rate(n: int) -> tuple:
    t, uvx, uvix = main_func(n)
    return (
        abs(calculate_impulse_len(n, uvx) - ref_par_uvx),
        abs(calculate_impulse_len(n, uvix) - ref_par_uvix)
    )
