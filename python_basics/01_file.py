f = open("test.txt", "r", encoding = "UTF-8")
print(f.readline())
words = []


for remove in f.readlines():
    words.append(remove.strip())
print(words)
f.close()