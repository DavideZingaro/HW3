
from itertools import combinations 
a = list(input())

def makeCombos(arr):
     for i in range(len(arr) + 1):
         for combo in map(list, combinations(arr, i)):
            yield combo

g = ()
d = makeCombos(a)

while True:
    
    try:
        c = next(d)
    except StopIteration:
            break
        
    for j in range(len(c)):
        if c[j] == c[j][::-1] and len(c[j]) > len(g):
            g = c[j]
            
        
        
print(len(g))