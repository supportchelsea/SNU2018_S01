
# Assignment Number ...... 5
# Student Name ........... 배지원
# File Name .............. hw5_배지원
# Program Description .... (1) if-elif-elif문을 활용하여, 세 정수 값 비교
# ........................ (2) if-elif-elif문과 .format 을 활용하여 입력 받은 도시 이름에 맞는 면적을 출력하는 프로그램 작성
# ........................ (3) for문과 range함수를 사용하여 0부터 9까지 정수의 팩토리얼 출력
# ........................ (4) while문을 활용하여 0부터 9까지 정수의 팩토리얼 출력

#1
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
    # input 함수를 이용하여 3개의 정수 변수를 생성한다.
    # 세 값에 int함수를 적용하여 문자열에서 정수형으로 변환한다.

if a >  b and c :
    print(b+c)
    # if 조건문을 통해 만약 a가 b 와 c 보다 크면(condition)
    # b와 c의 합을 출력(statement)한다라는 조건문을 실행한다.
    # 앞서 a,b,c의 자료형을 정수로 변환하였기 때문에 이와 같은 계산이 가능하다
    # (변환하지 않을 시, 5+11 = 511로 반환)
    # 이와 같은 조건문이 True라면 아래 statement인 print함수가 실행된다.
elif b > a and c :
    print(a+c)
    # 같은 수준에서 elif 문을 통해 b가 a 와 c 보다 크면(condition)
    # a와 c의 합을 출력(statement)한다라는 조건문을 실행한다.
    # 이와 같은 조건문이 True라면 아래 statement인 print함수가 실행된다.    
elif c > a and b:
    print(a+b)
    # 마찬가지로 또 하나의 elif문을 통해 c가 a 와 b 보다 크면(condition)
    # a와 b의 합을 출력(statement)한다라는 조건문을 실행한다.
    # 이와 같은 조건문이 True라면 아래 statement인 print함수가 실행된다.


# 2
recieved = input('Enter the name of the city: ')
city = ['Seoul','New York','Beijing']
# recieved라는 변수에 input함수로 사용자가입력한 값을 할당한다.
# city는 리스트 자료형으로 도시에 대한 이름을 입력한다.

# if elif else문을 통해 size변수에 대한 값을 할당한다.

if recieved == city[0]:
    size = 605
elif recieved == city[1]:
    size = 789
elif recieved == city[2]:
        size = 16808
else :
    size = 'Unknown'
    # if 만약 입력받은 변수와 city변수의 첫번째 element가 같다면 size에 605를 할당한다.
    # elif 만약 입력받은 변수와 city변수의 두번째 element가 같다면 size에 789를 할당한다.
    # elif 만약 입력받은 변수와 city변수의 세번째 element가 같다면 size에 16808를 할당한다.

print('The size of {} is {}'.format(recieved,size))
# print함수를 통해 도출된 출력값은 format메소드를 이용하여 참조하였다.
# 그리하여 첫번째 {}중괄호에는 사용자가 입력한 recieved변수가 출력되고
# 두번째 참조값은 if 문으로 정의한 size에 대한 값이 도출된다.


# 3
import math
# math라이브러리를 import하여 그에 딸린 메소드를 사용할 환경을 만든다.

for i in range(0,10):
    print(math.factorial(i))
    
# 계승값을 만들기 위해 반복문 for와  range함수를 사용한다.
# i 안에 range(0,10) 즉, 0부터10-1인 9까지의 수를 대입할 동안 아래 statement를 진행한다.

# math라이브러리 하에 있는 factorial 메소드를 사용하여 0부터 9까지의 계승값을 구한다.
# 이러한 식을 print함수 안에 넣어 팩토리얼을 출력한다.

# 이를 range(1,10)동안 반복한다.

# 4
i = 0
# 계승값을 만들기 위해 반복문 while을 사용한다.
# while은 주어진 조건을 만족하는 동안 계속 statement가 진행된다.
# 현재 while True로 무한 루프의 프로그램을 만들었기에
# 만족하는 값이 나오게 되면 break문으로 멈춰야 한다.

while True:
    print(math.factorial(i))
    i += 1
    if i == 10:
        break

    # i가 0으로 먼저 선언해 주고
    # while loop가 참인 동안
    # math 라이브러리의 factorial메소드를 활용하여 i의 팩토리얼을 출력한다.

    # 출력이 완료되면 i에 1씩 더한 값으로 바꿔주고
    # i = 10인 경우 break를 걸게 되면 0부터 9까지의 정수의 계승값을 구할 수 있다.
