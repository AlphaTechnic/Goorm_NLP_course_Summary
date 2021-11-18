# Day 4. python 문법 (2) - 2

### 모듈
- 파이썬에서 `모듈` = `.py` 파일
- **최상위에선 상대 경로가 작동되지 않음**
    - 최상위를 거치는 경우 포함
    - 일반적으로 프로젝트 이름으로 폴더를 만들어 소스 코드를 넣음


- `__init__.py` 파일
    - 폴더를 import할 때, 초기화 가능

### 패키지
- 웹 서버 프로젝트와 딥러닝 프로젝트가 따로 있다면?
    - 한 파이썬 위에 둘 다 설치 => 관리 어려움
    - 각각 다른 환경 & 다른 버전의 python에서 돌리고 싶다? => **패키지 관리자가 필요!**

- `pip` + virtual env
- `Anaconda3`


## Advanced Data Structure

### Counter
- 딕셔너리 처럼 생성 및 관리


```python
from collections import Counter
a = Counter([1, 1, 2, 2, 2, 3])
b = Counter([2, 3, 3, 4])

print(a + b)  # 횟수 더하기
print(a & b)  # 교집합
print(a | b)
print(a - b)


```

    Counter({2: 4, 3: 3, 1: 2, 4: 1})
    Counter({2: 1, 3: 1})
    Counter({2: 3, 1: 2, 3: 2, 4: 1})
    Counter({1: 2, 2: 2})


### Named Tuple
- 데이터만을 담기 위한 클래스를 사용한다면?


```python
class Coords3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x:{self.x}, y:{self.y}, z:{self.z}"

obj_3d = Coords3D(1, 2, 3)

print(obj_3d)  # 출력 결과에 필드값이 나타지 않아서 __str__() 재정
print(obj_3d.x, obj_3d.y, obj_3d.z)
```

    x:1, y:2, z:3
    1 2 3



```python
from collections import namedtuple

Coords3D = namedtuple("Coords3D", ['x', 'y', 'z'])
point = Coords3D(10, 20, z=30)

print(point)

print(point.x)
print(point[1])
print(point.z)
print(*point)

point.x += 1  # 오류
```

    Coords3D(x=10, y=20, z=30)
    10
    20
    30
    10 20 30



    ---------------------------------------------------------------------------
    
    AttributeError                            Traceback (most recent call last)
    
    /var/folders/57/3hb2xgp11zd1zyhd1zv6q15r0000gn/T/ipykernel_11255/554529095.py in <module>
         11 print(*point)
         12 
    ---> 13 point.x += 1  # 오류
         14 


    AttributeError: can't set attribute


### Dataclass
- pythonic한 데이터 클래스 선언을 위해서 dataclasses의 dataclass 데코레이터 활용


```python
from dataclasses import dataclass

@dataclass
class Coords3D:
    x: float
    y: float
    z: float
    def norm(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2

point = Coords3D(10, 20, z=30)
print(point)  # 출력 결과에 필드값이 나타남
print(point.x)
print(point.norm())
```

    Coords3D(x=10, y=20, z=30)
    10
    1400


### String
- r"<text>" 형태로 \ 를 무시하고 문자 그대로 취급 가능


```python
# raw string
locate = r"C:\Users\directory"
print(locate)
```

    C:\Users\directory



```python
# f string
page = 2
url = f"https://www.google.com/?page={page}"
print(url)
```

    https://www.google.com/?page=2


## 정규 표현식

### 특수문자
- `\w`
    - `[A-Za-z0-9]`
- `\d`
    - `[0-9]`
- `\s`
    - `[\t\r\n\v\f]`
- `\b` : 단어 경계
    - `(?<=\W)(?=\w)|(?<=\w)(?=\W)`


### 메타문자
- 정규식의 문법적인 요소를 담당하는 문자
    - `.`, `^`, `$`, `*`, `+`, `?`, `{`, `}`, `[`, `]`, `\`, `|`, `(`, `)`

- 이 문자들은 특수한 의미의 문자이므로 사용 불가
    - 만약 문자 그대로 매칭하고 싶다면 Escape 문자 `\`를 붙여 사용

- 문자 클래스 `[]`
- 부정 `^`
- 문자 `.`
    - 아무 문자 하나를 매칭
    - 줄 바꿈 문자 `\n`은 제외
- 0회 또는 1회 `?`
    - `ab?c`
- 반복 횟수 지정 `{m,n}`

- Lazy Matching `?`
    - `*`, `+`, `{}` 와 같은 반복 연산은 욕심쟁이 - 기본적으로 최대한 길게 매칭
    - 최대한 짧게 매칭하기 위해선 뒤에 `?` 삽입
    - `<.+?>`

- 줄의 시작 `^`
    - 줄이나 문자열의 시작점
    - Multiline flag 필요
    - `^\w+`

- 줄의 끝 `$`
    - 줄이나 문자열의 끝
    - Multiline flag 필요
    - `\.s$`

- 그룹 캡쳐 `()`
    - 괄호이므로 우선 순위가 있음
    - 해당 문자열을 캡쳐한다.
    - 캡쳐된 텍스트를 불러올 수 있다.
        - `\1`, `\2`, .., `\[number]`
        - `(\w{2,}).+\1`

- 비그룹 캡쳐 `(?:)`
    - 괄호이므로 우선 순위는 줌
    - 캡쳐는 안 함. 그냥 괄호다.
    - `(?:0|\+82-)\d{1,2}-(\d{4})-\1`

- 뒷 패턴 확인하고, **앞 부분**이랑 매칭 `D(?=R)`
    - R이 바로 뒤에 있는 D를 매칭
    - R 부분은 포함되지 않음
    - `\w+(?=ism)`

- 앞 패턴 확인하고, **뒷 부분**이랑 매칭 `(?<=R)D`
    - R이 바로 앞에 있는 D를 매칭
    - R 부분은 포함되지 않음
    - `(?<=pre)\w+`

### Match object
- match object의 `group()` 메서드는 정규식 전체의 일치부를 찾는다.
- 반면에 `groups()` 메서드는 명시적으로 캡쳐 `()`한 부분을 반환한다.


```python
import re

txt = \
"""
010-1234-1234
010-1234-5678
+82-10-5678-5678
+82-4123-1234
"""

# 패턴은 raw string이어야 함
pat = r"^(?:0|\+82-)\d{1,2}-(\d{4})-\1$"

for mat in re.finditer(pat, txt, re.MULTILINE):
    print(mat.group())
    print(mat.groups())

    print(mat.group(0))  # group()과 효과가 같다.
    print(r"\1 문자열", mat.group(1))
    print()




```

    010-1234-1234
    ('1234',)
    010-1234-1234
    \1 문자열 1234
    
    +82-10-5678-5678
    ('5678',)
    +82-10-5678-5678
    \1 문자열 5678




```python
import re

txt = \
"""
010-1234-1234
010-1234-5678
+82-10-5678-5678
+82-4123-1234
"""
pat = r"^(?:0|\+82-)\d{1,2}-(\d{4})-\1$"

# 탐색
mat = re.search(pat, txt, re.MULTILINE)
print(mat.group(0))

# 치환
repl = r"치환됨\1"
print(re.sub(pat, repl, txt, flags=re.MULTILINE))

# 나누기
splited = re.split(pat, txt, flags=re.MULTILINE)
print(splited)
```

    010-1234-1234
    
    치환됨1234
    010-1234-5678
    치환됨5678
    +82-4123-1234
    
    ['\n', '1234', '\n010-1234-5678\n', '5678', '\n+82-4123-1234\n']


### Compile

- 정규 표현식을 평가하는 것은 오래걸림
- 정규 표현식을 미리 컴파일 => 훨씬 빠름


```python
import re

txts = ["010-1234-1234", "010-1234-5678", "+82-10-5678-5678", "+82-4123-1234"]
pat = r"^(?:0|\+82-)\d{1,2}-(\d{4})-\1$"

for txt in txts:
    mat = re.search(pat, txt)
    if not mat: continue
    print(mat.group(0))

print()
compiled = re.compile(pat, flags=re.MULTILINE)
for txt in txts:
    mat = compiled.search(txt)
    if not mat: continue
    print(mat.group(0))
```

    010-1234-1234
    +82-10-5678-5678
    
    010-1234-1234
    +82-10-5678-5678

