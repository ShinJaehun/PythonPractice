f = open("c:/project/fex/fire.txt")
print("fire.txt")
data = f.readlines()

characters = []
words = []

for i in data:
    words += i.split()
print("단어의 수는 : " + str(len(words)))

for i in words:
    characters += list(i)
print("문자의 수는 : " + str(len(characters)))

print("단어의 평균 글자수는 : " + str(round(len(characters)/len(words), 3)))
f.close()

f = open("c:/project/fex/wheel.txt")
print("wheel.txt")
data = f.readlines()

characters = []
words = []

for i in data:
    words += i.split()
print("단어의 수는 : " + str(len(words)))

for i in words:
    characters += list(i)
print("문자의 수는 : " + str(len(characters)))

print("단어의 평균 글자수는 : " + str(round(len(characters)/len(words), 3)))
f.close()

f = open("c:/project/fex/lever.txt")
print("lever.txt")
data = f.readlines()

characters = []
words = []

for i in data:
    words += i.split()
print("단어의 수는 : " + str(len(words)))

for i in words:
    characters += list(i)
print("문자의 수는 : " + str(len(characters)))

print("단어의 평균 글자수는 : " + str(round(len(characters)/len(words), 3)))
f.close()

f = open("c:/project/fex/agriculture.txt")
print("agriculture.txt")
data = f.readlines()

characters = []
words = []

for i in data:
    words += i.split()
print("단어의 수는 : " + str(len(words)))

for i in words:
    characters += list(i)
print("문자의 수는 : " + str(len(characters)))

print("단어의 평균 글자수는 : " + str(round(len(characters)/len(words), 3)))
f.close()

f = open("c:/project/fex/earthware.txt")
print("earthware.txt")
data = f.readlines()

characters = []
words = []

for i in data:
    words += i.split()
print("단어의 수는 : " + str(len(words)))

for i in words:
    characters += list(i)
print("문자의 수는 : " + str(len(characters)))

print("단어의 평균 글자수는 : " + str(round(len(characters)/len(words), 3)))
f.close()

civilization = ""
f = open("c:/project/fex/fire.txt")
civilization += f.read()
civilization += '\n'
f.close()

f = open("c:/project/fex/wheel.txt")
civilization += f.read()
civilization += '\n'
f.close()

f = open("c:/project/fex/lever.txt")
civilization += f.read()
civilization += '\n'
f.close()

f = open("c:/project/fex/agriculture.txt")
civilization += f.read()
civilization += '\n'
f.close()

f = open("c:/project/fex/earthware.txt")
civilization += f.read()
civilization += '\n'
f.close()

f = open("c:/project/fex/civilization.txt", "w")

f.write(civilization)
f.close()