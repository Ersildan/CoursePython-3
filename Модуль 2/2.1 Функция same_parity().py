def same_parity(numbers):
    return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))
   
   
'''    
Sample Input 1:
print(same_parity([]))
Sample Output 1:
[]

Sample Input 2:
print(same_parity([6, 0, 67, -7, 10, -20]))
Sample Output 2:
[6, 0, 10, -20]

Sample Input 3:
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
Sample Output 3:
[-7, 67, -9, -29]
'''
