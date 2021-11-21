# 과제 2. 나만의 데이터 셋 만들기
기계 학습 분야에서 중요한 것 중 하나가 학습에 사용할 자료를 수집하고 관리하는 것입니다.
예를 들어 주어진 문장이 부정인지 긍정인지 판별하는 모델을 학습 시키기 위해서는 긍정 부정이 라벨링된 문장 자료가 필요합니다.

문장 | 긍부정 
-------|--------
진짜 좋은 영화. 가히 올해의 영화라고 불릴만하다. | 긍정 
이런 영화에 100억원 이상 때려 넣은 감독은 충무로에서 쫓겨나야한다. | 부정 

그러나 우리가 이러한 자료를 직접 수집 및 라벨링하기는 쉽지 않다.

한편, 내부 연구나 교육적 목적으로 이미 가공된 인터넷의 글들을 수집하는 것은 공정이용으로 저작권법에 어긋나지 않습니다.
따라서 네이버 영화 리뷰를 크롤링하여 나만의 긍부정 문장 데이터 셋을 만들어 봅시다.


## 2-1. 네이버 영화 리뷰 크롤링 (40점)
현재 상영 중인 영화에 대한 영화 한 줄 평은 다음 링크에서 확인 가능합니다.

[https://movie.naver.com/movie/point/af/list.naver?&page=1](https://movie.naver.com/movie/point/af/list.naver?&page=1)

네이버 영화 한줄평의 주소는 다음과 같이 `<페이지 숫자>`에 해당되는 숫자를 넣으면 해당 페이지를 불러오는 것이 가능합니다.

https://movie.naver.com/movie/point/af/list.naver?&page= `<페이지 숫자>`

이러한 접근을 통해 영화 한 줄 평을 끍어모아 다음과 같은 형태의 `CSV` 파일로 저장하는 코드를 만들어 봅시다.

movie | sentence | score
------|------|------
모가디슈 | 재미잇게 잘봤습니다. 배우들 연기에 더몰입감있게 봤습니다. | 10
낙원의 밤 | 차승원의 유머만 남은 흉내 낸 누아르, 결말조차 완벽하게 폭망 | 2
국화꽃 향기 | 뭔가 와닿지 않는 감동 그리고 스토리. 아쉽지만 여운이 남지 않는다 | 4
미쓰 홍당무 | 서우가 아주 매력적으로 나오는 영화 | 8
더 수어사이드 스쿼드 | 후련하게 봤어요 재밌네요ㅋㅋㅋ잔인하고 징그러운거 좋아하시는 분들께 추천 | 9

### 크롤러를 만들때 다음과 같은 사항을 준수해야 합니다.
1. 실제 학습을 진행할 것은 아니기 때문에 문장은 1000개 정도만 가져오면 충분합니다.
2. 각 페이지를 조회하실때 시간차가 없다면 DDOS 공격으로 분류되어 페이지 접속이 막힐 수가 있습니다. 페이지 조회시 최소 0.5초의 시간 차를 둡시다.
3. 신고되어 삭제된 한줄평은 데이터에 들어가면 안됩니다. 또한 한줄평이 아예 없는 경우도 제외하셔야 합니다.
4. 사용 가능한 라이브러리는 다음과 같습니다.
    * 파이썬 표준 라이브러리
    * Request
    * Beutiful Soup
    * (For colab user) Colab
    * (Optional) Scrapy
5. `CSV` 파일로 저장하실때 Unicode로 저장하셔야 하며, Excel에서 문제 없이 열 수 있어야 합니다.
6. `CSV` 파일은 쉼표로 구분되어야 합니다.
7. `CSV` 파일의 레코드 형식은 다음과 같습니다.
  * movie - 영화 이름이 들어갑니다. 문자열입니다.
  * sentence - 한줄평이 들어갑니다. 문자열입니다.
  * score - 별점이 들어갑니다. 숫자입니다.
8. 크롤링 코드를 실행하여 크롤링을 한 번에 완료해야 합니다.
9. 그외 상세한 구현 방법은 자율입니다.

### 과제를 제출하실때 다음을 제출해야합니다.
1. 크롤링된 데이터를 저장한 `samples.csv`
2. 크롤링 코드

### 제출 코드


```python
import requests
from bs4 import BeautifulSoup
import csv
import time

# open csv
fd = open("samples.csv", "w", encoding='utf-8')
writer = csv.writer(fd)
writer.writerow(["movie", "sentence", "score"])


print("크롤링 시작..")
for idx in range(1, 150):
    if idx % 10 == 0:
            print(f"크롤링 중.. iter={idx}")

    # DDOS 공격 의심을 피하기 위한 sleep
    time.sleep(0.5)

    uri = f"https://movie.naver.com/movie/point/af/list.naver?&page={idx}"

    gain = requests.get(uri)
    html = BeautifulSoup(gain.content, 'html.parser')

    # 유의미한 내용이 담긴 content까지 접근
    dep0 = html.find("tbody")
    dep1 = dep0.findAll("tr")
    for i in range(len(dep1)):
        dep2 = dep1[i].find("td", {"class": "title"})
        dep3 = dep2.text

        # parsing
        content = dep3.split('\n')
        movie_review = content[5]
        if not movie_review: continue

        movie_title = content[1]
        movie_score = int(content[3].split('중')[-1])

        # to csv
        writer.writerow([movie_title, movie_review, movie_score])

print("완료!")
fd.close()
```

    크롤링 시작..
    크롤링 중.. iter=10
    크롤링 중.. iter=20
    크롤링 중.. iter=30
    크롤링 중.. iter=40
    크롤링 중.. iter=50
    크롤링 중.. iter=60
    크롤링 중.. iter=70
    크롤링 중.. iter=80
    크롤링 중.. iter=90
    크롤링 중.. iter=100
    크롤링 중.. iter=110
    크롤링 중.. iter=120
    크롤링 중.. iter=130
    크롤링 중.. iter=140
    완료!


## 2-2. 네이버 영화 데이터 셋 제작 (30점)
`CSV` 파일로 저장된 데이터를 쉽게 접근하기 위해서는 파이썬 내에서 구조화할 필요가 있습니다.
이를 위하여 데이터에 접근 가능한 `RawMovieReview` 클래스를 만들어 봅시다.


### `RawMovieReview` 클래스는 다음을 준수해야 합니다.
0. 이하 모든 클래스 공통 사항
    * 클래스 속성은 사용이 금지됩니다.
    * 전역 변수 사용이 금지됩니다.
1. 생성자
    * 생성자의 인자는 `str`타입의 `file_name` 하나만을 받습니다.
    * `file_name` 인자의 기본값은 `"samples.csv"`입니다.
    * 해당 객체는 해당 파일을 다루는 객체가 되어야 합니다.
    * 모든 속성 값은 `protected` 홋은 `private`이어야 합니다. 즉, 메소드만 `public`입니다.
2. Indexing
    * 대괄호로 N번째 sample에 접근할 수 있어야 합니다.
    * N은 0부터 시작합니다. 즉, `dataset[0]`은 첫번째 한줄 평 입니다.
    * Indexing 결과값은 `영화 이름, 한줄평, 점수`로 타입은 `(str, str, int)` 형태의 튜플입니다.
    * 대괄호로 읽기만 가능하고 수정은 불가능해야 합니다.
3. Length
    * `len(dataset)`의 형태로 데이터셋 내의 한줄평 개수를 조회할 수 있어야 합니다.

### 과제를 제출하실때 다음을 제출해야합니다.
1. `RawMoviewReview` 클래스가 정의된 코드 (`.py` 혹은 `.ipynb`)

### 제출 코드


```python
import csv
from collections import namedtuple


class RawMoviewReview(object):
    def __init__(self, file_name: str = "samples.csv"):
        self._file_name = file_name
        self._dataset = self.disk2program(file_name)

    def __len__(self):
        return len(self._dataset)

    def __getitem__(self, idx):
        return self._dataset[idx]

    def disk2program(self, file_name):
        MovieInfo = namedtuple("MovieInfo", ['title', 'comment', 'score'])
        with open(file_name, "r") as fd:
            reader = csv.reader(fd)

            return_data = []
            next(reader)  # skip first row
            for row_info in reader:
                title, comment, score = row_info
                info_obj = MovieInfo(title, comment, int(score))
                return_data.append(info_obj)
        return return_data


if __name__ == "__main__":
    dataset = RawMoviewReview()
    print(f"dataset[0] = {dataset[0]}")
    print(f"len(dataset) = {len(dataset)}")
    dataset[1] = 1  # get an error
```

    dataset[0] = MovieInfo(title='디어 에반 핸슨', comment='이미 뮤지컬을 알고 넘버들을 좋아한 사람으로 개인적으로 영화를 보고 난 후유증이 컸습니다. 같이 본 제 친구들은 아쉬웠다고 하지만 저는 주인공의 상황과 감정에 너무 공감이 가서 계속 생각이 나네요. 하지만 원작과 내용을 모르고 보는 분들에게는 확실히 내용의 찝찝함? 아쉬움이 남을거라 생각이 들긴해요. 저 혼자 조용히 인생영화에 포함되는 거 같아 아쉽지만 위로를 바라시는 분들은 한 번은 봐보라고 하고싶네요. ', score=10)
    len(dataset) = 1398



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /var/folders/57/3hb2xgp11zd1zyhd1zv6q15r0000gn/T/ipykernel_32092/955970832.py in <module>
         32     print(f"dataset[0] = {dataset[0]}")
         33     print(f"len(dataset) = {len(dataset)}")
    ---> 34     dataset[1] = 1  # get an error
    

    TypeError: 'RawMoviewReview' object does not support item assignment


## 2-3. 네이버 영화 학습 데이터 셋 제작 (30점)
위에서 제작한 데이터 셋은 `CSV` 파일을 모두 조회하지만, 학습에 바로 사용되기에는 다소 불편합니다.
따라서 이를 상속한 `MovieReview`를 만들어 봅시다. 

### `MovieReview` 클래스는 다음을 준수해야 합니다.
1. 상속
    * 위에서 정의한 `RawMoviewReview` 클래스를 상속받아야합니다.
    * `RawMoviewReview` 내의 데이터를 복사하면 안됩니다.
    * 즉, 저장된 `CSV`파일은 부모 클래스의 속성 혹은 메소드로 접근해야합니다.
2. 생성자
    * 생성자의 인자는 부모의 인자와 `int`타입의 `score_threshold`를 받습니다.
    * 해당 클래스에는 `CSV`파일 및 그 내용이 속성으로 들어가면 안됩니다.
    * 즉, 영화 데이터는 부모에만 저장되어야합니다.
3. Indexing
    * 부모의 Indexing을 재정의합니다. (Overriding)
    * 기본적인 기능은 부모의 기능과 비슷하나 이하의 사항이 다릅니다.
    * Indexing 결과 값은 `한줄평, 긍부정`으로 타입은 `(str, bool)` 형태의 튜플입니다.
    * 점수가 객체의 `score_threshold` 이상일 경우 긍정이 `True`, 미만이면 `False` 입니다.
    * 한줄평 string의 경우 양쪽에 공백이 없어야 합니다.

### 과제를 제출하실때 다음을 제출해야합니다.
1. `MoviewReview` 클래스가 정의된 코드 (`.py` 혹은 `.ipynb`)

### 제출 코드


```python
class MoviewReview(RawMoviewReview):
    def __init__(self, score_threshold: int, file_name: str = "samples.csv"):
        super().__init__(file_name)
        self._score_threshold = score_threshold

    def __getitem__(self, idx):
        positive_or_negative = self._dataset[idx].score >= self._score_threshold
        return self._dataset[idx].comment.strip(), positive_or_negative


if __name__ == "__main__":
    dataset = MoviewReview(score_threshold=5)
    print(dataset[2])
```

    ('배우들의 연기와 ost는 정말 좋았다.하지만 주인공의 감정선도 이해할 수 없었고,전체적으로 점점 영화가 지루해져갔다.최근 본 영화 중 가장 최악...', False)


## 최종 제출
* 모든 파일을 `zip`으로 압축하여 `HW2_<한글 이름>.zip` 형태로 제출합니다.


## 채점 기준 표
각각의 문제에 대해서 이하의 감점이 각각 들어갈 수 있습니다. 음수 점수는 없습니다.
아래의 채점 기준표는 확정이 아니며, 추후 수정된 점수 기준이 적용될 수 있습니다.

감점요소 | 설명 | 감점 점수
-----|-----|-----
API 문서와 다른 입출력 | 과제 내 명시된 API 및 포멧과 입출력이 다릅니다. | -15
비효율적인 시간복잡도 | 시간복잡도가 최선이 아닙니다. (크롤링 $O(N)$, Indexing $O(1)$)| -10
비효율적인 공간 구조 | 부모 자식간 데이터가 중복하는 형태로 클래스가 작성되어 있습니다. | -10
명시되어 있지 않은 외부 라이브러리 사용 | 지정된 라이브러리 외에 다른 라이브러리를 사용하였습니다 | -10
권장하지 않는 문법 | 전역 변수나 클래스 속성을 사용하였습니다. | -10
