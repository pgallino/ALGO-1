def collatz(n):

    print(n)

    if n == 1:
        return 
    
    if n%2 == 0:
        n = n // 2
    
    elif n%2 != 0:
        n *= 3
        n += 1
    
    collatz(n)

collatz(5)
print("aca termina collatz de 5")

collatz(187)
print("aca termina collatz de 187")