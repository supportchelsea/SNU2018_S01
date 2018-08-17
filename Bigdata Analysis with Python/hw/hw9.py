# Assignment Number ...... 9
# Student Name ........... 배지원
# File Name .............. hw9_배지원
# Program Description .... (1) open함수를 이용하여 csv를 불러오고,for문을 통해 이를 출력한다.
# ........................ (2) csv파일을 파싱하고, 행마다 콤마를 기준으로 나누어 리스트 내부에 튜플을 위치시킨다.
# ........................ (3) open함수를 이용하여 txt를 불러오고,for문을 통해 이를 출력한다.
# ........................ (4) file모드를 달리하여 각 값을 리스트 요소로 저장하고,
# ........................      할당받은 리스트 내 3번째 위치 반환,문장을 추가하고 전체 파일을 출력해본다.


# 1
file = open('cars.csv',mode='r',encoding='utf-8')
    # open함수를 이용하여 cars.csv파일을 불러온다.
    # 읽는 모드로 불러들어 이를 읽고, 한글이 있을 수 있기때문에 utf-8로 인코딩해준다,

for line in file:
    print(line)
    # for문을 사용하여 파일의 각 줄을 출력한다.
    # 각각 다른 print함수로 진행되기 때문에 문장 줄바꿈이 이루어져 출력된다.

file.close()
    # 파일을 닫는다.





# 2
file = open('cars.csv',mode='r',encoding='utf-8')
alist = []
    # open함수를 이용하여 cars.csv파일을 읽어온다.
    # 리스트생성자를 통해 향후 튜플을 저장할 리스트를 생성한다.

for i in file:
    alist.append(tuple(i.split(',')))
    # for문을 이용하여 i에 file요소를 할당한다.
    # alist.append를 통해 각 행을 가진 튜플을 할당하는데,
    # 문자열 메소드인 split를 통해 구분자를 ','로 정해준다.

file.close()
print(alist)
    # 마지막으로 파일을 닫고, alist를 출력하면 된다.


# 3

with open('My way.txt') as file:
    # open함수를 통해 My way.txt파일을 읽어온다.
    # 이때, with함수를 사용하여 as file이라는 변수에 할당한다.
    
    lines = file.readlines()
    
    # file.readlines라는 함수를 통해
    # 각 줄을 리스트로 받는다.
    # 이에 대해서 프린트를 바로 적용하게 되면
    # ['And now, the end is near\n', 
    # 'And so I face the final curtain\n', 
    # "My friend, I'll say it clear"] 식의 리스트로 출력이 된다.
    
    # 때문에 for문을 통해 각 요소를 출력하고자 하였다.
    
    for line in lines:
    # 해당 문제는 각 문장마다 줄바꿈이 이루어 지되,
    # 마지막 문장에 대한 줄바꿈은 이루어지지 않는다.
    
    # lines의 경우, readlines로 만들었기 떄문에 
    # 마지막 요소를 제외하고 \n으로 분리되어 있다.
    # 때문에 특별한 조치 없이 이를 print하여도 
    # 보기와 같은 결과가 도출된다.
    
        print(line)
    file.close()


# 4
file = open('My way.txt',mode='r',encoding='utf-8')
f = file.read().splitlines()
print(f[2])
file.close()
    # open함수를 통해 My way.txt파일을 읽어온다. (read모드)
    # 각 행의 내용을 하나의 리스트 요소로 저장하기 위해 
    # splitlines()를 사용하였다.
    # splitlines()의 경우, 값을 리스트로 반환하기 때문에
    # 추가적으로 리스트화할 필요가 없다,
    # 따라서, 할당받은 f에서 3번째 위치인 f[2]를 프린트하면 된다. 

file = open('My way.txt',mode='a',encoding='utf-8')
file.write("\nI'll state my case, of which I'm certain")
file.close()
    # append를 위한 a 모드로 file을 open하였다.
    # 이에 추가하고자하는 문구를 file.write함수를 통해 입력하였고,
    # 앞부분에 대한 줄바꿈이 고려되어있지 않아 줄바꿈 연산을 추가하였다.

file = open('My way.txt',encoding='utf-8')
print(file.read())
file.close()

    # 앞서 추가변경한 파일을 열고 이를 file.read()함수와
    # print함수를 통해 인쇄하고 이를 닫았다.
