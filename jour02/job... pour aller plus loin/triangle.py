def triangle(a, b, c):
    lmax = max(a, b, c)

    if a + b > c and lmax == c or b + c > a and lmax == a or a + c > b and lmax == b:
        if a == b == c:
            print("Ceci est un triangle équilatéral")
        
        elif a == b != c or b == c != a or a == c != b:
            print("Ceci est un triangle isocèle")
        
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("Ceci est un triangle rectangle")
        
        elif a**2 + b**2 == c**2 and a == b != c or b**2 + c**2 == a**2 and b == c != a or a**2 + c**2 == b**2 and a == c != b:
            print("Ceci est un triangle rectangle isocèle")

        else:
            print("Ceci est un triangle quelconque")

    else:
        print("ceci n'est pas un triangle")

triangle(10, 10, 10)
triangle(20, 20, 32)
triangle(30, 40, 50)
triangle(40, 20, 30)
triangle(50, 30, 20)