sajeon = {"apple" : "사과", "friend" : "친구", "aori" :"사과"}
print(len(sajeon))


print(sajeon["apple"])
print(sajeon["aori"])
print(sajeon.keys())
print(sajeon.values())
print(sajeon.items())


print("apple" in sajeon)
print("pear" in sajeon)






naver = {"siug03" : ["남자", "지하철", "예봉중"]}

if "siug04" in naver:
    print(naver["siug03"])
else:
    print("요청한 아이디는 없습니다.")

naver["codingsam"] = ["여자", "코드플레이", "자가용"]

print(naver)
sajeon.update(naver)
#del naver["coding3"]
print(naver)

print(sajeon)















