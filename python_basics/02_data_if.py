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
    if bad_words == 0:
        print("맞아.")
    else:
        print("좋은말")

print("잘가.")