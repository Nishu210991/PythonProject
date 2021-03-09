import  json

# data= '{"Name":"Nishu", "Age":28}'
#
# x =json.loads(data)
# #print(p)
# print(x['Name'])

data2= {
    "channel_name":"scorpians",
    "cars":["Fortuner", "VW", "lamborghini"],
    "friends":("Aanaya", 253, "Aayesha"),
    "isbad":False
}
jscomp=json.dumps(data2)
print(jscomp)