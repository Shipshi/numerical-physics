import numpy as np

def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h) 

x0 = 1.0
exact = np.cos(x0)

print(f"{'h':>8} {'err forward':>12} {'err central':>12}")
for h in (1e-1, 1e-2, 1e-3, 1e-4):
    err_f = abs(forward_diff(np.sin, x0, h) - exact)
    err_c = abs(central_diff(np.sin, x0, h) - exact)
    print(f"{h:8.1e} {err_f:12.2e}, {err_c:12.2e}")