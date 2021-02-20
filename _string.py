#Create a String
S = 'Hello, Python-ds.com!'       # single quotes
S = "Hello, Tech-question.com!"   # double quotes

#Multiline Strings

S = """Hi. My name is Nishu Chauhan. 
I'm the creator of Tech-question.com,
 and I provide the content."""
print(S)
# Hi. My name is Nishu Chauhan.
# I'm the creator of Tech-question.com,
# and I provide the content.

#The str() Constructor

# an integer to a string
S = str(56)
print(S)
# Prints '56'

# a complex number to a string
S = str(4+5j)
print(S)
# Prints '(4+5j)

# List to String
S = str([11,12])
print(S)
# Prints '[11, 12]'

#Access Characters by Index

# Indexing
S = 'ABCDEFGHI'
print(S[0])    # Prints A
print(S[5])    # Prints F

# Negative Indexing
S = 'ABCDEFGHI'
print(S[-1])    # Prints I
print(S[-6])    # Prints D

#Slicing a String

S = 'ABCDEFGHI'
print(S[2:5])      # Prints CDE
print(S[5:-1])     # Prints FGH
print(S[1:6:2])    # Prints BDF

#Modify a String

S = 'Hello, World!'
S[0] = 'J'
# we cann't change because sting is immutable
# Triggers TypeError: 'str' object does not support item assignment

#If you wante to modify then we can do using below example
#The best we can do is create a new string that is a variation of the original:

S = 'Hello, world!'
new_S = 'J' + S[1:]
print(new_S)
# Prints Jello, world!

#String Concatenation

# concatenation operator
S = 'Python,' + ' DS!'
print(S)
# Python, DS!

# augmented assignment operator
S = 'Python,'
S += ' DS!'
print(S)
# Prints Python, DS!

# Implicit concatenation.
S = 'Hello,' " World!"
print(S)
# Prints Hello, World!

S = ('Put strings within parentheses '
    'to join them together.')
print(S)
# Put strings within parentheses to join them together.

# We can replicate substrings in a string using the replication operator *

# the hard way
S = '-------------------------'

# the easy way
S = '-' * 25

#Find String Length

S = 'Supercalifragilisticexpialidocious'
print(len(S))
# Prints 34

#Replace Text Within a String

S = 'Hello, Python!'
x = S.replace('Python', 'Kali')
print(x)
# Prints Hello, Kali!

#Split and Join a String

# Split the string on comma
S = 'red,green,blue,yellow'
x = S.split(',')
print(x)
# Prints ['red', 'green', 'blue', 'yellow']
print(x[0])
# Prints red

# Join the list of substrings
L = ['red', 'green', 'blue', 'yellow']
S = ','.join(L)
print(S)
# Prints red,green,blue,yellow

#String Case Conversion

S = 'Hello, PYTHON-DS.COM!'
print(S.lower())
# Prints hello, python-ds.com!

S = 'Hello, python-ds.com!'
print(S.upper())
# Prints HELLO, PYTHON-DS.COM!

S = 'Hello, python-ds.com!'
print(S.capitalize())
# Prints Hello, Python-ds.com!

S = 'Hello, World!'
print(S.swapcase())
# Prints hELLO, wORLD!

S = 'hello, world!'
print(S.title())
# Prints Hello, World!

#Check if Substring Contains in a String

S = 'Hello, World!'
print('Hello' in S)
# Prints True

# Search for 'Foolish' within a string
S = 'Stay Hungry, Stay Foolish'
x = S.find('Foolish')
print(x)
# Prints 18

# Iterate Through a String
# Print each character in a string
S = 'Hello, World!'
for letter in S:
    print(letter, end=' ')
# H e l l o ,   W o r l d !

#Python Escape Sequence

S = "We're open"		# Escape single quote
S = "I said 'Wow!'"		# Escape single quotes
S = 'I said "Wow!"'		# Escape double quotes


S = "Python told me, \"Compliler said, 'This won't work.'\""
print(S)
# Prints Python told me, "Compliler said, 'This won't work.'"

S = str('First line.\n\tSecond line.')
print(S)
# First line.
#     Second line.

#Raw String

S = 'C:\new\text.txt'
print(S)
# C:
# ew	ext.txt

S = r'C:\new\text.txt'
print(S)
# C:\new\text.txt


S = 'ABCDEFGHI'
print(S[2:7])	# CDEFG


S = 'ABCDEFGHI'
print(S[-7:-2])	# CDEFG

S = 'ABCDEFGHI'
print(S[2:-5])	# CD

# Return every 2nd item between position 2 to 7
S = 'ABCDEFGHI'
print(S[2:7:2])	# CEG

# Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3])    # ABC

# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])    # GHI

S = 'ABCDEFGHI'
print(S[::-1])    # IHGFEDCBA