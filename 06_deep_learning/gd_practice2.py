import numpy as np 
from gradient_descent import gradient_descent


def grad_a(w):
    return 2 * (w - 4)

path = gradient_descent(grad_a, w0= 10, lr= 0.2, steps= 3)
print("alpha= 0.2:", path)
assert np.allclose(path, [10.0, 7.6, 6.16, 5.296])

path = gradient_descent(grad_a, w0= 10, lr= 0.5, steps= 4)
print("alpha = 0.5:", path)
assert path == [10.0, 4.0, 4.0, 4.0, 4.0]

path = gradient_descent(grad_a, w0= 10, lr= 1.5, steps= 2)
print("alpha = 1.5:", path)
assert path == [10.0, -8.0, 28.0]

