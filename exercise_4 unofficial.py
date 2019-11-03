

from itertools import combinations 
a = list(input())

g = ()
for i in range(len(a)):
    c = list(combinations(a,i+1))
    for j in range(len(c)):
        if c[j] == c[j][::-1] and len(c[j]) > len(g):
            g = c[j]
            
        
print(len(g))
