# Assignment Number ...... 10
# Student Name ........... 배지원
# File Name .............. hw10_배지원
# Program Description .... < 파일 처리 >
# ........................ 파일을 읽고 리스트 변수에 할당한다. 열의 이름을 key로,
# ........................ 내용을 value로 하는 딕셔너리를 각 행마다 생성하고,
# ........................ 이에 대한 딕셔너리 값을 가지는 리스트 변수 정의 후 
# ........................ 조건에 해당하는 정보에 접근하도록 한다.

subway_data = []

with open('subway.txt',encoding='utf-8-sig') as file:
    lines = file.readlines()
        # file에 대한 readlines를 실시하여,각 행을 문자열 자료형 값으로 가지는 리스트를 생성하였다.
        # with 를 이용하였기 때문에 file이 자동적으로 닫히게 되므로 close를 할 필요가 없다.
        
    datas = []
        # 이러한 lines의 element는 마지막 요소로 \n 줄바꿈 연산자를 가지고 있다.
        # 이를 삭제하고, 새로운 리스트 형태로 받기 위하여 새로운 빈리스트인 datas를 생성하였다.
        
    for line in lines:
        datas.append(line[:-1])
        # line을 각행마다 받기위해 for 문을 이용하였고,
        # 빈리스트인 datas에 각 행의 마지막 요소를 제거한 line[:-1] 값을 append하였다.

    keys = datas[0].split(',')
        # datas의 첫번째 요소는 header이기 때문에 이를 key로 저장하였다.
        # 이를 할당하기 전, split(',')를 실시하여 항목 사이 구분을 ','로 이루었다.
    
    values = []
        # 또한, 나머지 값에 대한 리스트를 생성하기 위해 values라는 빈 리스트를 생성하였다.
        
    for i in range(1,len(datas)):
        values.append(datas[i].split(','))
        # 이를 위해 for문을 사용하였다.
        # datas의 첫번째 요소인 header는 key값으로 활용하여야 하기 때문에
        # range(1,len(datas))를 하여 첫번째 행부터 값을 받았다.
        # 이를 values에 append하기 전 split(',')를 실시하여 항목 사이 구분을 ','로 이루었다.
    
    for irr in values:
        data=dict()
        for index,key in enumerate(keys):
            data[key] = irr[index]
        subway_data.append(data)
        # 이렇게 정의된 value값에 대해 각 행마다 dictionary를 구축하고자 하였다.
        # 먼저 각 행인 모든 values에 대한 시행을 위해 for 문을 활용하였고,
        # 이를 받을 딕셔너리를 data라 설정하였다.
        
        # 앞서 for를 통해 받게 된 하나의 행에 대해 
        # enumerate문을 활용하여 key의 위치와 값을 반환받았다.
        # data에 key라는 키 값을 만들고, 이에 대해 irr[index]하였다.
        # key의 인덱스는 각행인 irr에서의 위치와 부합하기 때문이다.
        
        # 이렇게 정의된 data라는 여러 딕셔너리 값에 대해 subway_data라는 리스트 변수에 할당하였다.




# 출력 1
print("="*20,'테스트 1',"="*20)
print('목요일의 하차 정보만 모은 목록')

alist = []
for i in subway_data:
    if i['요일'] == '목' :
        alist.append(i)    
print(alist)

    # 목요일의 하차 정보만 모은 목록을 생성하고 이를 출력하기 위해
    # 먼저 빈리스트인 alist 를 생성하였다.

    # for문을 통해 모든 subway_data의 요소(각 행의 dict)별로 반복하여 확인하고자 하였다.
    # if 만약 key값이 요일일 경우 i의 value가 '목'요일 이라면
    # alist에 딕셔너리 자체를 append하여 모든 정보를 제공하고자 하였다.

    # 이에 대한 alist를 출력하면 목요일의 하차 정보만 모은 목록이 완성된다.




# 출력 2
print("="*20,'테스트 2',"="*20)
print('8시에서 9시 승차 인원이 1500명 이상인 날짜의 목록')
blist = []

for i in subway_data:
    if int(i['8']) >= 1500 and i['구분']== '승차':
        blist.append(i['날짜'])
print(blist)

    # 8시에서 9시 승차 인원이 1500명 이상인 날짜의 목록을 생성하고 이를 출력하기 위해
    # 먼저 빈리스트인 blist 를 생성하였다.

    # for문을 통해 모든 subway_data의 요소(각 행의 dict)별로 반복하여 확인하고자 하였다.
    # if key값이 8일때, (8시부터 9시 승차혹은 하차 경우) 이를 int로 치환하여,
    # 그 value가 1500 이상인 경우를 조건으로 걸었다.

    # 또한, 이러한 경우는 승차만 해당하기 때문에 i['구분']== '승차'라는 조건을 and로 걸어
    # 8시에서 9시 승차 인원이 1500명 이상인  경우를 알고자 하였다.

    # 이때 딕셔너리 i에 대한 날짜만 받고 싶기 때문에
    # blist에 i의 key 값이 날짜인 value만 받아 append하도록 하였다.

    # 이에 대한 blist를 출력하면 8시에서 9시 승차 인원이 1500명 이상인 날짜의 목록이 완성된다.



# 출력 3
print("="*20,'테스트 3',"="*20)
print('날짜가 3의 배수인 날짜 중 7시에서 8시 승차 인원은 짝수인 날들의 정보를 모은 목록')
clist = []

for i in subway_data:
    if int(i['7'])%2==0 and i['구분']=='승차' and int(i['날짜'])%3==0:
        clist.append(i)
print(clist)


    # 날짜가 3의 배수인 날짜 중 7시에서 8시 승차 인원은 짝수인 날들의 정보를 모은 목록을 생성하고 이를 출력하기 위해
    # 먼저 빈리스트인 clist 를 생성하였다.

    # for문을 통해 모든 subway_data의 요소(각 행의 dict)별로 반복하여 확인하고자 하였다.
    # 이에 대해 세가지의 조건을 동시에 만족하는 경우에만 clist에 i를 append하도록 하였다.

    # 이때의 조건은 
        # 1. int(i['7'])%2==0  ~> 7시에서 8시 사이 승차 혹은 하차를 하여야 하고, 이에 대한 인원이 짝수로 나누어 떨어져야 한다.
        # 2. i['구분']=='승차' ~> key값이 구분일때 , 그 value값이 승차인 경우를 동시에 만족해야 한다. 
        # 3. int(i['날짜'])%3==0 ~> 마지막으로, 날짜가 3의 배수임을 만족해야 한다.

    # 이에 대한 clist를 출력하면 날짜가 3의 배수인 날짜 중 7시에서 8시 승차 인원은 짝수인 날들의 정보를 모은 목록이 완성된다.
