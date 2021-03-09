import re

mystr= '''Nishu is a very good girl 
She is very genius. 
She gets up early in the morning.
Nishu likes to eat momos.
Nishu always ready to go to outside'''

"""----Function----
Findall-->final all specific string matches.
Search-->Returns a Match object if there is a match anywhere in the string.
split-->Returns a list where the string has been split at each match
finditer-->Replaces one or many matches with a string
"""
# pattern=re.compile(r'outside')
# #print(r"\n")
# matches=pattern.finditer(mystr)
# for match in matches:
#     print(match)

#pattern=re.compile(r'.') #. show all matches.It is meta chachter
#pattern=re.compile(r'^Nishu') #string start with Nishu
#pattern=re.compile(r'outside$')
#pattern=re.compile(r'os*')
#pattern=re.compile(r'os+')
pattern=re.compile(r'os{1}')

matches=pattern.finditer(mystr)
for match in matches:
    print(match)

#---Special Sequences
# pattern= re.complie(r'\ANishu')
# matches=pattern.finditer(mystr)
# for match in matches:
#  print(match)


