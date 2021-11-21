# Day 5. python 문법 (3)
### glob
- 유닉스 스타일의 경로 패턴 매칭 시스템 사용 가능


```python
import glob

# 파이썬을 '실행하는 위치'가 기준
print(*[entry for entry in glob.glob("*.ipynb")])
```

    DAY02_python_문법_1.ipynb DAY05_python_문법_3.ipynb DAY03_python_문법_2.ipynb DAY04_python_문법_2-2.ipynb HW1_Python_내장함수와_알고리즘_구현.ipynb DAY01_python_소개와_환경설정.ipynb


### Pickle
- 파이썬 객체를 그 자체로 디스크에 저장하고 싶다면?? => pickle
    - 객체를 직렬화 (serialize)하여, 파일로 저장

- 장점
    - 사용하기 쉽다
    - 파이썬 객체를 그대로 저장

- 단점
    - 파이썬에서만 읽을 수 있다.
    - **보안 문제**가 있다.

- Class Pickling
    - class 객체를 직렬화하기 위해선 조건이 필요
        - class의 모든 속성이 직렬화 가능해야 한다.
    - 저장된 객체 pickle을 **로드**하고 싶다면 미리 해당 클래스 선언 필요
        - **해당 클래스 정보가 없다면 역직렬화 불가능!**

```python
import pickle


class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return MyComplex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )


my_complex = MyComplex(3, -4)

with open("../test_files/test.pk1", "wb") as fd:
    pickle.dump(my_complex, fd)
del my_complex

with open("../test_files/test.pk1", "rb") as fd:
    my_complex = pickle.load(fd)
    print(my_complex)
```

    <__main__.MyComplex object at 0x112b11e80>



```python
del MyComplex
with open("test_files/test.pk1", "rb") as fd:
    my_complex = pickle.load(fd)  # 에러 발생
```


    ---------------------------------------------------------------------------
    
    AttributeError                            Traceback (most recent call last)
    
    /var/folders/57/3hb2xgp11zd1zyhd1zv6q15r0000gn/T/ipykernel_22485/1550957249.py in <module>
          1 del MyComplex
          2 with open("test_files/test.pk1", "rb") as fd:
    ----> 3     my_complex = pickle.load(fd)  # 에러 발생


    AttributeError: Can't get attribute 'MyComplex' on <module '__main__'>


### csv (Comma Separate Values)
- 데이터 사이언스에서 표준으로 쓰이는 확장자임 `.csv`
- 표 데이터를 프로그램에 상관 없이 쓰기 위한 데이터 형식
    - 필드를 쉼표(`,`)로 구분한 텍스트 파일
    - 탭, 공백 등으로 구분하기도 함
    - 통칭하여 Character Separated Values (`CSV`)라 지칭


- **파이썬 csv 라이브러리**로 쉽게 csv 읽기, 쓰기 가능!!


```python
import csv

with open("test_files/test.csv", "r") as fd:
    # 아래는 빼버려도 상관없음
    reader = csv.reader(fd,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    for entry in reader:
        print(entry)
```

    ['id', 'label']
    ['0', 'label_0']
    ['1', 'label_1']
    ['2', 'label_2']
    ['3', 'label_3']
    ['4', 'label_4']
    ['5', 'label_5']
    ['6', 'label_6']
    ['7', 'label_7']
    ['8', 'label_8']
    ['9', 'label_9']



```python
with open("test_files/test.csv", "w") as fd:
    writer = csv.writer(fd,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    writer.writerow(['id', 'label'])
    writer.writerows([i, f'label_{i}'] for i in range(10))

```

```
# test.csv
id,label
0,label_0
1,label_1
2,label_2
3,label_3
4,label_4
5,label_5
6,label_6
7,label_7
8,label_8
9,label_9
```


### JSON (JavaScript Object Notation)
- **웹 언어인 Javascript의 데이터 객체 표현 방식**식 (`Dictionary` 비슷)
    - 자료 구조 양식을 문자열로 표현
    - 간결하게 표현되어 사람과 컴퓨터 모두 읽기 편함
    - 코드에서 불러오기 쉽고 파일 크기 역시 작은 편
    - 최근 각광 받는 자료구조 형


```python
import json
with open("test_files/test.json", "r") as fd:
    data = json.load(fd)

    print(data)  # json의 null => python의 None
    print(data['version'])
```

    {'name': '01_PYTHON', 'version': '1.0.0', 'dependencies': None}
    1.0.0



```python
obj =\
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": True,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}

with open ("test_files/test2.json", "w") as fd:
    json.dump(obj, fd)
    print("성공")
```

    성공


- json 라이브러리로 읽기 쓰기 가능
- 직렬화 가능 개체
    - 원시 타입
        - `str`, `int`, `float`, `bool` ,`None`
    - 자료 구조
        - `list`, `dict`
    - 이외에는 Decoder 작성 필요
- 사실상 타입 규정이 가능한 셈
    - `int`는 `int`로 읽어들임



### XML (eXtensible Markup Language)
- 데이터 구조와 의미를 설명하는 **태그**를 활용한 언어
    - `<태그>`와 `</태그>` 사이에 값을 표시
    - 문자열로 처리
    - `<태그 속성=값>` 형태로 태그에 속성 부여
    - **HTML**은 웹페이지 표시를 위한 XML
    - 정규 표현식으로 parsing 가


### Beautiful Soup
- 파이썬 기본 XML Parser는 다소 불편
    - 일반적으로 XML, HTML 파싱을 위해 외부 라이브러리를 사용
    - Beautiful soup, xmltodict, ..

- **Beautiful Soup**
    - 가장 많이 쓰이는 parser 중 하나
    - HTML, XML 등 Markup 언어 Scraping을 위한 도구
    - 속도는 다소 느리나 간편하게 사용



```python
from bs4 import BeautifulSoup

with open("test_files/test.xml", "r") as fd:
    soup = BeautifulSoup(
        fd.read(),  # parsing할 문자열
        'html.parser'  # 사용할 parser
    )

to_tag = soup.find(name='to')  # 문서 전체에서 "to" 태그 찾기
print(to_tag)
print(to_tag.string)

```

    <to>Tove</to>
    Tove



```python
# 문서 전체에서 "cite" 태그 찾기
for li_tag in soup.findAll(name="cite"):
    print(li_tag.string)
```

    Cho
    Lee
    Park



```python
# "cites" 태그 찾기
cites_tag = soup.find(name="cites")

print(cites_tag)
print()

print(cites_tag.attrs)
print(cites_tag["attr"])
print()

# 속성으로 태그 찾기 ('attr'이 'name'인 애들만)
cites_tag = soup.find(attrs={'attr': 'name'})
for cite_tag in cites_tag.find_all(name="cite"):
    print(cite_tag.string)
print()

# 2개 동시에도 가능
cites_tag = soup.find(name="cites", attrs={'attr': 'name'})
for cite_tag in cites_tag.find_all(name="cite"):
    print(cite_tag.string)
```

    <cites attr="name">
    <cite>Cho</cite>
    <cite>Lee</cite>
    <cite>Park</cite>
    </cites>
    
    {'attr': 'name'}
    name
    
    Cho
    Lee
    Park
    
    Cho
    Lee
    Park


## Programming Setting

### 명령행 인자 (command line argument)
- 실행할 때마다 필요한 설정값
    - 딥러닝 학습 횟수 (epoch), 학습 계수 (learning rate)
    - GPU 개수

    => **Command Line Argument (명령행 인자)로 입력**

### 설정 파일
- 학습 자료의 폴더 위치
- 웹 서버의 Listening Port

    => **설정 파일에서 불러들이기**


### 명령행 인자
- console 창에서 프로그램 실행 시 프로그램에 넘겨주는 인자 값
- Command-Line Interface(CLI)에서 흔히 쓰이는 방식
- 파이썬에선 sys 라이브러리의 argvs 속성으로 접근
    - 공백 기준으로 잘라서 무나열 형태로 입력


```python
import sys
print(sys.argv)


```

    ['/Users/kimjuho/Documents/2021-11-15_Goorm_NLP/01_PYTHON/myvenv/lib/python3.8/site-packages/ipykernel_launcher.py', '-f', '/Users/kimjuho/Library/Jupyter/runtime/kernel-ec193272-5c87-42f5-a8dc-1d276ecf10e8.json']


### argparser
- 파이썬에서는 명령행 인자를 parsing하는 라이브러리가 있다.
    - 인자 flag를 설정 가능
    - flag별 입력 가능 (긴 flag, 짧은 flag)
    - 기본값 설정 가능
    - Type 설정 가능 (문자열에서 변환)
    - Help를 제공하여, 사용자 편의 향상


```python
import argparse
parser = argparse.ArgumentParser()

# parser.add_argument(<짧은 flag>, <긴 flag>)
parser.add_argument('-l', '-left', type=int)
parser.add_argument('-r', '-right', type=int)
parser.add_argument('-operation',
                    dest='op',  # 타겟 속성, 기본은 -- 없이
                    help="Set operation",  # 인자 설명
                    default='sum',  # 기본 값
                    )

args = parser.parse_args()
print(args)

if args.op == 'sum':  # 인자 접근
    out = args.left + args.right
elif args.op == 'sub':
    out = args.left - args.right

```



### Config File
- 프로그램 실행 설정을 file에 저장
- `Section`, `Key`, `Value` 값의 형태
- 이중 딕셔너리 형태
- 모든 key, value가 **str**

### configparser


```python
import configparser

config = configparser.ConfigParser()
config.read('test_files/test.cfg')
print(config.sections())

port = config["topsecret.server.com"]["port"]  # 딕셔너리처럼 접근
print(type(port), port)
port = config["topsecret.server.com"].getint("port")
print(type(port), port)
```

    ['bitbucket.org', 'topsecret.server.com']
    <class 'str'> 500022
    <class 'int'> 500022



```python
for name, section in config.items():
    print(name)
    for key, value in section.items():
        print(key, value)

with open("test_files/test.cfg", "w") as fd:  # 설정 저장
    config.write(fd)
```

    DEFAULT
    serveraliveinterval 45
    compressoin yes
    compressionlevel 9
    forwardx11 yes
    bitbucket.org
    user hg
    serveraliveinterval 45
    compressoin yes
    compressionlevel 9
    forwardx11 yes
    topsecret.server.com
    port 500022
    forwardx11 no
    serveraliveinterval 45
    compressoin yes
    compressionlevel 9


### Assertion
- 조선을 확인하여 참이 아닐 시 AssertError 발생
    - `assert <조건>`
    - `assert <조건>, <에러메세지>`
- 에러메세지가 없을 경우 빈 칸으로 처리


```python
def add_int(param):
    assert isinstance(param, int), "int만 됨"
    return param + 1

try:
    print(add_int(10))
    print(add_int('str'))
except AssertionError as e:
    print(e)

```

    11
    int만 됨


### Logging
- 프로그램이 일어나는 동안 발생했던 정보를 기록
    - 결과 처리, 유저 접근, 예외 발생.. 등
    - 기록된 로그 분석을 통한 디버깅 & 유저 패턴 파악

- 기록 용도에 따른 차이
    - 용도에 따라 출력 형식 및 필터링 필요

- 어떻게 표출 할까?
    - 표준 에러 출력
        - 일시적
        - 기록을 위해선 Redirection 필요, 구조화 필요
    - 파일 출력
        - 반영구적
        - 매번 file descriptor를 열고 닫아야 함

=> 체계적으로 로깅할 수는 없을까??

### Logging Module
- 파이썬 기본 Logging 모듈
    - 상황에 따라 다른 Level의 로그 출력
    - 심각성 level : `DEBUG` < `INFO` < `WARNING` < `ERROR` < `Critical`


```python
import logging

logging.basicConfig(
    filename='test.log',
    level=logging.INFO
)

logging.debug("디버깅--")
logging.info("정보 확인")
logging.warning("경고")
logging.error("에러")
logging.critical("치명적 오류!")
```

## WEB

### HTML
- XML 형태로 웹페이지의 구조를 표현
    - Beautiful Soup 등 XML parser로 해석 가능
- 다운 받은 HTML 파일을 웹 브라우저가 해석 & 화면에 표시

### Requests
- 웹페이지를 읽기 위해서 일반적으로 Requests 라이브러리 사용


```python
import requests

URL = "https://www.naver.com"
response = requests.get(URL)  # GET으로 접근

print(response.status_code)  # 결과 코드, 200이면 정상이라는 뜻
print(response.text[:300])  # 응답, 웹서버의 경우 HTML 코드

```

    200
    
    <!doctype html>                          <html lang="ko" data-dark="false"> <head> <meta charset="utf-8"> <title>NAVER</title> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=1190"> <meta name="apple-mobile-web-app-title" content="NAVER"/> <meta name="robo



```python
import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/index"
response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    'html.parser'
)

headline = soup.find(name='ul', attrs={'class': 'today_list'})  # 특정 섹션을 들고 옴
for title in headline.find_all(name='strong', attrs={'class': 'title'}):  # 그 섹션 내에서 탐색
    print(title.string)

```

    [오피셜] '페이커' 이상혁, T1과 재계약...다년계약-최고 대우 '추정'
    발롱도르 수상자 극찬, "손흥민 EPL에서 가장 뛰어나"
    "한화에 감사합니다" KS MVP 입에 나온 꼴찌팀, 배려 잊지 않은 '품격'
    MVP 1위표 한 장 못 받은 비운의 홈런왕 "유일한 문제는…"
    "손흥민, 또 골 날아갔네"…비디오판독 득점 취소 1위
    KS 끝나자 12명 방출한 두산, ‘베테랑’ 장원준·유희관 동행도 고민한다 [엠스플 이슈]

