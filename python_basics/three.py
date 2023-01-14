name = 0
name3 = []
namein = 0
name = input("세글자 입력 : ")
def sam():
    for word in name:
        namein = input(f"word : ")
        while True:
            if word == namein[0]:
                name3.append(namein)
                break
            else:
                    print("다시")
    print("*" * 20)
    print(f"{name}")
    for n in range(len(name)):
        print(f"{name[n]} : {name3[n]}")
    print("*" * 20)
    return name3
f = open("event.txt", "a", encoding = "UTF-8")
for word in sam():
    f.write(word + "\n")
f.close()
