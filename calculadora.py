def calc(a, b, op): 
    if op == "soma": 
        return a + b 
    elif op == "sub": 
        return a - b 
    elif op == "mult": 
        return a * b 
    elif op == "div": 
        return a / b 
    elif op == "pot":
        return a**b
    elif op == "raiz":
        if a < 0:
            return "Erro: não existe raiz quadrada real de número negativo"
        return a ** 0.5
if __name__ == "__main__": 
    print(calc(10, 5, "soma")) 
    print(calc(10, 5, "sub")) 
    print(calc(10, 5, "mult")) 
    print(calc(10, 5, "div"))
    print(calc(2, 3, "pot"))
    print(calc(16,9, "raiz"))