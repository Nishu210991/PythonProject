"""
Iterable--  __iter__() or __getitem__()
Iterator--  __next__
Iteration-process of iterator is called Iteration

"""
def gen(n):
    for i in range(n):
        yield i #Tyoe of generator , working on the fly.

# g=gen(325454545)
# print(g)

g=gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())  # Throw error because g value is 3. but in for loop it handle automaticaly.

for i in g:
    print(i)  # Dont throw error bcz in for loop it handle automaticaly.

N= "Nishu" # Iterators use in string not in integer
# for c in N:
#     print(c)
nis= iter(N)
print(nis.__next__())
print(nis.__next__())
print(nis.__next__())
print(nis.__next__())


