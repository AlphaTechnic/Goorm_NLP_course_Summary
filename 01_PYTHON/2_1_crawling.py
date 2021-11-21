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
