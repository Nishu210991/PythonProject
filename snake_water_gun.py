import random
i=1
count_comp=0
count_user=0

while i<6:
    game_pointer = ['S', 'W', 'G']
    rand = random.choice(game_pointer)
    #print(rand)
    input1 = input("Enter first key word of yours choice:S, W, G")

    if input1==rand:
        count_user = count_user + 1
        print("Congratulations You Won" ,count_user,"Times")
        i=i+1

        #print(count_user)
        

    else:
        count_comp = count_comp + 1
        print("Not Match:Try Again", "Loss", count_comp, "Times")
        i = i + 1


print("Your Game Limit Exceeded\n","You Won:",count_user ,"Computer Won:", count_comp)



