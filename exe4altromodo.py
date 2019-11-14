
from itertools import combinations 
a = list(input())

def combgener(arr):
     for i in range(len(arr) + 1):
         for combo in map(list, combinations(arr, i)):
            yield combo

g = ()
d = combgener(a)

while True:
    
    try:
        c = next(d)
    except StopIteration:
            break        
    
    if c == c[::-1] and len(c) > len(g):
        g = c
            
        
        
print(len(g))