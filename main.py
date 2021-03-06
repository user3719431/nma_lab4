import numpy as np
import lab2

def krylov(A: np.ndarray):
    np.set_printoptions(precision = 5)
    n = A.shape[0]
    y = np.zeros((n + 1, n))
    y[0][0] = 1
    for i in range(1, n + 1):
        y[i] = A@y[i - 1]
    print('y = ', y)
    B = y[n]
    y = np.transpose(y[0:n])
    y = y[:, ::-1]
    p = lab2.gaus(y.tolist(), B.tolist())
    print('p = ', p)
    p = np.array(p)
    l = np.roots(np.concatenate(([1], -1 * p)))
    print('l = ', l)

def main():
    np.set_printoptions(precision=5, suppress = True)
    A = np.array([
        [6.00, 1.10, 0.97, 1.24],
        [1.10, 4.00, 1.30, 0.16],
        [0.97, 1.30, 5, 2.10],
        [1.24, 0.16, 2.10, 7.0]
    ])
    krylov(A)

if __name__ == '__main__':
    main()