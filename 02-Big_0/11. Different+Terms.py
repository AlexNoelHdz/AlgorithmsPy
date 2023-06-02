'''
What happned when you have different therms for inputs. 
'''
def print_items(a,b):
    for i in range(a): # O(a)
        print(i)

    for j in range(b): # O(b)
        print(j)

print_items(1, 10) # O(a + B)  # Far you can simplify


def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j) 

# O(a*b)
