"""
== - value equality-->Two objects have the same values
is - reference equality -->two refernce refers to the same object

"""
"""
>>> a=[7,8,9]
>>> b=a
>>> b==a
True
>>> b is a
True
>>> c=a[:]
>>> b==c
True
>>> a==c
True
>>> cis a
  File "<stdin>", line 1
    cis a
        ^
SyntaxError: invalid syntax
>>> c is a
False
"""