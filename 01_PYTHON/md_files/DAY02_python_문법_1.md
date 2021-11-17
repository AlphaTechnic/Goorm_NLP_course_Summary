# Day 2. python 문법 (1)

### 예약어, 내장함수, 메소드
- python slicing은 새로운 객체를 생성함 (좀 비쌈)
- 파이썬에서 제공되는 기능은 일반적으로 3가지 형태
    - **예약어**
        - 재정의 불가능
        - 예 : `del`
    - **내장함수**
        - 재정의 가능
        - 예 : `len()`, `sum()`, ..
    - **메소드**
        - 객체 내에서 정의된 함수
        - `.method()`으로 접근


### 패킹 & 언패킹


```python
# 언패킹
a, *b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)

```

    1
    [2, 3, 4]
    5


### 3항 연산자
- \[value1\] if \[condition\] else \[value2\]
- 파이썬 유일의 3항 연산자


```python
val = 32
"odd" if val % 2 != 0 else "even"
```




    'even'



### Variable Scope
- 파이썬에서는 상위에 정의된 변수는 언제나 참조 가능
- read는 되는데 write은 함부로 못함
- 아래의 코드는 에러


```python
VAR = 1

def fun():
    VAR += 1

```

### Closure (<- enclose)
- **클로저는 자신을 둘러싼 스코프(네임스페이스)의 상태값을 기억하는 함수**
- **Closure이기 위한 조건**
    - 해당 함수(inner)는 어떤 함수(outer) 내의 중첩된 함수여야 함
    - 해당 함수는 자신을 둘러싼 함수 내의 상태 값을 반드시 참조해야 함
    - 해당 함수를 둘러싼 함수(outer)는 이 함수(inner)를 반환해야 함.



```python
"""
wrapper(n)은
- in_cache 함수 내의 중첩된 함수이고,
- Enclosing하는 in_cache 스코프의 cache 라는 상태값을 참조하고 있으며,
- 자신을 둘러싼 함수는 wrapper을 반환하고 있다!
"""

def in_cache(func):
    cache = {}
    def wrapper(n):
        print(cache) ## !!!!
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

factorial = in_cache(factorial)

factorial(3)
factorial(5)
factorial(10)
```

    {}
    {3: 6}
    {3: 6, 5: 120}





    3628800



- 위 코드 설명
    - 클로저는 자체 스코프를 가지고 있어, cache 라는 상태는 매번 실행할 때마다 초기화되는 것이 아니라 값이 유지시킨다. (마치 전역공간에 선언이라도 했듯)
    - 신기하게도 원래 함수 정의에서 cache 는 wrapper 함수 스코프의 밖에 선언되어 있었다.
    - 그럼에도 wrapper(여기서는 factorial)는 cache 에 접근이 되고, 그 상태를 자신의 스코프 내에서 저장하고 제어할 수 있다.
    - 클로저의 정의 - ‘**클로저는 자신을 둘러싼 스코프(네임스페이스)의 상태값을 기억하는 함수**’- 는 이런 뜻인 것이다.
    - 이 예에서 factorial 스코프에서는 자신을 **둘러싼(enclosing)** 스코프의 상태값을(cache) 기억하고 제어할 수 있다.

> 출처 : https://shoark7.github.io/programming/python/closure-in-python

### Decorator
- Decorator는 closure를 만드는 함수


```python
def print_closure_factory(function):
    def wrapper(var):
        print("Input :", var)
        out = function(var)
        print("Output :", out)

    return wrapper


def add(var):
    return var + 2

print_add = print_closure_factory(add)
print_add(10)
```

    Input : 10
    Output : 12



```python
def print_decorator(function):
    def wrapper(var):
        print("Input :", var)
        out = function(var)
        print("Output :", out)

    return wrapper

@print_decorator
def add(var):
    return var + 2

add(10)
```

    Input : 10
    Output : 12


### Variable Length Parameter
- 인자의 개수가 정해져 있지 않다면?
- \*(Asterisk)를 사용하여 남은 여러 인자를 Packing 가능
- 가변 인자는 맨 마지막에 단 한 개만 위치 가능


```python
def add_all(a, b, *args):
    print(args)

    tot = 0
    for elem in args:
        tot += elem

    return a + b + tot

add_all(1, 2, 3, 4, 5)
```

    (3, 4, 5)





    15



### Keyword Variable Length Parameter
- 명시적으로 지정된 파라미터가 남는다면? => 키워드 가변인자
- \*\*(Double asterisk)를 사용하여 남은 여러 인자를 Packing 가능
- dictionary로 반환


```python
def print_args(a, *args, **kargs):
    print(args, kargs)

print_args(1, 2, 3, 4, 5, var1=13, var2=15)

```

    (2, 3, 4, 5) {'var1': 13, 'var2': 15}


### Parameter Unpacking
- 리스트, 튜플을 언패킹? => \* (single asterisk)
- 딕셔너리를 언패킹? => \*\* (double asterisk)


```python
def function(a, b, c):
    print(a, b, c)

some_list = [1, 2, 3]
function(*some_list)
```

    1 2 3



```python
def function(var1, var3, **kwargs):
    print(var1, var3, kwargs)


dic = {
    "var1": 13,
    "var2": 23,
    "var3": 33,
}
function(**dic)
```

    13 33 {'var2': 23}


### Type hints
- 아래와 같은 방식으로 함수의 정보를 줄 수 있다.
- 에러를 체킹하는 것은 아님!


```python
def multiply_txt(txt: str, n: int) -> str:
    return txt * n

print(multiply_txt("abcde", 3))
print(multiply_txt(2, 3))

```

    abcdeabcdeabcde
    6

