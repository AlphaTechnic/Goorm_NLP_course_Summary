### Generator

- range 함수의 경우 숫자를 하나씩 생성하여 반환
- element를 하나씩 생성해서 반환하는 객체를 **generator**라고 한다.
- function에서 yield를 사용할 시 generator가 됨
- yield하는 위치에서 값을 반환
- **다시 값을 요청 시 yield 다음 줄부터** 실행
- Return될 시 반복을 멈춤
    - 정확히는 `Stopiteration Exception` 발생
- 괄호로 Generator Comprehension 형태로 선언 가능
    - function 등으로 이미 괄호가 쳐져 있다면, 괄호 생략 가능


```python
even_generator = (i * 2 for i in range(5))
for i in even_generator:
    print(i)
```

    0
    2
    4
    6
    8


### Zip
- 2개 이상의 순환 가능한 객체를 앞에서부터 한번에 접근할 때 사용
- Unpacking을 이용하여 2차원 리스트의 열 단위 접근 역시 가능


```python
arr = [[1, 2, 3], [4, 5, 6]]
for col in zip(*arr):
    print(col)
```

    (1, 4)
    (2, 5)
    (3, 6)



```python
# transopse
arr = [[1, 2, 3], [4, 5, 6]]
arr_transpose = [list(col) for col in zip(*arr)]
print(arr_transpose)
print(list(zip(*(zip(*arr)))))
```

    [[1, 4], [2, 5], [3, 6]]
    [(1, 2, 3), (4, 5, 6)]


### Built-in function
- `map([function], [iterable])`
    - 각 element에 function 함수를 적용하여 반환


```python
seq = [1, -1, 2, -2, 3, -3]
list(map(lambda x: x > 0, seq))
```




    [True, False, True, False, True, False]



- `filter([function], [iterable])`
    - 각 element에 function을 적용하여, `True`가 나오는 것만 반환


```python
seq = [1, -1, 2, -2, 3, -3]
list(filter(lambda x: x > 0, seq))




```




    [1, 2, 3]

ㅤ

ㅤ

ㅤ



## Object-Oriented Programming



```python
class Student(object):
    SCHOOL = "SOGANG"  # 클래스 속성 (Class Attribute)

    def __init__(self, name: str, sid: int):
        self.name = name
        self.sid = sid
        self.classes = set()

    def take_classes(self, class_name: str) -> None:
        self.classes.add(class_name)

    def drop_class(self, class_name: str) -> None:
        self.classes.discard(class_name)

```

### Method
- 현재 수정하고자 하는 객체를 self로 지정
- 파이썬은 `self`를 첫번째 파라미터로 명시적으로 받음

### Magic Method: Initializer
- 메소드 이름이 `__METHOD__` 형태일 경우 특별한 Magic Method

### `__init__`
- 객체를 생성할 때 호출됨
- 일반적으로 객체의 속성을 초기화하는 데 사용
- `Class(args, ..)` 형태로 호출
- 거의 유일하게 정해진 Argument format이 없는 매직 메소드
    - 다른 매직 메소드와 차별되는 점


### `__del__`
- 객체를 소멸할 때 호출됨
- 파이썬은 Garbage Collection으로 메모리 관리
    - 객체가 어디에서도 참조되지 않을 때 객체가 소멸
- `del` 명령어
    - 변수 이름을 명시적으로 없애기 가능
    - **'참조'를 삭제하는 것이지 '객체'를 삭제하는 것이 아님**

### `__getitem__`,  `__setitem__`
- [] 을 재정의 (indexing)


```python
class DoubleMapper(object):
    def __init__(self):
        self.mapping = dict()

    def __getitem__(self, index):  # indexing get
        return self.mapping.get(index, 0)  # 2번째 arg는 default 값

    def __setitem__(self, index, item):
        self.mapping[index] = item

mapper = DoubleMapper()
print(mapper[10])  # self-defined dictionary 느낌으로 사용 가능

mapper[10] = 15
print(mapper[10], mapper[1])

```

    0
    15 0


### `__len__`


```python
class Dataset:
    def __init__(self, data, times):
        self.data = data
        self.times = times

    def __len__(self):
        return len(self.data) * self.times

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError()
        return self.data[index % len(self.data)]

dataset = Dataset([2, 4, 6, 8], times=5)
print(len(dataset))
print(dataset[5])

```

    20
    4


### `__str__`
- 객체를 다른 타입으로 형 변환할 때 호출
- 이외에도 `__int__`, `__float__`, `__bool__` 등이 존재


```python
class Student:
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def __str__(self):
        return self.name + "_" + str(self.sid)

    def __int__(self):
        return self.sid

juho_kim = Student("김주호", 20121277)
print(str(juho_kim), juho_kim)
print(int(juho_kim))

```

    김주호_20121277 김주호_20121277
    20121277



```python
class Student:
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def __lt__(self, other):
        return self.sid < other.sid

students = [
    Student("Jun", 2345),
    Student("Cho", 1234),
    Student("Ho", 4567),
]

print(*[st.name for st in sorted(students)])
```

    Cho Jun Ho


### `__add__`
- 산술 연산자를 재정의할 수도 있다.


```python
class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + 'i'

    def __add__(self, other):
        return MyComplex(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )


a = MyComplex(-1, 3)
b = MyComplex(3, 4)
print(a + b)

a += MyComplex(3, 4)
print(a)
```

    2 + 7i
    2 + 7i



```python
class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + 'i'

    # in-place mode 연산으로 재정의
    def __iadd__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        return self


a = MyComplex(-1, 3)
a += MyComplex(3, 4)
print(a)
```

    2 + 7i


### `__call__` (많이 씀)
- 클래스를 함수처럼 만들어준다.
- 생성된 객체를 호출 가능하게 만듦
- `instance(args, ..)`가 `instance.__call__(args, ..)` 를 호출


```python
class AdditionNumber(object):
    def __init__(self, number):  # 생성자
        self.number = number

    def __call__(self, number):
        return self.number + number

addto5 = AdditionNumber(5)
print(addto5(20))
```

    25


### Property
- Property를 통해 Getter, Setter를 명시적으로 설정 가능
- Encapsulation 등에 활용
    - 이를테면, read(getter)만 허락하고 write(setter)는 불허하는 방식으로


```python
class Circle(object):
    PI = 3.141592

    def __init__(self, radius=3.):
        self.radius = radius

    def get_area(self):
        return Circle.PI * self.radius ** 2

    # 넓이가 value가 되도록, 반지름을 set
    def set_area(self, val):
        self.radius = (val / Circle.PI) ** 0.5

circle = Circle(5.)
print(circle.get_area())

circle.set_area(10)
print(circle.radius)
```

    78.5398
    1.7841243017410415



```python
class Circle(object):
    PI = 3.141592

    def __init__(self, radius=3.):
        self.radius = radius

    @property
    def area(self):
        return Circle.PI * self.radius ** 2

    @area.setter
    def area(self, val):
        self.radius = (val / Circle.PI) ** 0.5

circle = Circle(5.)
print(circle.area)

circle.area = 10
print(circle.radius)
```

    78.5398
    1.7841243017410415


### 정적 함수
- 파이썬에는 2가지 **정적 함수**가 존재
    - 객체에서는 접근 불가능
    - 일반적으로 Classmethod 형태로 사용
- 아래의 2가지 정적함수는 **상속**을 하면 차이가 발생

- **Static Method**
    - `@staticmethod` 데코레이터 사용
    - 특별한 arg 없음 (`self` 같은)
    - 일반적으로 class 내 유틸함수로 사용
- **Class Method**
    - `@classmethod` 데코레이터 사용
    - 호출된 class인 cls를 인자로 받음 (`self` 와 비슷)
        - 이는 해당 메소드를 호출한 `class`를 구분할 수 있다는 얘기
        - static method는 그렇지 않음
    - factory 패턴에서 사용



```python
class Number:
    Constant = 10

    @staticmethod
    def static_factory():
        obj = Number()
        obj.value = Number.Constant
        return obj

    @classmethod
    def class_factory(cls):
        obj = cls()
        obj.value = cls.Constant
        return obj

number_static = Number.static_factory()
number_class = Number.class_factory()
print(number_static.value, number_class.value)

```

    10 10


### 3 Elements of OOP
- **상속 (Inheritance)**
- **가시성, 캡슐화 (Visibility)**
- **다형성 (Polymorphism)**

### 상속과 다형성


```python
class Student:
    def __init__(self, name: str, sid: int):
        self.name = name
        self.sid = sid
        self.classes = []

    def __str__(self):
        return self.name + "_" + str(self.sid)

    def take_class(self, class_name: str) -> None:
        self.classes.append(class_name)


class Master(Student):
    def __init__(self, name: str, sid: int, professor: str):
        super().__init__(name, sid)
        self.professor = professor

    def __str__(self):
        return super().__str__() + "_prof:" + str(self.professor)
        # return super(Master, self).__str__() + "_prof:" + str(self.professor) # 이것도 가


master_obj = Master("김주호", 20121277, "임경수")
print(master_obj)
print(super(Master, master_obj).__str__())  # super([class], [obj]) -> [class]의 상위 class
```

    김주호_20121277_prof:임경수
    김주호_20121277


### 가시성
- 가시성이란 **사용자에게 모델의 내부를 감추는 것**을 의미
    - 캡슐화, 정보 은닉, 클래스 간 간섭 최소화
    - 최소한의 정보만을 특정 API로 공개
    - Cpp나 JAVA에서는 private & protected로 구현

- Python에서의 가시성
    - 명시적인 private & protected 범위가 없음 => 모두 public
    - private 변수 / 함수 이름 앞에 `__`을 붙임
        - ex ) `self.__name`, `self.__sid`
    - protected 변수 / 함수 이름 앞에 `_`를 붙임
        - ex ) `self._name`, `self._sid`


```python
class TestClass(object):
    def __init__(self):
        self.attr = 1  # public
        self._attr = 2  # protected => 본인과, 상속 받은 놈한테 보임
        self.__attr = 3  # private => 본인한테만 보임

inst = TestClass()
inst.
# private 변수는 맹글링(Mangling)이 된다는 것을 알 수 있다.
print(dir(inst))  # dir([object]) => 객체가 가지고 있는 변수, 메소드를 나열해 보여줌





```

    ['_TestClass__attr', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_attr', 'attr']


- `__`의 경우 변수명 앞에 `_[class이름]`을 넣어 Mangling이 된다.
    - 자식과 이름이 겹치지 않음
- Private와 Protected는 코드 자동 완성 등에서 안 보임.
- **그러나 둘 다 public과 기능적인 차이는 없다.** (밖에서 접근 가능함)

