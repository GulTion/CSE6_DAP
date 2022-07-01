
a = [
    [1,2,3],
    [3,4,5],
    [5,6,7]
]

b = [
    [1,2,3],
    [3,4,5],
    [5,6,7]
]

c = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]





def martixMultipication(a,b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

