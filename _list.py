"""The important properties of Python lists are as follows:

Lists are ordered – Lists remember the order of items inserted.
Accessed by index – Items in a list can be accessed using an index.
Lists can contain any sort of object – It can be numbers, strings, tuples and even other lists.
Lists are changeable (mutable) – You can change a list in-place, add new items, and delete or update existing items.
"""

L = ['red', 'green', 'blue', 'yellow', 'black']

print(L[0])
# Prints red

print(L[2])
# Prints blue

L = ['red', 'green', 'blue', 'yellow', 'black']
print(L[10])
# Triggers IndexError: list index out of range

#Negative List Indexing
L = ['red', 'green', 'blue', 'yellow', 'black']

print(L[-1])
# Prints black

print(L[-2])
# Prints yellow

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])
# Prints eee


L = ['a', 'b', 'c', 'd', 'e', 'f']

print(L[2:5])
# Prints ['c', 'd', 'e']

print(L[0:2])
# Prints ['a', 'b']

print(L[3:-1])
# Prints ['d', 'e']

L = ['red', 'green', 'blue']

L[0] = 'orange'
print(L)
# Prints ['orange', 'green', 'blue']

L[-1] = 'violet'
print(L)
# Prints ['orange', 'green', 'violet']

L = ['red', 'green', 'yellow']
L.append('blue')
print(L)
# Prints ['red', 'green', 'yellow', 'blue']

L = ['red', 'green', 'yellow']
L.insert(1,'blue')
print(L)
# Prints ['red', 'blue', 'green', 'yellow']


L = ['red', 'green', 'yellow']
L.extend([1,2,3])
print(L)
# Prints ['red', 'green', 'yellow', 1, 2, 3]

# concatenation operator
L = ['red', 'green', 'blue']
L = L + [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

# augmented assignment operator
L = ['red', 'green', 'blue']
L += [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

L = ['red', 'green', 'blue']
x = L.pop(1)
print(L)
# Prints ['red', 'blue']

# removed item
print(x)
# Prints green

L = ['red', 'green', 'blue']
L.remove('red')
print(L)
# Prints ['green', 'blue']

L = ['red', 'green', 'blue', 'yellow', 'black']
del L[1:4]
print(L)
# Prints ['red', 'black']

L = ['red', 'green', 'blue']
L.clear()
print(L)
# Prints []

L = ['red']
L = L * 3
print(L)
# Prints ['red', 'red', 'red']

L = ['red', 'green', 'blue']
print(len(L))
# Prints 3

# Check for presence
L = ['red', 'green', 'blue']
if 'red' in L:
    print('yes')

# Check for absence
L = ['red', 'green', 'blue']
if 'yellow' not in L:
    print('yes')


L = ['red', 'green', 'blue']
for item in L:
    print(item)
# Prints red
# Prints green
# Prints blue

# Loop through the list and double each item
L = [1, 2, 3, 4]
for i in range(len(L)):
    L[i] = L[i] * 2

print(L)
# Prints [2, 4, 6, 8]

L = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])
# Prints eee

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[-3])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[-3][-1])
# Prints ['eee', 'fff']

print(L[-3][-1][-2])
# Prints eee

L = ['a', ['bb', 'cc'], 'd']
L[1][1] = 0
print(L)
# Prints ['a', ['bb', 0], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].append('xx')
print(L)
# Prints ['a', ['bb', 'cc', 'xx'], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].insert(0,'xx')
print(L)
# Prints ['a', ['xx', 'bb', 'cc'], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].extend([1,2,3])
print(L)
# Prints ['a', ['bb', 'cc', 1, 2, 3], 'd']

L = ['a', ['bb', 'cc', 'dd'], 'e']
x = L[1].pop(1)
print(L)
# Prints ['a', ['bb', 'dd'], 'e']

# removed item
print(x)
# Prints cc

L = ['a', ['bb', 'cc', 'dd'], 'e']
del L[1][1]
print(L)
# Prints ['a', ['bb', 'dd'], 'e']

L = ['a', ['bb', 'cc', 'dd'], 'e']
L[1].remove('cc')
print(L)
# Prints ['a', ['bb', 'dd'], 'e']

L = ['a', ['bb', 'cc'], 'd']

print(len(L))
# Prints 3

print(len(L[1]))
# Prints 2

L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for list in L:
    for number in list:
        print(number, end=' ')
# Prints 1 2 3 4 5 6 7 8 9

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7])
# Prints ['c', 'd', 'e', 'f', 'g']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[-7:-2])
# Prints ['c', 'd', 'e', 'f', 'g']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:-5])
# Prints ['c', 'd']

# Return every 2nd item between position 2 to 7
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7:2])
# Prints ['c', 'e', 'g']

# Return every 2nd item between position 6 to 1
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:1:-2])
# Prints ['g', 'e', 'c']

# Slice the first three items from the list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[:3])
# Prints ['a', 'b', 'c']

# Slice the last three items from the list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:])
# Prints ['g', 'h', 'i']

L = ['a', 'b', 'c', 'd', 'e']
print(L[::-1])
# Prints ['e', 'd', 'c', 'b', 'a']

# Modify multiple list items
L = ['a', 'b', 'c', 'd', 'e']
L[1:4] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'e']

# Replace multiple elements in place of a single element
L = ['a', 'b', 'c', 'd', 'e']
L[1:2] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'c', 'd', 'e']


# Insert at the start
L = ['a', 'b', 'c']
L[:0] = [1, 2, 3]
print(L)
# Prints [1, 2, 3, 'a', 'b', 'c']

# Insert at the end
L = ['a', 'b', 'c']
L[len(L):] = [1, 2, 3]
print(L)
# Prints ['a', 'b', 'c', 1, 2, 3]

# Insert in the middle
L = ['a', 'b', 'c']
L[1:1] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'b', 'c']

L = ['a', 'b', 'c', 'd', 'e']
L[1:5] = []
print(L)
# Prints ['a']

L = ['a', 'b', 'c', 'd', 'e']
del L[1:5]
print(L)
# Prints ['a']

L1 = ['a', 'b', 'c', 'd', 'e']
L2 = L1[:]
print(L2)
# Prints ['a', 'b', 'c', 'd', 'e']
print(L2 is L1)
# Prints False


L = []
L.append(0)
L.append(1)
L.append(4)
L.append(9)
L.append(16)
print(L)
# Prints [0, 1, 4, 9, 16]

L = []
for x in range(5):
    L.append(x**2)
print(L)
# Prints [0, 1, 4, 9, 16]

L = [x**2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]

L = [x*3 for x in 'RED']
print(L)
# Prints ['RRR', 'EEE', 'DDD']

# Convert list items to absolute values
vec = [-4, -2, 0, 2, 4]
L = [abs(x) for x in vec]
print(L)
# Prints [4, 2, 0, 2, 4]

# Remove whitespaces of list items
colors = ['  red', '  green ', 'blue  ']
L = [color.strip() for color in colors]
print(L)
# Prints ['red', 'green', 'blue']

L = [(x, x**2) for x in range(4)]
print(L)
# Prints [(0, 0), (1, 1), (2, 4), (3, 9)]

# Filter list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
L = [x for x in vec if x >= 0]
print(L)
# Prints [0, 2, 4]


vec = [-4, -2, 0, 2, 4]
L = []
for x in vec:
    if x >= 0:
        L.append(x)
print(L)
# Prints [0, 2, 4]


# With list comprehension
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = [number for list in vector for number in list]
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# equivalent to the following plain, old nested loop:
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = []
for list in vector:
    for number in list:
        L.append(number)
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
L = [[row[i] for row in matrix] for i in range(3)]
print(L)
# Prints [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#List Comprehension vs map() + lambda

"""
When all you’re doing is calling an already-defined function 
on each element, map(f, L) is a little faster than the corresponding 
list comprehension [f(x) for x in L].

"""


# With list comprehension
L = [ord(x) for x in 'foo']
print(L)
# Prints [102, 111, 111]

# With map() function
L = list(map(ord, 'foo'))
print(L)
# Prints [102, 111, 111]


# With list comprehension
L = [x ** 2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]

# With map() function
L = list(map((lambda x: x ** 2), range(5)))
print(L)
# Prints [0, 1, 4, 9, 16]

# With list comprehension
L = [x for x in range(10) if x % 2 == 0]
print(L)
# Prints [0, 2, 4, 6, 8]

# With filter() function
L = list(filter((lambda x: x % 2 == 0), range(10)))
print(L)
# Prints [0, 2, 4, 6, 8]