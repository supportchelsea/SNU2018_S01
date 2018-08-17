# 소수 판별
while True:
    try:
        condition = True
        prime_fact = []
        in_value = int(input('임의의 양의 정수를 입력하세요: '))
        if  (in_value > 1 and type(in_value)==int) :
            for divide in range(2,in_value):
                if in_value%divide==0:
                    prime_fact.append(divide)
                    condition = False
            if condition:
                print('이 숫자는 소수입니다.')
                break
                
            else:
                print('{}x{}={}'.format(prime_fact[0],prime_fact[-1],in_value))
                print('이 숫자는 소수가 아닙니다.')
                print('{}의 소인수는 {}입니다.'.format(in_value,prime_fact))
                break
        else:
            raise ValueError

    except ValueError:
            print('ValueError:1보다 큰 양의 정수를 입력하세요.')
