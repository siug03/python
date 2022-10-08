
import random

rcp = ["가위", "바위", "보"]
user = 0
computer = 0

def result_show(who):
    if who == 1:
        return "비겼네"
    elif who == 2:
        return "이겼네"
    elif who == 3:
        return "졌네"
user =  input("우리 게임ㅁ하자 : ")
computer = rcp[random.randint(0, 2)]
computer = random.choice(rcp)
result = 0



def result_show(who):
    if who == 1:
        return "비겼네"
    elif who == 2:
        return "이겼네"
    elif who == 3:
        return "졌네"

if user == computer:
    result = 1
elif user == "가위":
    if computer == "보":
        result = 2
    else:
        result = 3

elif user == "바위":
    if computer == "가위":
        result = 2
    else:
        result = 3
elif user == "보":
    if computer == "바위":
        result = 2
    else:
        result = 3

print(f"유져 : {user}, 컴퓨터 : {computer} ==> {result_show(result)}")























