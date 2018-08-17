
# Assignment Number ...... 2
# Student Name ........... 배지원
# File Name .............. hw2_배지원
# Program Description .... 문자열(str) 자료형의 변수를 생성하고 슬라이싱(slice)하는 과제
# ........................ 문자열 이스케이프 활용하여, 하나의 print 함수만으로 여러 줄의 텍스트 출력






cellphone = 'Samsung Galaxy6'
print(cellphone)
    # 1
    #   cellphone 변수를 선언하고,
    #   이에 대한 문자열의 값을 입력하였다.
    #   이에 대한 변수값을 print함수로 출력하였다.

    #   type(cellphone) 함수를 통해 확인한다면
    #   cellphone의 형태가 문자열임을 알 수 있다.

company = cellphone.split()[0]
    # 2 - (a)
    #   cellphone 문자열 변수를 슬라이싱해 새로운 변수(company)를 만든다.
    #   이를 위해 split 메소드를 사용하였으며,
    #   기본값인 화이트 스페이스를 기준으로 분할하였다.

    #   제조사의 경우, 첫 번째 인덱스, 즉 [0]에 값에 대한 정보가 위치하여 있기 때문에
    #   cellphone.split()[0]의 값을 할당하였다.

print(company)
    #   company 변수를 print 함수를 통해 출력하였다.


    
model = cellphone.split()[1]
    # 2 - (b)
    #   마찬가지로 model변수를 선언함으로서 이를 생성하고,
    #   인덱스 [1]에 위치한 핸드폰의 모델명의 정보를 할당하였다.
    #   이를 위하여 split 메소드를 사용하였다.(화이트 스페이스 기준의 분할로 2 - (a)와 동일하다.)

print(model)
    #   할당된 model 변수를 print 함수를 통해 출력하였다.

print(type(company))
print(type(model))
    # 3
    #   company와 model의 자료형을 type함수를 통해 출력한다.
    #   기본 소스가 되는 cellphone 변수가 문자열 자료형이었기 때문에
    #   company와 model도 문자열 자료형태임을 알 수 있다.

print('It had been that way for days and days.','\n',
'And then, just before the lunch bell rang, he walked into our','\n'+'class room.','\n',
'Stepped through that door white and softly as the snow.')
    # 4
    #문자열 이스케이프(\) 사용하여 print함수 한번 사용으로 출력

        # \n : 문자가 아닌 새 줄바꿈으로 처리
        # \t : 탭 문자 사용
        # \' : 문자의 시작이 아닌 따옴표로 사용 등

    #   이 중 \n을 사용하여 텍스트 제작하였다.
    #   특이한 점은, 문장 간의 사이라고 할 수 있는 2번째와 4번째 줄은 (And ~ 와 Stepped ~)
    #   콤마(,)로 처리하여 문장 간 새 줄바꿈 시 한 칸 들여쓰기를 하였고

    #   줄바뀜이 있으나 문장 시작이 아닌 3번째 줄은 (class room ~ ) 
    #   '\n'와 결합 연산자인 플러스(+)를 사용하여 들여쓰지 않고자 하였다.

