L = [7, 11, 42, 39, 2, 15]

def mylen(L):
    compteur = 0
    for i in L:
        compteur=compteur+1
    return compteur

def croissant(L):
    i=0
    for i in range(mylen(L)):
        for j in range(i+1,mylen(L)):
            if L[i] > L[j]:
                L[i],L[j]=L[j],L[i]
    return L

print(croissant(L))