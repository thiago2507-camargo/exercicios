base=int(input("digite um numero:"))
inicio=int(input("digite um numero:"))
fim=int(input("digite um numero:"))
def tabuada_personalizada(base, inicio, fim):
    print(f"Tabuada do {base} de {inicio} a {fim}:")
    for j in range(inicio, fim + 1):
        print(f"{base} x {j} = {base*j}")
    print()
        
tabuada_personalizada(base, inicio, fim)
