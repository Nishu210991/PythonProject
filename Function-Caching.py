import  time

#Delay in function priting while executing
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     print("Completed..Working again")
#     some_work(2)
#     print("Working Again")

#Alredy Stored in cache usinh lru decoratoors

from functools import lru_cache

@lru_cache(maxsize=30) #3 is size of given argument
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(5)
    some_work(6) #last 3 wrk save bcz max size is 3.
    print("Completed..Working again")
    input()
    some_work(3)
    print("Working Again")