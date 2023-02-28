def sucesion(n):
    for n in range(1, n + 1):
        print("\\frac {1}{10^{" + str(n) + "}}", end = " ")
    
    print()

    for n in range(1, n +1):
        print(float(round((1 / (10 ** n)) , n)), end = " ")

    print()

sucesion(int(input("Ingresa tu numero: ")))
