def french_mult(x,y):
    #return x times y using recursion
    if y == 0:
        return 0
    z = french_mult(x, y>>1)
    if y%2 == 0:
        return z<<1
    else:
        return x + z>>1

def loop_mult(x,y):
    #return x times y using a loop
    rec_stack = []
    z = 0
    while y > 0:
        rec_stack.append(y%2)
        y = y>>1
    ln = len(rec_stack)
    while ln > 0:
        if rec_stack.pop() == 1:
            z = (z<<1) + x
        else:
            z = z<<1
        ln = ln-1
    return z
        


    

#print(french_mult(35,2**1022))
print(loop_mult(35,2**1023))

