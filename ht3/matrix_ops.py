import random

def make_vector(n):
    return [random.random() for _ in range(n)]

def make_matrix(m, n):
    return [[random.random() for _ in range(n)] for _ in range(m)]

def mat_vec_mul(A, v):
    res = []
    for i in range(len(A)):
        s = 0
        for j in range(len(v)):
            s += A[i][j] * v[j]
        res.append(s)
    return res

def diag_sum(A):
    s = 0
    for i in range(min(len(A), len(A[0]))):
        s += A[i][i]
    return s

def dot(a, b):
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s

def histogram(v, bins):
    mn = min(v); mx = max(v)
    if mx == mn:
        return [0] * bins
    step = (mx - mn) / bins
    res = [0] * bins
    for x in v:
        idx = int((x - mn) / step)
        if idx == bins:
            idx = bins - 1
        res[idx] += 1
    return res

def filter_vector(v, kernel):
    n = len(v); k = len(kernel); p = k // 2
    res = []
    for i in range(n):
        s = 0
        for j in range(k):
            idx = i + j - p
            if 0 <= idx < n:
                s += v[idx] * kernel[j]
        res.append(s)
    return res

def mat_mul(A, B):
    m = len(A); k = len(B); n = len(B[0])
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            s = 0
            for t in range(k):
                s += A[i][t] * B[t][j]
            res[i][j] = s
    return res

def convolution_2d(image, kernel):
    h = len(image); w = len(image[0])
    kh = len(kernel); kw = len(kernel[0])
    pad_h = kh // 2; pad_w = kw // 2
    result = []
    for i in range(h):
        row = []
        for j in range(w):
            total = 0
            for ki in range(kh):
                for kj in range(kw):
                    ii = i + ki - pad_h
                    jj = j + kj - pad_w
                    if 0 <= ii < h and 0 <= jj < w:
                        total += image[ii][jj] * kernel[ki][kj]
            row.append(total)
        result.append(row)
    return result

def write_data(filename, data):
    with open(filename, 'w') as f:
        for row in data:
            f.write(' '.join(str(x) for x in row) + '\n')

def read_data(filename):
    res = []
    with open(filename, 'r') as f:
        for line in f:
            res.append([float(x) for x in line.split()])
    return res
