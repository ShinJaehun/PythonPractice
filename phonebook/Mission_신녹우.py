book = []

class contact: #contact 클래스 정의
    name = ''
    number = ''

def add(): #연락처를 추가할 함수 생성
    print('추가할 연락처를 입력하세요.\n')
    c = contact()
    c.name = input('name : ')
    c.number =  input('number : ')
    book.append(c)
    print(' 연락처가 추가되었습니다.\n')

def delete(): #연락처를 삭제할 함수 생성
    print('삭제할 이름을 입력하세요.\n')
    delete_name = input('name : ')
    
    find_error = False #비교가 끝났을때 입력한 연락처가 book에 있는지 확인
    for i in book: #비교
        if i.name == delete_name:
            del book[book.index(i)]
            find_error = True

    if find_error == False:
        print('그런 이름은 없어요.')
    else:
        print('자료가 삭제되었습니다.')

def printbook(): #결과값을 출력할 함수 생성
    for i in book:
        print('이름:' + i.name)
        print('전화번호:' + i.number)
        print('----------------')

def modify():
    print('수정할 연락처의 이름을 입력하세요.')
    modify_name = input('name:')
    find_error = False
    for i in book:
        if i.name == modify_name:
            print('대신 넣을 연락처를 입력하세요.')
            i.name = input('name:')
            i.number = input('number:')
            find_error = True
    if find_error == False:
        print('그런 이름은 없어요.')

def read_file():
    print('연락처에 입력할 파일을 입력하세요.')
    try:
        f = open(input('파일 주소:'),'r')
    except IOError:
        print("ERROR : 파일을 열 수 없어요.")
    else:

        new_file = f.read()

        new_lst = new_file.split("\n")
        for i in new_lst:
            if new_lst.index(i) % 2 == 0:
                c = contact()
                c.name = i
                c.number = new_lst[new_lst.index(i)+1]
                book.append(c)
        print('연락처가 추가되었습니다.')
        f.close()

def write_file():
    print('연락처를 저장할 파일의 이름을 입력하세요.')
    try:
        f = open(input('파일 이름:'), 'w')
    except IOError:
        print("ERROR : 파일을 열 수 없어요.")
    else:
        for i in book:
            f.write(i.name)
            f.write('\n')
            f.write(i.number)
            f.write('\n')
        f.close()


while True:
    print ('1.연락처 추가\n2.연락처 삭제\n3.연락처 수정\n4.연락처 전체 출력\n5.종료\n6.파일로 연락처 추가\n7.연락처 파일 생성\n8.전부 지우기')
    try:
        command=  input('실행할 명령을 입력하세요.')
    
        if command == '1':
            add()
        elif command == '2':
            delete()
        elif command == '3':
            modify()
        elif command == '4':
            printbook()
        elif command == '5':
            exit()
        elif command == '6':
            read_file()
        elif command == '7':
            write_file()
        elif command == '8':
            answer = input('전부 다 지우시겠습니까?(y/n)')
            if answer == 'y' or answer == 'Y':
                book = []
                print ('삭제되었습니다.')
            elif answer == 'n' or answer == 'N':
                print('삭제되지 않았습니다.')
            else:
                print('잘못된 입력입니다.')

        else:
            print('잘못된 입력입니다.')
    
    except KeyboardInterrupt:
        print('ERROR : Ctrl + C')