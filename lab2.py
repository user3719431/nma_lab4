import copy

def sub(b, ax):
    r = []
    for i in range(len(b)):
        r.append((abs(b[i] - ax[i])))
    return r

def multiply(a, x):
    ax = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += a[i][j] * x[j]
        ax.append(sum)
    return ax

def findMax(a, y, k):
    m = a[k][k]
    maxCoordinate = [k, k]
    for i in range(len(a) - k):
        for j in range(len(a[i]) - 1 - k):
            if abs(a[i + k][j + k]) > m:
                m = a[i + k][j + k]
                maxCoordinate = [i + k][j + k]
    x = a[k]
    a[k] = a[maxCoordinate[0]]
    a[maxCoordinate[0]] = x
    for i in range(len(a)):
        x = a[i][k]
        a[i][k] = a[i][maxCoordinate[1]]
        a[i][maxCoordinate[1]] = x
    
    c = y[k]
    y[k] = y[maxCoordinate[1]]
    y[maxCoordinate[1]] = c
    return a

def cout(a):
    for i in range(len(a)):
        b = ''
        for j in range(len(a[i]) - 1):
            b += (' ' + str(a[i][j]))
        b += ' | ' + str(a[i][len(a[i]) - 1])
        print(b)
    print('____________')

def gaus(a, b):
    z = [x for x in range(len(a))]
    for i in range(len(b)):
        a[i].append(b[i])
    cout(a)
    for i in range(len(a)):
        a = findMax(a, z, i)
        x = a[i][i]
        cout(a)
        for j in range(len(a[i])):
            a[i][j] /= x
        cout(a)
        for j in range(len(a)):
            if j == i:
                continue
            y = a[j][i]
            for k in range(len(a[i])):
                a[j][k] -= y * a[i][k]
        cout(a)
    result = []
    for i in z:
        result.append(a[i][-1])
    print(z)
    return result

def main():
    a = [
        [3.81, 0.25, 1.28, 0.75],
        [2.25, 1.32, 4.58, 0.49],
        [5.31, 6.28, 0.98, 1.04],
        [9.39, 2.45, 3.35, 2.28]
    ]
    b = [4.21, 6.47, 2.38, 10.48]
    x = gaus(copy.deepcopy(a), b)
    print('x:', x)
    ax = multiply(a, x)
    print('Ax:', ax)
    r = sub(b, ax)
    print('r', r)

if __name__ == '__main__':
    main()