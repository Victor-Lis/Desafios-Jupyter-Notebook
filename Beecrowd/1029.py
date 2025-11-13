entradas = int(input()) 

for i in range(entradas): 
    num_calls = 0 
    inicial = int(input()) 
    
    def fibonacci(n): 
        global num_calls 
        num_calls += 1 
        if n == 0 or n == 1: 
            return n 
        else: 
            return fibonacci(n - 1) + fibonacci(n - 2) 
        
    result = fibonacci(inicial) 
    print(f"fib({inicial}) = {num_calls-1} calls = {result}")