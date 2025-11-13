def josephus(n, k):    
    sobrevivente_idx = 0  
    for i in range(2, n + 1):
        sobrevivente_idx = (sobrevivente_idx + k) % i
    return sobrevivente_idx + 1

entradas = int(input())

for i in range(1, entradas + 1):
    n, k = map(int, input().split(" "))
    
    resultado = josephus(n, k)
    
    print(f"Case {i}: {resultado}")