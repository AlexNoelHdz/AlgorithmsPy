def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 


print('========n*n = n^2 or O(n^2)===========')
print('Less efficient from time complexity point of view')
print_items(10)