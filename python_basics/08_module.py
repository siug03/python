from split_04 import *
import fortuneteller_07 as ft
from lotto_06 import lotto1
import random

select = 0


running = True
while running:
    select = int(input('''안녕하세요. 뭐 할까?
1. 계산기   2. 로또번호 추첨기  3. 미래배우자  4. 끝
(위 앱 중에 한개 번호로 골라)'''))

    if select == 4:
        break
    elif select == 1:
       print(myname)
       calculator
    elif select == 3:
        ft.future()
    elif select == 2:
        lotto1()
        

print("주인님 아주 같은 하루 보내세여")