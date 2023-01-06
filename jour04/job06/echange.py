L = [1, 15, 16, 40, 50]

for a,b in [(0,4)]:
    L[a],L[b] = L[b],L[a]
    print(L)