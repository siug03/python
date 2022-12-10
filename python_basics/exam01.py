import random


#tool = ["칼", "오함마", "벽돌", "주먹"]
#people = ["코딩쌤", "코딩선생", "코딩선생님", "코딩"]
#place = ["공원", "화장실", "학원", "버스 안"]

#criminal = random.choice(people)
#murder = random.choice(tool)
#scene = random.choice(place)
#print(f"{criminal}(이)가 {scene}에서 {murder}로 사람을 죽였다.")




def deotsem(number):
    sum = 0
    for i in range(number):
        sum += (i + 1)  
    print(sum)
    return sum

