def f1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f1(n-1) + f1(n-2)

def f2(n):
    if n == 0:
        return 0
    else:
        fib = [0,1]
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
        return fib[-1]
    
