      
# Returns the length of the longest  
# palindromic subsequence in seq  
def pal(a, i, j): 
      
    # Base Case 1: If there is  
    # only 1 character  
    if (i == j): 
        return 1
  
    # Base Case 2: If there are only 2  
    # characters and both are same  
    if (a[i] == a[j] and i + 1 == j): 
        return 2
      
    # If the first and last characters match  
    if (a[i] == a[j]): 
        return pal(a, i + 1, j - 1) + 2
  
    # If the first and last characters do not match  
    return max(pal(a, i, j - 1), pal(a, i + 1, j)) 