# Exrcice 4
x = int(input("Entrez un entier x:"))
for n in range (1, 11):
    print (x, "*",n, "=" ,x * n)
somme = 0
n = 1 

while n <= x:
    somme += n
    n += 1

print(f"La somme de 1 à {x} est : {somme}")