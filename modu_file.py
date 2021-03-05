#1st exe_code
# import sys
# print(sys.path)

# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())
#
# import sklearn as sk
# print(sk.__version__)
#
# import modu_file2 as md
# print(md.a) #Best way to import a file
# md.function1(" This is a module:")

#or we can write it but it can b create ambiguity.
# from modu_file2 import a
# print(a)


######

import modu_file2
print(modu_file2.add(5, 8))