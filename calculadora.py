def calc(a, b, op): 
    if op == "soma": 
        return a + b 
    elif op == "sub": 
        return a - b 
    elif op == "mult": 
        return a * b 
    elif op == "div": 
        if b == 0: 
            return None 
        return a / b 

if __name__ == "__main__": 
    print(calc(10, 5, "soma")) 
    print(calc(10, 5, "sub")) 
    print(calc(10, 5, "mult")) 
    print(calc(10, 0, "div"))