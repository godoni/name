import random
import time
print('welcome to the game')
a=input('참가하면 o 아니면 x')
if a=='x':
    print('수고하셨습니다')
elif a =='o':
    print('게임 시작')
    back_num=random.randint(1,456)
    print('당신의 등번호는',back_num,'입니다')
    print('첫번째 게임에 오신걸 환영합니다')
    start=time.time()
    b=input('10초를 세고 누르세요')
    end=time.time()
    print(end-start)
    if end-start >= 9 and end-start <= 11:
        print('통과하셨습니다')
        data=["creater's",'birthday','is','october','twenty sixth']
        word=data[random.randint(0,4)]
        print(word)
        start=time.time()
        player=input('주어진 시간안에 주어진 단어를 입력하시오')
        end=time.time()
        print(end-start)
        if word==player and end-start<=5:
            print('통과하셨습니다')
            print('가위바위보 게임을 시작합니다')
            point=0
            while point != 3 and point != -3:
                player=input('무엇을 내시겠습니까?')
                option=['가위','바위','보']
                com=option[int(random.random()*3)]
                if player==com:
                    point=point+1
                    print('이김')
                    print(point)
                elif (player=='가위' and com=='바위') or (player=='바위' and com=='보') or (player=='보' and com=='가위'):
                    point=point-1
                    print('짐')
                    print(point)
                else:
                    point=point
                    print('비김')
                    print(point)
            if point==3:
                print('통과하셨습니다')
                num=int(random.random()*2)+1
                choice=input('홀 아니면 짝')
                if (choice=='홀' and num==1) or (choice=='짝' and num==2):
                    print('통과하셨습니다')
                    life = 3
                    bridge = []
                    print('이번 게임은 징검다리다 입니다. 0 또는 1 을 입력하여 5번 연속으로 3번의 기회 안에 통과하시오.')
                    for i in range(5):
                        bridge.append(int(random.random()*2))
                    while True:
                        if life == 0:
                            print('아쉽게도 목숨을 다 써버렸네요 끝..잘가요')
                            break
        
                        num1 = int(input('첫 번째 숫자를 입력해주세요: '))
                        if num1 != bridge[0]:
                            life = life - 1
                            print('틀렸네요 !!!')
                            continue
                        
                        num2 = int(input('두 번째 숫자를 입력해주세요: '))
                        if num2 != bridge[1]:
                            life = life - 1
                            print('틀렸네요 !!!')
                            continue

                        num3 = int(input('세 번째 숫자를 입력해주세요: '))
                        if num3 != bridge[2]:
                            life = life - 1
                            print('틀렸네요 !!!')
                            continue
                        
                        num4 = int(input('네 번째 숫자를 입력해주세요: '))
                        if num4 != bridge[3]:
                            life = life - 1
                            print('틀렸네요 !!!')
                            continue

                        num5 = int(input('다섯 번째 숫자를 입력해주세요: '))
                        if num5 != bridge[4]:
                            life = life - 1
                            print('틀렸네요 !!!')
                            continue

                        print('통과했습니다!')
                        break
                        print('깐부치킨의 깐부는 오징어게임의 깐부와 똑같은 뜻일가요?, 맞으면 o 틀리면 x')
                        quiz=input()
                        if quiz.lower()=='o':
                            print('정답입니다')
                            print('모든 게임을 통과하셨습니다. 안녕히 가십시오')
                        else:
                            print('탈락입니다')
                            
                else:
                    print('탈락하셨습니다')
            else:
                print('탈락하셨습니다')
        elif word!=player or end-start>5:
            print('탈락하셨습니다')
    else:
        print('탈락하셨습니다')
        
else:
    print('잘못 입력하셨습니다')
