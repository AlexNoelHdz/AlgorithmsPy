'''
Simplification tecnique
Drop Non-Dominants
'''
def print_items(n):
    # 100 operations: O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    # 10 operations O(n)
    for k in range(n):
        print(k)

    # Result = (n^2 + n)
    '''
    As a percentaje, n becomes unsignificant 
    Dominant term: n^2
    Non dominant: term n
    Drop non dominant
    O(n^2)
    '''    

print_items(10)
