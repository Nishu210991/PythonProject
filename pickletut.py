import pickle
#Pickiling a python object-->It is used for storing the data

# Phones= ["OnePlus", "Apple", "Readme", "Motorola"]
# file="myphone.pkl"
# fileobj=open(file, 'wb')  #it should be open in wb(write and binary) format
# pickle.dump(Phones, fileobj)
# fileobj.close()

#pickling unpacking

file= "myphone.pkl"
fileobj=open(file,'rb')
myphone=pickle.load(fileobj)
print(myphone)
print(type(myphone))