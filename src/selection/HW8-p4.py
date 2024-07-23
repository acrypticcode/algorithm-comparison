def greedy(A, W):
    sack=[]
    sortA = sorted(A, key=lambda x: x[1]/x[0], reverse = True)
    print("sortA is ", sortA)

    chosen = []
    value = 0
    w = W
    for a in sortA:
        if a[0]<=w:
            chosen.append(a)
            value += a[1]
            w = w-a[0]
    return value

def dynamic (A, W):
    n = len(A)
    
    K = [[0 for i in range(n+1)] for h in range(W+1)]
    for j in range(1,n+1):
        wj = A[j-1][0]
        vj = A[j-1][1]
        for w in range(1, W+1):
            if wj > w: 
                K[w][j]=K[w][j-1]
            else:
                K[w][j]= max(K[w][j-1], K[w-wj][j-1]+vj)
    return K[W][n]

dataset = [[96, 91], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96],
           [102, 97], [103, 97], [104, 99], [106, 101], [107, 101],
           [106, 102], [107, 102], [109, 104], [109, 106], [110, 107],
           [111, 108], [113, 107], [114, 110]]

print(greedy(dataset, 100))
print(dynamic(dataset, 100))
print(greedy(dataset, 200))
print(dynamic(dataset, 200))
print(greedy(dataset, 300))
print(dynamic(dataset, 300))



    
