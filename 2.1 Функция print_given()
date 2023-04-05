def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for name, value in sorted(kwargs.items()):
        print(name, value, type(value))
        
'''        
Sample Input 1:
print_given(1, [1, 2, 3], 'three', two=2)

Sample Output 1:
1 <class 'int'>
[1, 2, 3] <class 'list'>
three <class 'str'>
two 2 <class 'int'>

Sample Input 2:
print_given('apple', 'cherry', 'watermelon')

Sample Output 2:
apple <class 'str'>
cherry <class 'str'>
watermelon <class 'str'>

Sample Input 3:
print_given(b=2, d=4, c=3, a=1)
Sample Output 3:
a 1 <class 'int'>
b 2 <class 'int'>
c 3 <class 'int'>
d 4 <class 'int'>

Sample Input 4:
print_given()
Sample Output 4:
None
'''
