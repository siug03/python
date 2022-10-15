import random
eng = []
kor = []
score = 0
order = 0


for i in range(10):
    eng.append(input("단어 입력 : "))
    kor.append(input("단어 입력 : "))

print("단를 10개 입력했습니다\n이제 시험 시작")

while len(eng) > 0:
    order = random.randint(0, len(eng) + 1)