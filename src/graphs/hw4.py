import random
import matplotlib.pyplot as plt

#Code for Part 1
def graphgen (n,p):
    adjmat = [[0 for a in range(n)] for b in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            r=(int(random.random()<p))
            adjmat[i][j]= r
            adjmat[j][i]=r
    return adjmat

#Code for Part 2
def sizecheck(G, thresh):
    #homework said that I MAY use DFS for this section
    #so I assumed it was optional. I used something similar to BFS
    gnodes = len(G)
    fndlist = [0 for x in range(gnodes)]
    for row in range(gnodes):
        if fndlist[row]:
            continue
        found = 1
        fndlist[row] = 1
        Q = [row]
        while len(Q):
            cur = Q.pop()
            for e in range(gnodes):
                if (G[cur][e] and not fndlist[e]):
                    found += 1
                    if (found >= thresh):
                        return 1    
                    fndlist[e] = 1
                    Q.append(e)        
    return 0;

#Code for Part 3
def test():
    n = 40
    crange = [c/10 for c in range(2,31,2)]
    data = []
    for c in crange:
        p = c/n
        big = 0
        for i in range(500):
             G = graphgen(n, p)
             if(sizecheck(G,30)):
                big+=1
        data.append(big)
    print(data)
    percentages = [d/5 for d in data]
    plt.plot(crange, percentages)
    plt.show()
    
test()


    
