D = {'emp1': {'name': 'Vishavjeet', 'job': 'Data Scientist'},
     'emp2': {'name': 'Anupam', 'job': 'Sr. Manager'},
     'emp3': {'name': 'Nishu', 'job': 'CEO'}}

print(D['emp1']['name'])
# Prints Vishavjeet

print(D['emp2']['job'])
# Sr. Manager

print(D['emp1']['salary'])
# Triggers KeyError: 'salary'

# key absent
print(D['emp1'].get('salary'))
# Prints None

# key present
print(D['emp1'].get('name'))
# Prints Vishavjeet

#Change Nested Dictionary Items

D = {'emp1': {'name': 'Vishavjeet', 'job': 'Data Scientist'},
     'emp2': {'name': 'Anupam', 'job': 'Sr. Manager'},
     'emp3': {'name': 'Nishu', 'job': 'CEO'}}

D['emp3']['name'] = 'Compiler'
D['emp3']['job'] = 'Tech Lead'

print(D['emp3'])
# Prints {'name': 'Compiler', 'job': 'Tech Lead'}


D = {'emp1': {'name': 'Vishavjeet', 'job': 'Data Scientist'},
     'emp2': {'name': 'Anupam', 'job': 'Sr. Manager'},
     'emp3': {'name': 'Max', 'job': 'Janitor'}
     }

#Merge Two Nested Dictionaries

D1 = {'emp1': {'name': 'Vishavjeet', 'job': 'Data Scientist'},
     'emp2': {'name': 'Anupam', 'job': 'Sr. Manager'},
     'emp3': {'name': 'Max', 'job': 'Janitor'}
     }

D2 = {'emp4': {'name': 'Nimesh', 'job': 'Sr. Software Engineer'},
     'emp5': {'name': 'Gulfam', 'job': 'Sr. Software Engineer'}
     }

D1.update(D2)

print(D1)

x = D.pop('emp3')

print(x)

del D['emp3']

D = {'emp1': {'name': 'Vishavjeet', 'job': 'Data Scientist'},
     'emp2': {'name': 'Anupam', 'job': 'Sr. Manager'},
     'emp3': {'name': 'Max', 'job': 'Janitor'}
     }

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])


D = {}
D[0] = 0
D[1] = 1
D[2] = 4
D[3] = 9
D[4] = 16
print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

D = {}
for x in range(5):
    D[x] = x**2

print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Comprehension

D = {x: x**2 for x in range(5)}
print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

D = {c: c * 3 for c in 'RED'}
print(D)
# Prints {'R': 'RRR', 'E': 'EEE', 'D': 'DDD'}

L = ['ReD', 'GrEeN', 'BlUe']
D = {c.lower(): c.upper() for c in L}
print(D)
# Prints {'blue': 'BLUE', 'green': 'GREEN', 'red': 'RED'}

D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selectedKeys = [0, 2, 5]

X = {k: D[k] for k in selectedKeys}

print(X)
# Prints {0: 'A', 2: 'C', 5: 'F'}

#Filter Dictionary Contents

D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
removeKeys = [0, 2, 5]

X = {k: D[k] for k in D.keys() - removeKeys}

print(X)
# Prints {1: 'B', 3: 'D', 4: 'E'}

# Invert Mapping / Reverse lookup

D = {0: 'red', 1: 'green', 2: 'blue'}
R = {v: k for k,v in D.items()}
print(R)
# Prints {'red': 0, 'green': 1, 'blue': 2}

#Dictionary Comprehension with Enumerate

L = ['red', 'green', 'blue']
D = {k:v for k,v in enumerate(L)}
print(D)
# Prints {0: 'red', 1: 'green', 2: 'blue'}


D = {ix: line for ix, line in enumerate(open('myFile.txt'))}
print(D)
# {0: 'First line\n',
#  1: 'Second line\n',
#  2: 'Third line\n'}

# Initialize Dictionary with Comprehension

keys = ['red', 'green', 'blue']

# using dict comprehension
D = {k: 0 for k in keys}
print(D)
# Prints {'red': 0, 'green': 0, 'blue': 0}

# equivalent to using fromkeys() method
D = dict.fromkeys(keys, 0)
print(D)
# Prints {'red': 0, 'green': 0, 'blue': 0}

keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']

# using dict comprehension
D = {k: v for (k, v) in zip(keys, values)}
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# equivalent to using dict() on zipped keys/values
D = dict(zip(keys, values))
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

#Dictionary Comprehension with if Clause

D = {x: x**2 for x in range(6) if x % 2 == 0}

print(D)
# Prints {0: 0, 2: 4, 4: 16}

D = {}
for x in range(5):
    if x % 2 == 0:
        D[x] = x**2

print(D)
# Prints {0: 0, 2: 4, 4: 16}

D = {(k,v): k+v for k in range(2) for v in range(2)}
print(D)
# Prints {(0, 1): 1, (1, 0): 1, (0, 0): 0, (1, 1): 2}

# is equivalent to
D = {}
for k in range(2):
    for v in range(2):
        D[(k,v)] = k+v
print(D)
# Prints {(0, 1): 1, (1, 0): 1, (0, 0): 0, (1, 1): 2}