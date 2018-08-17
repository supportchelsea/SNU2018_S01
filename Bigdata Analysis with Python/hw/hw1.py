
# Assignment Number ...... 1
# Student Name ........... 배지원
# File Name .............. hw1_배지원
# Program Description .... 기본적인 자료형과 input함수를 활용하는 과제





season = input('What is your favorite season? ')
    # 좋아하는 계절을 입력받고(input) 그 결과를 season이라는 변수에 할당하였다.

print(season)
    # 사용자가 입력한 계절을 반환하기 위해 print를 함수 사용하여 출력하였다.

date = input('Which date were you born? ')
    # 사용자가 태어난 날짜를 묻고입력(input) 받은 결과(object)를 date라는 변수에 할당하였다.

print(type(date))
    # date 변수의 자료형을 출력하기 위해 type함수로 자료의 클래스를 파악하였고,
    # 이를 print 함수로 출력하였다.

print(type(float(date)))
    # date 변수의 자료형을 문자열(string)에서 숫자형(float)으로 변환하기 위해 float함수를 사용하였다.
    # 또한, 변환된 date 변수의 자료형을 print 함수를 통해 출력하였다.

print('My favorite season is',season +'.','I was born on the',date+'th.')
    # 사용자가 좋아하는 계절(season)과 태어난 날짜를 한 문장(date)에 출력하였다.
    # season과 . / date와 th. 사이를 붙이기 위해 +로 결합시켰고 나머지 연결은 ,를 사용해주었다. 
