ban_dict = ["개새끼", "십", "ㄴㄱㅁ", "ㅄ" ,"ㅗ"]
status = True

print("챗봇 시작")
while status:
    bad_words = 0
    chat = input("말해 : ")
    for word in ban_dict:
        if word in chat:
            bad_words += 1
    if chat == "꺼져":
        status = False
    if chat == "추가":
        add_word = input("추가 금칙어 말해: ")
        if add_word in ban_dict:
            print(f"{add_word} 단어가 이미 있어")
        else:
            ban_dict.append(add_word)
            print(f"{add_word} 단어가 금칙어 사전에 등록됨")
        continue


            
    if bad_words == 0:
        print("맞아.")
    else:
        print("좋은말")

print("잘가.")