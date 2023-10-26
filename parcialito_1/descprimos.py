def descomposicion_factores_primos(k):
    while k > 1:
        for i in range(2, k+1):
            if k%i == 0:
                print(i)
                k = k//i
                break