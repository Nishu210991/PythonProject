#only one time sleep method run.after that it will start from the while loop..no delay in executing the program.

def seacher():
    import time
    #Taking 4 sec Task
    Book="This is a book.This book content is related to women's empowerment. "
    time.sleep(4)  #coroutine Started

    while(True):
        text =(yield ) #seacher is using as coroutine by yield
        if text in Book:
            print("Your content is in the Book")
        else:
            print("Your content is not in the Book")

search=seacher()
next(search)
search.send("Nishu")
input("Next method run")
search.send("This is")
input("Press any Key")
search.send("This ")
input("Press any Key")
search.send("Beautiful")

search.close()
#search.send("This is") #after closeing statement we can not be pass the value.it will occur an error.

