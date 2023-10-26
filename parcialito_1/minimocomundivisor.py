def calcular_mcd(n, m):
    r = 0
    while True:
        r = m % n
        if r == 0:
            return n
        m, n = n, r   #forma GOD

def calcular_mcd(n, m): #mi forma sidosa
    "le das dos numeros y te da el minimo común divisor"
    divisores=[]
    if n>m:
        resto = n%m
        if resto == 0:
            return m
        elif resto != 0:
            divisores.append(resto)
            resto = m%resto
            divisores.append(resto)
            while resto != 0:
                resto = divisores[len(divisores)-2]%resto
                divisores.append(resto)
    elif m>n:
        resto = m%n
        if resto == 0:
            return n
        elif resto != 0:
            divisores.append(resto)
            resto = n%resto
            divisores.append(resto)
            while resto != 0:
                resto = divisores[len(divisores)-2]%resto
                divisores.append(resto)
    return divisores[-2]