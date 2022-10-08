import random

def future():

    outfit = ["키가 큰", "잘생긴", "뚱뚱한", "멋진"]
    gender = ["남자", "여자"]
    age = 0
    name = 0

    name = input("니이름 입력 : ")
    print(f"{name}의 미래 여친")

    print(f"당신의 배후자는 {random.choice(outfit)} {random.choice(gender)} 모습입니다. 나이는 {random.randint(19, 75)}살 정도로 추정")

future()