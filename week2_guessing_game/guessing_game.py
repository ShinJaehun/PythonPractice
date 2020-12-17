import random


win = random.sample(range(1, 16),5)#당첨 번호 할당
you = []
result = []

while True:
    for i in range(5):
        num = input("1부터 15까지 숫자를 입력하세요 : ")
        if int(num) > 15 or int(num) < 1:
            print("잘못된 입력입니다.")
            exit()
        else:
            you.append(num) #you에 플레이어의 입력 할당

    bb = 0 #당첨번호와 you를 비교해 맞은 개수를 넣을 변수 입력
    for i in win:
        for n in you:
            if i == int(n):
                bb += 1 #당첨 번호와 you를 비교해 맞은 개수를 bb에 입력


    com_1 = random.sample(range(1, 16),5) #컴퓨터들의 숫자 할당
    com_2 = random.sample(range(1, 16),5)
    com_3 = random.sample(range(1, 16),5)
    com_4 = random.sample(range(1, 16),5)
    com_5 = random.sample(range(1, 16),5)
    com_6 = random.sample(range(1, 16),5)
    com_7 = random.sample(range(1, 16),5)
    com_8 = random.sample(range(1, 16),5)
    com_9 = random.sample(range(1, 16),5)

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0 #컴퓨터들과 당첨번호를 비교해 맞은 개수를 넣을 변수 입력

    for i in win:
        for n in com_1:
            if i == n:
                c1 += 1 #컴퓨터들과 당첨번호를 비교해 각 변수에 입력
    result.append(c1)

    for i in win:
        for n in com_2:
            if i == n:
                c2 += 1
    result.append(c2)

    for i in win:
        for n in com_3:
            if i == n:
                c3 += 1
    result.append(c3)
                
    for i in win:
        for n in com_4:
            if i == n:
                c4 += 1
    result.append(c4)
                
    for i in win:
        for n in com_5:
            if i == n:
                c5 += 1
    result.append(c5)

    for i in win:
        for n in com_6:
            if i == n:
                c6 += 1
    result.append(c6)

    for i in win:
        for n in com_7:
            if i == n:
                c7 += 1
    result.append(c7)

    for i in win:
        for n in com_8:
            if i == n:
                c8 += 1
    result.append(c8)

    for i in win:
        for n in com_9:
            if i == n:
                c9 += 1
    result.append(c9)

        
    print("당첨번호:" + str(win) )#나온 변수들로 화면에 출력
    print("당신의 숫자:" + str(you) + " 맞힌 개수:" + str(bb))
    print ("com_1의 숫자:" + str(com_1) + " 맟힌 개수:" + str(c1))
    print ("com_2의 숫자:" + str(com_2) + " 맟힌 개수:" + str(c2))
    print ("com_3의 숫자:" + str(com_3) + " 맟힌 개수:" + str(c3))
    print ("com_4의 숫자:" + str(com_4) + " 맟힌 개수:" + str(c4))
    print ("com_5의 숫자:" + str(com_5) + " 맟힌 개수:" + str(c5))
    print ("com_6의 숫자:" + str(com_6) + " 맟힌 개수:" + str(c6))
    print ("com_7의 숫자:" + str(com_7) + " 맟힌 개수:" + str(c7))
    print ("com_8의 숫자:" + str(com_8) + " 맟힌 개수:" + str(c8))
    print ("com_9의 숫자:" + str(com_9) + " 맟힌 개수:" + str(c9))


    ranking = 1#플레이어의 순위를 셀 변수 만들기

    for i in result:#컴퓨터들과 플레이어의 맞힌 개수를 비교하여 순위를 정함
        if i > bb:
            ranking += 1

    print ("당신은" + str(ranking)+ "등!")#플레이어의 순위를 화면에 출력

    ans = input("다시 하겠습니까?(Y/N) : ")

    if ans == 'y' or ans == 'Y':
        continue
    elif ans == 'n' or ans == 'N':
        break


