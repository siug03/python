import random
import os
import time
clear = lambda: os.system('cls')
mode = 0

def word_in():
    kor = open("kor.txt",  "a", encoding = "UTF-8")
    eng = open("eng.txt",  "a", encoding = "UTF-8")
    answer = 0
    in_eng = ""
    in_kor = ""
    while True:
        answer = input("입력a, 끝내기q")
        if answer == "q":
            break
        elif answer == "a":
            in_eng = input("영어단어 입력 : ")
            eng.write(f"{in_eng}\n")
            in_kor = input("한국뜻 입력 : ")
            kor.write(f"{in_kor}\n")

        else:
            print("잘 못했어")
    kor.close()
    eng.close()

def test():
    kor = open("kor.txt",  "r", encoding = "UTF-8")
    eng = open("eng.txt",  "r", encoding = "UTF-8")
    kor_words = []
    eng_words = []


    for r in kor.readlines():
        kor_words.append(r.strip())
    for r in eng.readlines():
        eng_words.append(r.strip())

    questions = ""
    answer =  ""
    for num in range(len(kor_words)):
        questions = kor_words[num]
        clear()
        answer = input(f"{questions} 뜻을 가진 영어 단어는? : ")
        if eng_words[num] == answer:
            print("정답")
        else:
            print("틀림")
        time.sleep(1)
    kor.close()
    eng.close()

while True:
    mode = int(input("1-단어입력 / 2-단어시험 / 3-앱 종료"))
    if mode == 3:
        break
    elif mode == 1:
        word_in()
    elif mode == 2:
        test()