import random
eng = []
kor = []
score = 0
order = 0


for i in range(10):
    eng.append(input("단어 입력 : "))
    kor.append(input("뜻 입력 : "))

print("단를 10개 입력했습니다\n이제 시험 시작")

while len(eng) > 0:
    order = random.randint(0, len(eng) - 1)
    if eng[order] == input(f"{kor[order]}은/는 영어로 무엇인가요? : "):
        eng.pop(order)
        kor.pop(order)
        print("정답")
    else:
        print("틀림")
    score += 1

if score == 10:
    print("대단해")
