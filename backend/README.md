# Coin Auto Trading



### 백엔드 파일 계층 구조

- `./backend`
  - `./migrations`                        # DB를 관리하는 초기 파일
    - `./versions`
      - alembic.ini
      - env.py
      - README
      - script.py.mako
  - `./src`
    - `./domain`                          # http 관련
      - `./main`                       
        - _ _ init _ _.py        # model 가져오기
    - `./model`                           # DB table 정의  
      - models.py                   
    - `./pybithumb`   # bithumb api 관련 모듈 정의
      - ApiConnect.py
      - ClientAsset.py
    - `./db`      # DB data 업데이트
      - Update.py
    - `./crawling.  # 웹 크롤링
      - CrawledInfo.py 
      - WebCrawler.py
      - tickernames.txt
    - _ _ init _ _.py                       # Flask 와 DB 연결
    - config.py                             # 환경설정
    - database.py                        # DB 관련 모듈들을 모아두는 곳
    - coin.db   # Coin, Client table 
- main.py                                              # 실제 서버를 띄우는 역할
- Pipfile
