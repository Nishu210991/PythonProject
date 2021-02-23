import random
i=1
count_comp=0
count_user=0

while i<6:
    game_pointer = ['S', 'W', 'G']
    rand = random.choice(game_pointer)
    print(rand)
    input1 = input("Enter first key word of yours choice:S, W, G")


    if input1=='S' and rand=='G':
        print("Oooopppsss Gun shoot to your Snake","Your Choice:" ,input1,"Computer Choice:", rand)
        count_comp = count_comp + 1
        #i=i+1
        print("You Loss",count_comp)

    elif input1=='S' and rand=='W':
        print("Wooo!!!You won your snake drunk water ", "Your Choice:", input1, "Computer Choice:", rand)
        count_user = count_user + 1
        #i = i + 1
        print("You won", count_user)

    elif input1=='W' and rand=='G':
        print("Wooo! You won gun drown into the water", "Your Choice:", input1, "Computer Choice:", rand)
        count_user = count_user + 1
        #i = i + 1
        print("You won", count_user)

    elif input1=='W' and rand=='S':
        print("Oooopppsss You Loss snake drunk your all water", "Your Choice:", input1, "Computer Choice:", rand)
        count_comp = count_comp + 1
        #i = i + 1
        print("You Loss", count_comp)

    elif input1=='G' and rand=='W':
        print("Oooopppss!! Your Gun drown into the water", "Your Choice:", input1, "Computer Choice:", rand)
        count_comp = count_comp + 1
        #i = i + 1
        print("You Loss", count_comp)

    elif input1 == 'G' and rand == 'S':
        print("Wooo!!! You won Your Gun shoot snake", "Your Choice:", input1, "Computer Choice:", rand)
        count_user = count_user + 1
        #i = i + 1
        print("You Won", count_user)

    elif input1==rand:
        print("Match Tie:Both Guesses are same")
        #i=i+1

    i=i+1

print("Your Game Limit Exceeded\n","You Won:",count_user ,"Computer Won:", count_comp)



