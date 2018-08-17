
# Assignment Number ...... 6
# Student Name ........... 배지원
# File Name .............. hw6_배지원
# Program Description .... (1) date 모듈을 이용하여 현재시간을 출력
# ........................ (2) calendar몯ㅍㄹ을 불러와 현재시간을 출력
# ........................ (3) colletions모듈을 사용하여 문장 내 모음의 갯수를 세고,
#                              가장 많은 갯수를 가지는 모음을 대문자로 바꾸는 함수를 생성

# 1. datetime 모듈 사용하기

import datetime
# import 함수를 사용하여 datetime모듈을 불러오기

now = datetime.datetime.now()
# datetime의 하위노드인 datetime의 now라는 함수 사용을 위해서 점(.)으로 접근한다.

print(now.strftime("%Y-%m-%d %H:%M:%S"))
# 정의한 now 변수에 strftime 메소드를 사용하여 시간표현의 형식을 정의하고 출력한다.


# 2. calendar모듈 사용하기

import calendar 
    # import 함수를 calendar모듈을 불러오기 (함수 사용을 위해 점.으로 접근해야한다.)

print(calendar.isleap(2050)) 
    # calendar 모듈에서 isleap이라는 윤년 판별 함수를 가지고 전달인자인 2050년이 윤년인지 확인하였다.
    # 이에 대한 출력값은 논리연산으로 받게 되며 FALSE가 출력되었기 때문에 윤년이 아님을 알 수 있다.

print(calendar.weekday(2050,7,7)) 
    # weekday함수를 이용하여 2050년 7월7일이 무슨 요일인지 도출하였다.
    # 값은 3이 도출되므로 목요일이다.

# 3

import collections
    # collections 모듈을 import한다.

def _print(i,j):
    print('The number of {} : {}'.format(i,j))
# 함수를 만들기 이전 함수 내부에서 사용할 _print라는 함수를 def를 통해 생성한다.
# 이에 대한 내용은 중복되는 문장에 대한 출력문이다.

def vowel(x):
    count_x = collections.Counter(x)
    vowel_list = list('aeiou')
    x_dict = {'a':[],'e':[],'i':[],'o':[],'u':[]}
    # vowel에 대해 정의하였다.
    # 먼저 count_x 라는 변수를 collections.Counter(x)를 통해 생성하였는데, 
    # 이는 함수의 전달인자를 대상으로 각각의 요소의 개수를 세는 딕셔너리를 생성하는 것이다.
    # 여기서의 key는 spell이 될것이고, value는 그에 대한 갯수이다.

    # 또한, 향후 for문에서 받을 vowel_list를 정해주어 각 모음에 대해 정의하였고,
    # count한 갯수를 할당할 딕셔너리인 x_dict을 생성하였다. 
    # 이에 대한 key는 각 모음의 요소이고, 값은 빈리스트로 할당하여 값을 나중에 받도록 하였다.
    
    for i in vowel_list:
        _print(i,count_x[i])
        x_dict[i] = count_x[i]
    # for문을 통해 i에 vowel_list순서대로 입력하였다.
    # 그리고 먼저 정의한 함수인 _print를 통해 vowel_list와 count_x[i]를 출력하였다.
    # i는 vowel_list의 요소로 aeiou값이고,
    # count_x[i]는 vowel_list의 요소로 키 값을 받아 접근하였다.
    # 그렇게 하여, count_x에 존재하지 않는 모음에 대해서도 출력할 수 있게 하였다.
    
    # 또한, x_dict의 key가 i(즉, vowel_list의 요소값)일때 value를 count_x의 key가 i일때의 Value로 받았다.
    # 이는 모음의 갯수를 할당한 것이다.

    x_dict = sorted(x_dict.items(), key=lambda t : t[1],reverse=True)
    larger = x_dict[0][0]
    x = x.replace(larger,larger.upper())
    print(x)
    
    # 앞서 받게된 x_dict.items들을 람다와 sorted함수를 이용하여 리스트로 받아 정렬하였다.
    # 원래는 key값을 기준으로 정렬이 되기 때문에 람다함수를 이용하여 [1]번째 값인 value로 지정하겠다고 설정하였다.
    # 또한, 기본값은 오름차순으로 정렬이 되기 때문에 값이 가장 많은 값을 첫번째로 받기 위해, reversed를 True로 놓았다.

    # x_dict[0][0]을 통해서 리스트의 첫번째 요소인 (키,값)의 튜플에서 첫번째 위치한 키를 뽑아 larger라는 변수에 할당하였다.
    # larger값을 larger의 대문자 값으로 받기 위해, 문자열 메소드인 .replace를 이용하였다.
    # 즉, x.replace(larger,larger.upper())를 통해 기존 값을 대문자로 변환하였고, 이를 다시 x에 재할당하였다.
    
    # 재할당받은 x를 출력한다.

vowel('The regret after not doing something is bigger than that of doing something.')
