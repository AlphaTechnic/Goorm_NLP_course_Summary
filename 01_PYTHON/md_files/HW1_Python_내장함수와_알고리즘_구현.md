# 과제 1. 나만의 python & 알고리즘 함수 만들기
## 1. 파이썬 내장함수 만들기
Python에는 사용자의 편의를 위해서 여러가지 함수를 내장하고 있다. 다음 사진이 python 내장함수의 목록을 보여준다.

<p align="center"><img src="https://wikidocs.net/images/page/14598/2-1.png" width="600px"></p>

자세한 내용은 [링크](https://docs.python.org/ko/3/library/functions.html)에서 확인해 볼 수 있으며, 문서 안에서 몇 가지 예시를 제시하고 있다. 다음은 python 공식 문서에서 제시하는 `all` 함수의 예시를 `my_all` 함수로 재작성한 예시이다.


```python
def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

test1 = [True, 7 == 4, 3 > 7, False]
test2 = [3 < 5, 10 == 10, True, 'something']

# Assert 문은 이하의 식의 참인지 검사합니다.
assert all(test1) == my_all(test1) == False
assert all(test2) == my_all(test2) == True

print("통과")
```

    통과


아래의 함수들은 자주 사용되는 내장 함수들의 목록이다. 위의 코드 예시와 같이 몇 가지 함수들을 내장 함수를 쓰지 않고 따라 만들어보자. \
(단, 편의를 위해 엄격하게 만들지 않고 test를 통과할 정도만 작성하여도 무방하다.)

### 1-1. abs


```python
def my_abs(number):
    return number if number > 0 else -number

test1 = 1.7
test2 = -8
assert abs(test1) == my_abs(test1)
assert abs(test2) == my_abs(test2)
print("통과")
```

    통과


### 1-2. round


```python
def my_round(number, ndigits=None):
    if ndigits == None:
        ndigits = 0
    
    # int 연산으로 바꿈
    num_int = int(number * 10 ** (ndigits + 1))
    if num_int % 10 >= 5:
        num_int += 10 - (num_int % 10)  # 조정
    else:
        num_int -= (num_int % 10)
    ret = num_int * 10 ** (-ndigits-1)

    if ndigits == 0:
        return int(ret)
    else:
        return ret

test = 1.74789
assert round(test) == my_round(test)
assert round(test, 3) == my_round(test, 3)
assert round(-test, 2) == my_round(-test, 2)
print("통과")
```

    통과


### 1-3. any


```python
def my_any(iterable):
    for ele in iterable:
      if ele:
        return True
    return False

test1 = [True, 7 == 4, 'Something', False]
test2 = [3 > 5, 10 != 10, False, '', None]
assert any(test1) == my_any(test1)
assert any(test2) == my_any(test2)
print("통과")
```

    통과


### 1-4. enumerate


```python
def my_enumerate(sequence, start=0):
    for ele in sequence:
        yield (start, ele)
        start += 1

test1 = [60, 50, 20, 10]
test2 = [True, None, 'test']
assert list(enumerate(test1)) == list(my_enumerate(test1))
assert list(enumerate(test2, 12)) == list(my_enumerate(test2, 12))
print("통과")
```

    통과


### 1-5. max & min


```python
def my_max(*args):
    if len(args) == 1:
        args = args[0]

    mxv = - 10 ** 9
    for ele in args:
        if ele > mxv:
            mxv = ele
    return mxv


def my_min(*args):
    if len(args) == 1:
        args = args[0]

    mnv = 10 ** 9
    for ele in args:
        if ele < mnv:
            mnv = ele
    return mnv


test = [7, 4, 2, 6, 8]
assert max(test) == my_max(test) and min(test) == my_min(test)
assert max(7, 4, 2, 5) == my_max(7, 4, 2, 5) and min(7, 4, 2, 5) == my_min(7, 4, 2, 5)
print("통과")
```

    통과


### 1-6. range
실제론 함수가 아니지만 함수 같이 만들어보자.


```python
def my_range(*args):
    # print(args)
    if len(args) == 1:
        it = 0
        while it < args[0]:
            yield it
            it += 1

    if len(args) == 2:
        s = args[0]
        e = args[1]
        while s < e:
            yield s
            s += 1

    if len(args) == 3:
        s = args[0]
        e = args[1]
        diff = args[2]
        if diff > 0:
            while s < e:
                yield s
                s += diff
        elif diff < 0:
            while s > e:
                yield s
                s += diff

assert list(range(10)) == list(my_range(10))
assert list(range(3, 10)) == list(my_range(3, 10))
assert list(range(3, 10, 2)) == list(my_range(3, 10, 2))
assert list(range(10, 3, -2)) == list(my_range(10, 3, -2))
print("통과")
```

    통과


### 1-7. reversed


```python
def my_reversed(seq):
    return seq[::-1]

test = [7, 4, 2, 6, 8]
assert list(reversed(test)) == list(my_reversed(test))
print("통과")
```

    통과


### 1-8. filter


```python
def my_filter(function, iterable):
    for ele in iterable:
        if function(ele):
            yield ele

def test_function(number):
    return number > 5
test = [1, 7, 5, 2, 9, 11]

# 역슬래시 "\"를 이용하면 평가식을 다음 줄로 나눌 수 있다.
assert list(filter(test_function, test)) == list(my_filter(test_function, test)) \
    == list(filter(lambda x: x > 5, test))
print("통과")
```

    통과


### 1-9. map


```python
def my_map(function, iterable):
    for ele in iterable:
        yield function(ele)

def test_function(number):
    return number * 2


test = [1, 7, 5, 2, 9, 11]

assert list(map(test_function, test)) == list(my_map(test_function, test)) \
    == list(map(lambda x: x * 2, test))
print("통과")
```

    통과


### 1-10. sum


```python
def my_sum(iterable, start=0):
    tot = 0
    for ele in iterable:
        tot += ele
    return tot

test = [7, 4, 2, 6, 8]
assert sum(test) == my_sum(test)
assert sum(range(10)) == my_sum(my_range(10))
assert sum(filter(lambda x: x % 2, range(1, 20, 3))) \
    == my_sum(my_filter(lambda x: x % 2, my_range(1, 20, 3)))
print("통과")
```

    통과


### 1-11. zip


```python
def my_zip(*iterables):
    if len(iterables) == 1:
        iterables = iterables[0]

    length = len(iterables)

    idx = 0
    while idx != len(iterables[0]):
        tmp = []
        for i in range(length):
            tmp.append(iterables[i][idx])
        yield tuple(tmp)
        idx += 1
    

test1 = (1, 2, 3)
test2 = (10, 2, 30)
assert list(zip(test1, test2)) == list(my_zip(test1, test2))

test3 = [(10, 20, 30, 40), (55, 22, 66, 70), (False, True, True, False)]
assert list(zip(*test3)) == list(my_zip(*test3))
print("통과")
```

    통과


### 1-12. sorted
정렬 알고리즘은 어떠한 것을 써도 무방하다.
쉬운 정렬 알고리즘으로 일반적으로 [삽입정렬](https://ko.wikipedia.org/wiki/%EC%82%BD%EC%9E%85_%EC%A0%95%EB%A0%AC), [선택정렬](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%A0%95%EB%A0%AC), 그리고 [버블정렬](https://ko.wikipedia.org/wiki/%EA%B1%B0%ED%92%88_%EC%A0%95%EB%A0%AC)을 꼽는다.


```python
def neg(obj):
    if type(obj) == int:
        return - obj
    else:
        ret = []
        for ele in obj:
            ret.append(-ele)
        return tuple(ret)


def nothing(num):
    return num


def my_sorted(iterable, key=None, reverse=False):
    fun = nothing
    if key:
        fun = key
    if reverse:
        iterable = list(map(neg, iterable))

    # 버블 소트
    p = 1
    while p != len(iterable):
        for i in range(len(iterable) - p):
            if fun(iterable[i]) > fun(iterable[i + 1]):
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
        p += 1

    if reverse:
        iterable = list(map(neg, iterable))

    return iterable


test1 = [7, 4, 2, 6, 8]
assert sorted(test1) == my_sorted(test1)
test2 = [(1, 2), (6, 2), (5, 3), (10, 5)]
assert sorted(test2) == my_sorted(test2) \
   and sorted(test2, reverse=True) == my_sorted(test2, reverse=True) \
   and sorted(test2, key=lambda x: x[1]) == my_sorted(test2, key=lambda x: x[1])
print("통과")
```

    통과


## 2. 알고리즘 함수 만들기
몇 가지 간단한 알고리즘 함수를 만들어보자.

### 2-1. 피보나치 수열 만들기
숫자 $N$가 주어졌을때,다피보나치 길이 $N$의 피보나치 수열을 생성하는 함수를 작성해보자. 시작은 1부터다.


```python
def fibonacci(number):
    if number == 1:
        return [1]
    if number == 2:
        return [1, 1]

    ret = [1, 1]
    a = 1
    b = 1
    number -= 2
    while number != 0:
        a, b = b, a + b
        ret.append(b)
        number -= 1

    return ret

assert list(fibonacci(10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

assert sum(fibonacci(5)) == 12
print("통과") 
```

    통과


### 2-2. 순열 만들기
수열 $S$가 주어졌을때 그 안에서 $N$를 뽑아 순열을 만드는 함수를 작성해보자. 순서는 상관없다. \
(힌트: 재귀 함수를 써보자)


```python
res = []
ans = []
vis = [False for _ in range(10)]


def init():
    global vis, res, ans
    res = []
    ans = []
    vis = [False for _ in range(10)]


def my_permutations(seq, r):
    global vis, res, ans

    if len(res) == r:
        res_tup = tuple([res[i] for i in range(len(res))])
        ans.append(res_tup)
        return ans

    for i in range(0, len(seq)):
        if vis[i]: continue
        vis[i] = True
        res.append(seq[i])

        my_permutations(seq, r)

        vis[i] = False
        res.pop()
    return ans

from itertools import permutations
test = [1, 2, 3, 4]

# init을 삽입하기 위해 assert 구문 수정
init()
assert set(permutations(test, 2)) == set(my_permutations(test, 2))
init()
assert set(permutations(test, 3)) == set(my_permutations(test, 3))
print("통과") 
```

    통과


### 2-3. 조합 만들기
수열 $S$가 주어졌을때 그 안에서 $N$를 뽑아 조합을 만드는 함수를 작성해보자. 순서는 상관없다. \
(힌트: 재귀 함수를 써보자)


```python
res = []
ans = []


def init():
    global res, ans
    res = []
    ans = []


def my_combinations(seq, number, idx):
    if len(res) == number:
        res_tup = tuple([res[i] for i in range(len(res))])
        ans.append(res_tup)
        return ans

    for i in range(idx, len(seq)):
        res.append(seq[i])

        my_combinations(seq, number, i + 1)

        res.pop()
    return ans

from itertools import combinations
test = [1, 2, 3, 4]

# init을 삽입하기 위해 assert 구문 수정 and my_combinations()에 파라미터 개수 하나 추가
init()
assert set(combinations(test, 2)) == set(my_combinations(test, 2, 0))
init()
assert set(combinations(test, 3)) == set(my_combinations(test, 3, 0))
print("통과") 
```

    통과


