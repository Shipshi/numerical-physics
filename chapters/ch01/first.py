import numpy as np

def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def central_diff(f, x, h):
    return (f(x + h) - (f(x - h))) / (2 * h)

x0 = 1.0
exact = np.cos(x0)

for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
    err_f = abs(forward_diff(np.cos, x0, h) - exact)
    err_c = abs(central_diff(np.cos, x0, h) - exact)
    print(f"h = {h:.1e}, Forward Diff Error = {err_f:.2e}, Central Diff Error = {err_c:.2e}")
