termos = int(input("Quantos termos você deseja? "))
fibonacci = 1
fibonacci2 = 1
contador = 0
while contador < termos:
    print(fibonacci)
    auxiliar = fibonacci + fibonacci2
    fibonacci = fibonacci2
    fibonacci2 = auxiliar
    contador += 1