import random
dic = {"snake": 0, "water": 1, "gun": 2}
revdic = {0:"snake",1 :"water",2:"gun"}

score = 0
while True:
    a = input("enter your choice : ")
    answer = dic[a]
    computer = random.choice([0, 1, 2])
    b = revdic[computer]
    print(f"You chose {a}, Computer chose {b}")
    
    if(answer == computer):
        print("It's a draw")
        continue
    else:
        if(answer == 0 and computer == 1):
            print("You won!")
            score +=1
            continue
        elif(answer == 0 and computer == 2):
            print("You lost!")
            print(f"Your final score is : {score}")
            break
        elif(answer == 1 and computer == 0):
            print("You lost!")
            print(f"Your final score is : {score}")
            break
        elif(answer == 1 and computer == 2):
            print("You won!")
            score +=1
            continue
        elif(answer == 2 and computer == 0):
            print("You won!")
            score +=1
            continue
        elif(answer == 2 and computer == 1):
            print("You lost!")
            print(f"Your final score is : {score}")
            break
        