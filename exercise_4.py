

# Returns the length of the longest palindromic subsequence in a  
# i and j are indexes of a
def recpa(a, i, j): 
      
    #If there is only 1 character      
    if (i == j): 
        return 1
  
    #If there are only 2 characters and both are same      
    if (a[i] == a[j] and i + 1 == j): 
        return 2
      
    # If the first and last characters match  
    if (a[i] == a[j]): 
        return recpa(a, i + 1, j - 1) + 2
  
    # If the first and last characters do not match  
    return max(recpa(a, i, j - 1), recpa(a, i + 1, j))