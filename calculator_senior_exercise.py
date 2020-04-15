# Hacer que la calculadora pueda recibir n números
# Recibir los números con un sólo input, separados por comas
# Escribe los números a jugar con ellos, separados por una coma -> 5,6,4,3,5,7

# Realizar la suma de todos los números
# Calcular el promedio de todos los números
# Calcular la multiplicación de todos los números
# Elevar cada uno de los números al cuadrado
# Calcular el factorial de cada uno de los números
# Y el factorial de la suma de todos los números

# Modularizar lo más que se pueda el código

# Y ya je
def sumaDigitos(num):
    s = 0 
    while num > 0:
        s = s + num % 10
        num = num // 10


n = int(input("Cantidad de numeros: "))
sumaT = 0 
while n > 0:
    num = int(input("Numeros: "))
    sumaT = sumaT + sumaDigitos(num)
    n = n -1

print (sumaT)


    
