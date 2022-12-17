import random
n = []
 

for i in range(10):
    n.append(random.randint(1, 100))


running = True
count = 0
while running:
    move = 0
    for i in range(len(n)-1): 
        if n[i] < n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            move += 1
            count += 1
        if move == 0:
            running = False
print(n, f"\n정렬 횟수 : {count}")
print(n)