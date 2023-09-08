import pandas as pd
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pyowm.utils import timestamps
from pyowm.utils import config
from pyowm import OWM

import time

import random

import modi

import datetime


bundle = modi.MODI()
button = bundle.buttons[0]
motor = bundle.motors[0]
display = bundle.displays[0]
speaker = bundle.speakers[0]

# Open Weather Map
owm = OWM('821411ca9f7cf8ff908a7a51b611b6e5')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Seoul, KR')
w = observation.weather


# BeatifulSoup for rainfall
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hpya%2Fsp0YiRssSl16LNssssssb4-082859"
html = urlopen(url).read()
# 기준은 서울
soup = BeautifulSoup(html, 'html.parser')
rain = soup.find(class_='cell_weather')
rain2 = rain.text.split(' ')

# Get current time
now = datetime.datetime.now()

# Reset clock
motor.degree = 00, 00
time.sleep(3)


# Set clock to current time
display.text = "Start"
while True:
    if now.hour % 12 <= 10:
        motor.degree = 0, (now.hour % 12) * 10
    else:
        motor.degree = 0, 100

    if button.clicked == True:
        break

# =====================================================================================<Wake Up> 07:00=========================================================
# Set clock to 8 AM
motor.degree = 0, 70
display.text = "Wake Up"
# 알람소리
for i in range(1, 7):
    speaker.tune = i * 10, 100
    time.sleep(0.2)

for i in range(1, 7):
    speaker.tune = i * 10, 100
    time.sleep(0.2)
speaker.tune = 0, 0

while True:
    if button.clicked == True:
        break

# =======================================================================================<Mode 1> 09:00==========================================================
display.text = "Mode 1"
# set clock to 9 PM
motor.degree = 0, 90
while True:
    if button.clicked == True:
        break
# Show current temperature, wind speed, possibility of rainfall
display.text = str(
    f"temp:{round(w.temperature('celsius')['temp'])}C  wind:{round(w.wind()['speed'])}m/s     {rain2[4]}")

while True:
    if button.clicked == True:
        break
# =======================================================================================<Mode 2> 14:00==========================================================
display.text = "Mode 2"
# set clock to 2 PM
motor.degree = 0, 20
while True:
    if button.clicked == True:
        break

# 1번부터 4번까지의 4개의 게임 진행
# '참'이면 버튼 한번, '거짓'이면 버튼 두번 눌러서 진행

# 최종적으로 정답률 반환
total_accurate = 0
# -----------------------------------------------<1> start----------------------------------
# First Game: Number Memory
# 숫자 암기 게임: 1부터 99 안의 5개의 랜덤 정수를 기억하는지 여부 확인
display.text = "Game 1.      Number memory"
time.sleep(3)
display.text = "Press to    start"
while True:
    if button.clicked:
        break

display.text = 'yes->once no->twice'
time.sleep(3)

# 기억해야할 정수 리스트
num_list = random.sample(range(1, 99), 5)

# 검사 리스트 -> 리스트 숫자들 2 내외의 숫자들로 구성
test_list = []
err = random.randint(-2, 2)
for i in num_list:
    test_list.append(i + err)

# 검사
# answer 함수: test_list 함수에 대해 정답을 반환하는 함수


def answer(test_list_num, num_list):
    if test_list_num in num_list:
        answer = True
    else:
        answer = False
    return answer

# user 함수: 사용자의 정답 입력을 받는 함수


def user(num):
    user_answer = ''
    display.text = f'Was {num} in the list?'
    time.sleep(0.5)
    while True:
        if button.clicked:
            user_answer = True
            break
        if button.double_clicked:
            user_answer = False
            break
    return user_answer

# test 함수: 유저의 입력과 정답을 비교하여 정답 개수를 반환


def test():
    accurate = 0
    for i in test_list:
        if answer(i, num_list) == user(i):
            accurate += 1
        else:
            pass

    return accurate


# main
display.text = str(num_list)
time.sleep(5)
accurate_num = test()
display.text = str(f'Accurate: {accurate_num}')
time.sleep(3)

total_accurate += accurate_num

# ------------------------------------------------<1> end----------------------------------
# -----------------------------------------------<2> start-----------------------------------
# Second Game: Simple Number calculation
display.text = "Game 2.      Calculation"
time.sleep(3)
display.text = "Press to    start"

while True:
    if button.clicked:
        break

display.text = 'yes->once no->twice'
time.sleep(3)

# 문제 만드는 함수


def make_question2():
    a = random.randint(1, 20)  # a에 1부터 20 사이의 임의의 수 저장
    b = random.randint(1, 20)  # b에 1부터 20 사이의 임의의 수 저장
    k = random.randint(1, 3)  # ob에 1부터 3 사이의 임의의 수 저장
    d = random.randint(1, 9)
    e = random.randint(2, 8)

    # 문자열 변수 q에 문제를 만든다.
    # 첫번째 숫자를 q에 저장한다

    if k == 1:  # op 값이 1이면 덧셈
        q = str(a)
        q = q + "+"
        q = q + str(b)
    if k == 2:  # op 값이 2이면 뺄셈
        q = str(a)
        q = q + "-"
        q = q + str(b)
    if k == 3:  # op 값이 3이면 곱셈
        q = str(d)
        q = q + "*"
        q = q + str(e)
    return q

# 정답 확인


def user2():
    user_answer2 = ''
    time.sleep(0.5)

    while True:
        if button.clicked:
            user_answer2 = True
            break
        if button.double_clicked:
            user_answer2 = False
            break
    return user_answer2


# 만들어진 문제를 돌려준다
accurate2 = 0
for x in range(5):  # 다섯문제를 출력
    # 문제를 만든다
    q = make_question2()

    if '+' in q or '-' in q:
        j = random.randint(-2, 2)
        g = eval(q) + j
    else:
        q1 = list(q)
        j = random.randint(-1, 1)
        g = (int(q1[2]) + j) * int(q1[0])

    display.text = f'{str(q)} = {str(g)}'

    if eval(q) == g:
        answer2 = True
    else:
        answer2 = False

    if answer2 == user2():
        accurate2 += 1
    else:
        pass

display.text = f'Accurate:{accurate2}'
time.sleep(2)

total_accurate += accurate2

# --------------------------------------------------------------------------<2> end------------------------------------
# --------------------------------------------------------------------------<3>------------------------------------
# 3번 단어 암기 게임
# 단어 리스트
voca_list = ["apple", "banana", "monkey", "fish", "wallet",
             "sun", "river", "scissors", "paper", "glasses"]
voca_list2 = ["ship", "banana", "lion", "fish", "pencil",
              "sun", "river", "scissors", "dok-do", "glasses"]
correct3 = 0
wrong3 = 0

display.text = str(voca_list)
time.sleep(4)
# 단어암기 게임은 총 5회 동안 반복


num_list = random.sample(range(0, 10), 5)


for i in range(0, 5):
    # 10개의 단어 중 랜덤하게 선택 후 표시
    k = num_list[i]
    display.text = str(voca_list2[k])

    if voca_list2[k] in voca_list:
        real_answer = "T"
    else:
        real_answer = "F"

    while True:
        if button.clicked == True:
            user_answer = 'T'
            break
        if button.double_clicked == True:
            user_answer = 'F'
            break
    time.sleep(0.5)
    # 정답이면 correct 증가, 아니면 wrong 증가
    if user_answer == real_answer:
        correct3 += 1
    else:
        wrong3 += 1


# 최종적으로 몇 개를 맞췄는지 표시
display.text = (f"{correct3} / 5")
time.sleep(2)

total_accurate += correct3
# --------------------------------------------------------------------------<3>------------------------------------
# --------------------------------------------------------------------------<4>------------------------------------
# 4번 기억력 검사
# 4번 게임에 대한 아주 기본적인 설명
display.text = "Game 4.       memory"
time.sleep(3)
display.text = 'Personal questions'
time.sleep(2)

# 게임 시작 위한 버튼 누르기
display.text = "Press to start"
while True:
    if button.clicked:
        break

display.text = 'yes->once no->twice'
time.sleep(3)

# 4번 게임


# 개인적인 질문들과 답 csv 형태로 저장된 파일 불러서 dataframe으로 저장
game4_csv = 'game4_questions.csv'
df = pd.read_csv(game4_csv, index_col=0)

# test_index_4: df 길이 내에서 질문할 4개의 숫자 랜덤으로 선정.
test_index_4 = random.sample(range(1, len(df)), 4)

# test_list_4: 전체 질문 중 질문 인덱스에 해당하는 검사 질문 리스트
test_list_4 = list(df['question'].iloc[test_index_4])

# answer_list_4: test_list 질문에 대한 답 리스트
answer_list_4 = list(df['answer'].iloc[test_index_4])

# 검사
# 유저의 정답 입력 함수


def user_4(i):
    user_answer_4 = ''
    display.text = str(test_list_4[i])
    time.sleep(0.5)
    while True:
        if button.clicked:
            user_answer_4 = True
            break
        if button.double_clicked:
            user_answer_4 = False
            break
    return user_answer_4

# test 함수: 유저의 입력과 정답을 비교하여 정답 개수를 반환


def test_4():
    accurate_4 = 0
    for i in range(len(test_list_4)):
        if answer_list_4[i] == user_4(i):
            accurate_4 += 1
        else:
            pass
    return accurate_4


# main
# test 함수 실행
accurate_num_4 = test_4()
display.text = str(f'accurate: {accurate_num_4}')
time.sleep(3)


total_accurate += accurate_num_4

# --------------------------------------------------------------------------<4> end------------------------------------
# 4개 게임 전체에 대한 정답률 표시
# 날짜, 각 게임 성적, 최종 합으로 구성된 Total_Accuracy.csv 파일 생성

display.text = str(f'Total Accuracy: {total_accurate}/20')
time.sleep(3)

# 4개 게임에 대한 성적을 DataFrame 형태로 저장.
today = str(datetime.datetime.today())[:10]
total_accurate_dict = {'날짜': [today], '숫자암기': [accurate_num], '숫자계산': [accurate2],
                       '단어암기': [correct3], '기억력검사': [accurate_num_4], '전체': [total_accurate]}
total_accurate_df = pd.DataFrame(total_accurate_dict).set_index('날짜')

# csv 파일로 내보내기
if not os.path.exists('Total_Accuracy.csv'):
    total_accurate_df.to_csv('Total_Accuracy.csv',
                             mode='w', encoding='utf-8-sig')
else:
    total_accurate_df.to_csv('Total_Accuracy.csv',
                             mode='a', encoding='utf-8-sig', header=False)

# =======================================================================================<Mode 3> 18:00==========================================================
display.text = "Mode 3"

# set clock to 6 PM
motor.degree = 0, 60
while True:
    if button.clicked == True:
        break

# Play alarm sound
for i in range(0, 5):
    speaker.tune = 30, 100
    time.sleep(0.5)
    speaker.tune = 0, 0
    time.sleep(0.3)
speaker.tune = 0, 0

display.text = f"18:00            Take Pill"

while True:
    if button.clicked == True:
        break
# ======================================================================================<Mode 4> 22:00==========================================================
display.text = "sleep"
# Set clock to 10 PM
motor.degree = 0, 100

# Play alarm sound
speaker.tune = 50, 100
time.sleep(0.15)
speaker.tune = 75, 100
time.sleep(0.15)
speaker.tune = 25, 100
time.sleep(0.15)
speaker.tune = 50, 100
time.sleep(0.15)
speaker.tune = 15, 100
time.sleep(0.15)
speaker.tune = 0, 0
time.sleep(0.2)
speaker.tune = 50, 100
time.sleep(0.15)
speaker.tune = 75, 100
time.sleep(0.15)
speaker.tune = 25, 100
time.sleep(0.15)
speaker.tune = 50, 100
time.sleep(0.15)
speaker.tune = 15, 100
time.sleep(0.15)

speaker.tune = 0, 0
while True:
    if button.clicked == True:
        break


display.text = "Goodbye"
