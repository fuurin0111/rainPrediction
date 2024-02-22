import random

rain = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

#定数定義
BIG = 3 #max=9 min=0
SMALL = 3 #max=9-BIG min=0
TIME = 300 #min
SPEED = 5 #max=len(rain[len(rain)-1]) min=0

#変数定義
a = 0
b = []
amount = 0
amount_sp = 0
player_x  = len(rain[len(rain)-1])-1
tentative = []
rain_oth = []

#雨の位置の確定
for i in range(len(rain)):
    for j in range(len(rain[i])):
        a = random.randrange(10) #0から9でランダムに代入
        if a >= 9-BIG:
            rain[i][j] = random.randrange(1,10)*3
        elif a <= SMALL:
            rain[i][j] = random.randrange(1,10)
        else:
            rain[i][j] = random.randrange(1,10)

#歩いた場合のため
rain_oth = rain

#雨の位置の出力(走った場合)
def printer():
    for i in range(len(rain)):
        print(*rain[i])
    print()

#雨の位置の出力(歩いた場合)
def printer1():
    for i in range(len(rain_oth)):
        print(*rain_oth[i])
    print()


# printer()
# printer1()

for i in range(round(TIME/SPEED)):
    b = []
    for j in range(SPEED):
        amount_sp += rain[len(rain)-1][player_x-(1+j)]

    for j in range(len(rain)-1):
        rain[len(rain)-(j+1)] = rain[len(rain)-(j+2)]

    for j in range(len(rain[0])):
        a = random.randrange(10) #0から9でランダムに代入
        if a >= 9-BIG:
            b.append(random.randrange(1,10)*3)
        elif a <= SMALL:
            b.append(random.randrange(1,10))
        else:
            b.append(random.randrange(1,10)*2)
    rain[0] = b

    for j in range(len(rain)):
        tentative = rain[j]
        for k in range(SPEED):
            for l in range(len(tentative)-1):
                tentative[len(tentative)-1+(-1*l)] = tentative[len(tentative)-2+(-1*l)]
            a = random.randrange(10) #0から9でランダムに代入
            if a >= 9-BIG:
                tentative[0] = random.randrange(1,10)*3
            elif a <= SMALL:
                tentative[0] = random.randrange(1,10)
            else:
                tentative[0] = random.randrange(1,10)*2
        rain[j] = tentative
    #printer()

for i in range(TIME):
    b = []
    amount += rain_oth[len(rain_oth)-1][player_x-1]

    for j in range(len(rain_oth)-1):
        rain_oth[len(rain_oth)-(j+1)] = rain_oth[len(rain_oth)-(j+2)]

    for j in range(len(rain_oth[0])):
        a = random.randrange(10) #0から9でランダムに代入
        if a >= 9-BIG:
            b.append(random.randrange(1,10)*3)
        elif a <= SMALL:
            b.append(random.randrange(1,10))
        else:
            b.append(random.randrange(1,10)*2)
    rain_oth[0] = b

    for j in range(len(rain_oth)):
        tentative = rain_oth[j]
        for l in range(len(tentative)-1):
            tentative[len(tentative)-1+(-1*l)] = tentative[len(tentative)-2+(-1*l)]
        a = random.randrange(10) #0から9でランダムに代入
        if a >= 9-BIG:
            tentative[0] = random.randrange(1,10)*3
        elif a <= SMALL:
            tentative[0] = random.randrange(1,10)
        else:
            tentative[0] = random.randrange(1,10)*2
        rain_oth[j] = tentative
    #printer1()

print("体に雨が当たる量")
print(f"歩いた場合{amount}")
print(f"走った場合{amount_sp}")
print(f"走ったほうが良い確率{round((amount/amount_sp)*100,1)}%")