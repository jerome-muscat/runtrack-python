def inversecaractère(caractère):
    ch=""
    for i in range((len(caractère)) -1, -1, -1):
        ch = ch + caractère[i]
    return ch

print(inversecaractère("nikana"))

caractère=(input("veuiller taper ce que vous voulez inverser : "))
print(inversecaractère(caractère))