# Assignment Number ...... 7
# Student Name ........... 배지원
# File Name .............. hw7_배지원
# Program Description .... 



def _print(text):
    print(' ________________\n<   I AM GROOT!  |\n \_______________|\n{}'.format(text))

# def를 통해 _print함수를 만들어 그루트의 말풍선을 만든다.
# 여기서 전달인자로 text를 받는다. 그 내용은
# I AM GROOT!라는 문장을 말풍선이 감싸고 있는 형태로
# 이후 추가되는 값이 전달인자로서 작용한다.    
    
print('''
[ 전략게임 : 그루트 키우기 ]

게임 규칙 : 

그루트의 감정 상태 
기쁨 : joy
화남 : angry
즐거움 : funny
짜증 : disgust

(1) 짜증이 +5가 되면 화남이 +1이 증가한다.
(2) 즐거움이 +5 모이면 기쁨이 +1 증가한다.
(3) 화남이 5 이상이 되면 가출을 하며, 게임이 종료된다.
(4) 그루트가 20살이 되면 독립을 하며 게임이 끝난다.

''')

#전략게임 그루트 키우기의 규칙을 print문으로 출력한다.

while True:
    try:
        age = int(input('Groot의 나이를 설정하세요... : '))
        if not isinstance(age,int) or (age >= 15) or (age<=0):
            raise ValueError
        else :
            print('\n~ 그루트가 {}살이 되었습니다. ~\n'.format(age))
            break
    except ValueError:
        print('Groot의 나이는 0보다 크고 15보다 작은 정수여야 합니다.')
# while문을 이용하여 그루트의 나이를 입력받는다.
# 이경우, 나이는 0살부터 15살 안의 숫자만을 받도록
# try, except문을 이용하여 이를 관리한다.
# if not 에 isinstance 를 사용하여 age가 정수인지를 확인 받았고,
# age가 0보다 작은 경우와, 15보다 큰 경우 에러를 발생시켰다.

# 에러가 발생하지 않게 되는 else 상황에서 그루트의 나이를 print문을 통해 출력하고
# break 를 통해 입력을 그만 받는다.

# 또한, except문을 통해 valueerror인 상황에서 그루트 나이에 대한 조건을 출력하므로서
# 유저에게 이에 대해 알려 주고자하였다.

joy = 0
disgust = 0
angry = 0
funny = 0

# 그루트의 감정 상태의 척도인 joy,disgust,angry,funny의 변수를 정의하고
# 이에 대한 값으로 정수를 할당하였다.

while age < 20:
    try:
        situation = int(input
                        ('\n그루트에게 어떤 일과를 시킬까요?\n1. 춤추기\n2. 음악듣기\n3. Language 교육시키기 \n4. 전투하기\n5. 비디오게임하기 \n번호를 입력하세요 => '))
        if not isinstance(situation, int) or not 0 < situation < 6:
            raise ValueError
# while문을 통해 그루트의 나이가 20미만인 경우만 출력한다.
# 또한, try, except 문을 통해 
# 이에 대해 그루트 일과를 명령하는 input을 situation으로 받는다.
# 만약 이러한 입력이 정수형이나, 0과 6사이에 해당하는 값을 받지 않는다면 
# valueerror를 발생시키고 아래 except문에서 다시입력하라는 출력값이 나온다.
# 이것이 참이 될 때까지 받는다.
        age += 1
        # 입력받은 나이에 1을 더해 재할당한다.
        if situation == 1:
            joy += 1
            _print('그루트가 드랙스의 눈을 피해 춤을 춥니다. 기쁨이 1 증가합니다.')
        elif situation == 2:
            disgust += 1
            _print('그루트가 듣는 음악을 스타로드가 따라 부릅니다. 짜증이 1 증가합니다.')
        elif situation == 3:
            angry += 1
            _print('그루트가 빈정거리다 Language 잔소리를 들었습니다. 화남이 1 증가합니다.')
        elif situation == 4:
            funny += 1
            _print('그루트가 추락하는 전투기 옆을 지나며 나무가지 팔로 적들을 공격합니다. 즐거움이 1 증가합니다.')
        elif situation == 5:
            funny += 1
            _print('그루트가 비디오 게임을 합니다. 방임이지만, 즐겁습니다. 즐거움이 1 증가합니다.')
    # 이에 대한 situation값에 따른 조건문으로
    # if elif문을 통해 조건에 따른 sentence를 지정한다.

    # situation이 1의 값을 받았을 때,(춤추기) 
    # 먼저 정의한 말풍선 함수에 그루트가 드랙스의 눈을 피해 춤을 추고, 
    # 기쁨이 1 증가한다는 출력을 실행한다.
    # 또한, 기존 joy에 +1 한 값을 할당한다.

    # situation이 2의 값을 받았을 때, (음악듣기의 경우), 
    # if 문을 통해 그루트의 짜증이 1 증가한다는 출력을 한다
    # 또한, 기존 disgust에 +1 한 값을 할당한다.

    # situation이 3의 값을 받았을 때,(language 교육받기)
    # 그루트의 상태를 직접 정의한 문장이 출력되고,
    # 기존 angry에 +1 한 값을 할당한다.

    # situation이 4의 값을 받았을 때, (전투하기) 
    # 그루트의 상태를 직접 정의한 문장이 출력되고,
    # 기존 funny에 +1 한 값을 할당한다.

    # 마지막으로 situation이 5의 값을 받았을 때,
    # 그루트의 상태를 직접 정의한 말풍선 문장이 출력되고,
    # 기존 funny에 +1 한 값을 할당한다.

        if funny >= 5:
                joy += 1
                print('즐거움이 5가 모여 기쁨이 1 증가합니다.')
                funny -= 5
        if disgust >= 5:
            angry += 1
            print('짜증이 5가 모여 화남이 1 증가합니다.')
            disgust -= 5  
# 게임 규칙에 따라, 각 감정 상태를 치환한다.

# if funny 의 값이 5 이상이 되면
# joy의 기존 값에 +1을 추가한 값을 할당한다.
# 이러한 연산에 대한 이유를 print함수로 출력하고,
# 치환된 값(funny = 5)를 빼준다.

# 마찬가지로,
# if disgust 의 값이 5 이상이 되면
# angry의 기존 값에 +1을 추가한 값을 할당한다.
# 이러한 연산에 대한 이유를 print함수로 출력하고,
# 치환된 값(disgust = 5)를 빼준다.
        if angry >= 5:
            print('\n ~~~ BAD ENDING ~~~\n그루트가 몹시 화가 나, 우주선을 가출합니다. 당신은 더이상 그루트를 보지 못합니다. ;(')
            break
# 또한, 그루트의 감정 상태가 angry 5이상이 되면,
# 그루트가 가출을 하게 되고, break문을 통해 전체 프로그램이 종료된다.
        if 15<age <18 :
            print('\n<WARNING!>그루트가 사춘기가 되었습니다.\n모든 명령에 반항을 합니다.')
            disgust += 3
            _print('당신의 명령에 그루트가 짜증을 냅니다. 짜증 3 증가')
    # 이스터 에그!!
    # 그루트의 사춘기 발생!!

    # if 그루트의 나이가 16살부터 18살 까지가 된다면,
    # 그루트가 사춘기가 되어 모든 명령에 짜증을 낸다.
    # 이를 출력하고, disgust상태에 +3을 더한다.
    # age는 미리 연산되므로 15살 부터 이러한 짜증이 연산이 된다.

        print('\n~ 그루트가 {}살이 되었습니다. ~\n'.format(age))
        print('##### 그루트의 감정상태 #####\n기쁨(joy) : {}\n화남(angry) : {} \n짜증(disgust) : {}\n즐거움(funny) : {}'.format(joy,angry,disgust,funny))
#각 단계가 마무리되면 그루트의 나이에 1이 더해진(윗쪽에서 미리 연산) 나이를 format 메소드를 통해 출력한다.
# 또한, 단계마다 연산된 그루트의 감정상태도 출력한다.
        if age == 20:
            print('''
            ~~~~~ THE END ~~~~~
             _______________
            < WE ARE GROOT! |
             \______________|

            그루트가 20살이 되었습니다.
            그루트가 당신에게 고마움을 표하며 독립을 합니다.
            ''')
    # 마지막으로,
    # if 그루트의 age가 20살이 된다면, 
    # ending을 보여주고 프로그램이 끝이 나게 된다.
    except ValueError:
        print('ValueError : 다시 입력하세요!')
        # 그루트 일과를 명령하는 input을 situation으로 받는다.
        # 만약 이러한 입력이 정수형이나, 0과 6사이에 해당하는 값을 받지 않는다면 
        # valueerror를 발생시키고 아래 except문에서 다시입력하라는 출력값이 나온다.
