import random

def lotto1():

    lotto_numbers = []
    pick = 0
    lotto_picks = []

    for i in range(45):
        lotto_numbers.append(i + 1)

    for j in range(7):
        pick = lotto_numbers.pop(random.randint(0, len(lotto_numbers) - 1))
        lotto_picks.append(pick)


    print(f"이번주 당첨 예상 번호는 {lotto_picks} 입니다.")
