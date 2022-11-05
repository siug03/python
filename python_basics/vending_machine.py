drinks = {"2%" : 1000, "몬스터" : 2000, "빙그레 바나나 우유" : 1200, "닥터 페퍼" : 1500, "칠성 사이다" : 1500}
money = 0
select = 0
choice = 0
income = 0

def display():
    print("*" * 5, "독약 자판기", "*" * 5)
    print(drinks)
    print("*" * 22)
    print(f"잔액 : {money}")
    print("*" * 22)

while True:
    customer = True
    while customer:
        display()
        select = int(input("1. 돈 넣기 / 2. 물건 사기 / 3. 그냥 가기 : "))
        if select == 1:
            money = int(input("금액 입력 : "))
            continue
        elif select == 2:
            display()
            choice = input("상품을 고르시오 : ")
            if money >= drinks[choice]:
                print(f"<{choice}상품 구매 완료")
                income += drinks[choice]
                money = money - drinks[choice]
            else:
                print("잔액 부족")
                break
        elif select == 3:
            print("정말 가실껀가요??")
            if money > 0 :
                print(f"환불 금액 : {money}")
                money = 0
                customer = False
        elif select == 720602:
            print(f"오늘의 수입 : {income}")
            input("부자 되세요")
        else:
            print("틀림")