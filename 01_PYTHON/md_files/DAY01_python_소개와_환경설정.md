# Day 1. 파이썬 소개와 환경설정

## LECTURE 0. PYTHON OVERVIEW

### Features of Python

- 플랫폼 독립적인 인터프리터 언어
- 완전 객체 지향 언어
- 동적 타이핑 언어
  - type이 runtime에 결정됨.

## LECTURE 1. ENVIRONMENT

- "개발 환경"이라고 하면 아래 4가지를 고려
  - 운영체제
  - python 인터프리터
  - 코드 편집기 (Editor, IDE)
  - 패키지 관리자

- **OS**
  - 대부분 리눅스

- **인터프리터**
  - python 3

- **IDE**
  - Code Editor
    - Vim

  - IDE
    - Visual Studio Code
    - Pycharm

  - Web-based IDE
    - jupyter notebook
    - jupyter lab

  - Cloud-based IDE
    - colab
    - goormide


- **Package & Environment Manager**

  - PIP
  - Anaconda3

    - 기계학습 및 수치해석 특화 패키지 관리 프로그램



## LECTURE 2. JUPYTER

- python은 기본적으로 interactive shell(대화형)을 사용함
- 이에 대한 발전된 형태라고 보면 됨.
- `Code cell` vs `Markdown Cell`




```python
# 맨 앞에 느낌표를 붙이면 bash shell 명령어
!ls 
```

    DAY1_python_소개와_환경설정.ipynb


## LECTURE 3. VARIABLE & OPERATOR

- 파이썬 변수의 특징
  - 모든 변수는 메모리 주소를 가리킨다. (즉, 모든 것은 포인터이다.)





```python
a = 15
```

- 위 코드는 15라는 값이 담긴 저장 공간을 만들고, a라는 것을 taging한 개념
  - a라는 저장 공간에 15를 담은 게 X


```python
a = 15
b = a
print(id(a))
print(id(b))

print()

# 아래와 같은 in-place 연산 마저도 out-place 연산으로 바꿈
# 왜냐하면, int는 immutable이기 때문
a += 1
print(id(a))
print(id(b))
```

    4497026272
    4497026272
    
    4497026304
    4497026272



```python
# ==  -> 값이 같다.
# is  -> 메모리 주소가 같다.
a = 123456789
b = 123456789

print(a == b)
print(a is b)
```

    True
    False




- Primitive Data Type들은 **Immutable Type (불변 타입)** 이다.
- Primitivd Data Type과 Tuple을 제외한 다른 모든 파이썬 객체는 **Mutable Type (가변 타입)** 이다.


```python
a = [1, 2, 3]
b = a
a.append(4)

print(a)
print(b)
```

    [1, 2, 3, 4]
    [1, 2, 3, 4]



```python
a = [1, 2, 3]
b = a
a = [1, 2, 3] + [4] # 새로운 객체를 다른 메모리공간에 생성하고 a가 그것을 가리키게 됨.

print(a)
print(b)
```

    [1, 2, 3, 4]
    [1, 2, 3]

