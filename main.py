from shagzoda import *
t_case = int(input())
for i in range(t_case):
    x, y, w, z = map(int, input().split())
    nuqta1 = nuqta(x, y)
    nuqta2 = nuqta(w, z)
    prince = Shaxzoda(nuqta1, nuqta2)
    n = int(input())
    counter = 0
    for j in range(n):
        a, b, r = map(int, input().split())
        a_nuqta = nuqta(a, b)
        circle = aylana(a_nuqta, r)
        if prince.kesibUtadimi(circle):
            counter += 1
    print(counter)