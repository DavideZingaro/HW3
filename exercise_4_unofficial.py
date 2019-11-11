

from itertools import combinations 
a = list(input())

g = ()
for i in range(len(a)-1,0,-1):
    c = list(combinations(a,i+1))
    for j in range(len(c)):
        if c[j] == c[j][::-1] and len(c[j]) > len(g):
            g = c[j]
            break
    else:
        continue
    
    break

print(len(g))
