import sys

data_file = open(sys.argv[1], 'r').read()

#정보파일에서 정보 추출
accel = [] #가속도 리스트

info = data_file.split('\n')

for lines in info:
    if len(lines)>1:
        lines = lines.split('\n')
        accel.append(float(lines[0]))

    

#유효 극값 분리 파트
#극댓값 찾기
extreme= [] #극값 list
extreme_small = [] #극솟값 list
extreme_big = [] #극댓값 list
for i in range(1,len(accel)-1):
    if accel[i]<=accel[i-1] and accel[i]<accel[i+1]:
        extreme_small.append(i)
    if accel[i]>accel[i-1] and accel[i]>=accel[i+1]: 
        extreme_big.append(i)

if extreme_small[0]<extreme_small[0]:
    del extreme_small[0] #극대,극소의 배열로 만들기 위해 첫 극값이 극솟값이라면 첫 극솟값은 제외

#극대, 극소의 순서로 두 값이 0값을 지날때 극값 list에 더하기
for i in range(min(len(extreme_small),len(extreme_small))-1):
    if accel[extreme_big[i]]*accel[extreme_small[i]]<0:
        extreme.append(extreme_big[i])
        extreme.append(extreme_small[i])

l = len(extreme) 




#걸음수 파트
#걷기상태 판별 함수
def state(b,s): #extreme 값중 accel index 값으로 받기
    if accel[s]<-6 or accel[b]>6: 
        state = 'run'
    elif accel[s]<=-0.5 or accel[b]>=0.5:
        state = 'walk'
    else:
        state = 'stand'
    return state

#걸음수 측정
count_run=0 #달리기 횟수
count_walk=0 #걷기 횟수

for i in range(1,l//2 +1): 
    a = state(extreme[2*i-2],extreme[2*i-1]) #홀수 인덱스는 극댓값, 짝수인덱스는 극솟값
    if a =='run':
        count_run+=1
    if a == 'walk':
        count_walk +=1

count_total =count_run+count_walk #총 걸음수




#상태구분자 파트
#상태구분자 dictionary 생성
s= {} #상태구분자 dictionary {상태번호: 가속도 값}
for i in range(len(accel)):
    if i%25 ==0:
        s[i] = accel[i-2]

skey = list(s.keys())

#상태구분자 표시
for i in range(len(s)):
    if accel[skey[i]-1]>accel[skey[i]]:
        if state(skey[i]-1, skey[i]) == 'run':
            s[skey[i]] = 2
        if state(skey[i]-1, skey[i]) == 'walk':
            s[skey[i]] = 1
        if state(skey[i]-1, skey[i]) == 'stand':
            s[skey[i]] = 0
    else:
        if state(skey[i], skey[i]-1) == 'run':
            s[skey[i]] = 2
        if state(skey[i], skey[i]-1) == 'walk':
            s[skey[i]] = 1
        if state(skey[i], skey[i]-1) == 'stand':
            s[skey[i]] = 0
    


#파일 출력
fout = open('output.txt','w')
fout.write(str(count_total)+'\n' + str(count_walk) + '\n' + str(count_run)+'\n')
for i in range(len(s)):
    fout.write('S'+str(i)+': '+ str(s[25*i])+'\n')

