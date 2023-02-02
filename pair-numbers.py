a = int(input("Entre com um valor: "))
b = int(input("Entre com um valor: "))
resto_a = a%2
resto_b = b%2
if resto_a == 0 or not resto_b > 0:
    print("Foi Digitado um numero par")
else:
    print("Nenhum numero par foi digitado")

c = int(input("Entre com um valor: "))
d = int(input("Entre com um valor: "))
resto_c = a%2
resto_d = b%2
if resto_c == 0 or resto_d == 0:
    print("Foi Digitado um numero par")
else:
    print("Nenhum numero par foi digitado")