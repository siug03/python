import random

a = ["가위", "바위", "보"]
computer = 0
user = 0


user = input("가위바위보")


computer = random.choice(a)
if computer == user:
        print("비김")

elif user == "가위":
        if computer == "바위":
            print("컴승")

elif user == "가위":
        if computer == "보":
            print("니가 이김")
 

elif user == "바위":
        if computer == "보":
            print("컴승")

elif user == "바위":
        if computer == "가위":
            print("니가 이김")

    
elif user == "보":
        if computer == "가위":
            print("컴승")
elif user == "보":
        if computer == "바위":
            print("니가 이김")

    



    

    