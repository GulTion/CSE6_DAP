
a = [
    [1,2,3],
    [3,4,5],
    [5,6,7]
]

b = [
 
    [3,4,5],
    [5,6,7],
    [7,8,9]
]

c = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]




def martixMultipication(a,b,c):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

print(martixMultipication(a,b,c))


# [[34, 40, 46], [64, 76, 88], [94, 112, 130]]