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
      - models.py : Coin, Client 테이블 컬럼 및 제약 지정         
    - `./pybithumb`   # bithumb api 관련 모듈 정의
      - ApiConnect.py : client API 연결 및 클라이언트의 빗썸 인스턴스 반환
      - ClientAsset.py : client 보유 자산 정보 조회 및 반환
    - `./update`      # DB data 업데이트 모듈 정의
      - Update.py : Coin, Client 테이블의 데이터 업데이트 관련 모듈
    - `./crawling`  # 웹 크롤링
      - CrawledInfo.py : 티커네임 크롤링 데이터를 전처리하여 딕셔너리로 반환
      - WebCrawler.py : 티커네임 크롤러
    - _ _ init _ _.py:Flask 와 DB 연결
    - config.py : 환경설정
    - database.py : DB 관련 모듈들을 모아두는 곳
    - coin.db : Coin, Client DB 
    - tickernames.txt : 티커네임 크롤링 원본 파일
- main.py : 실제 서버를 띄우는 역할
- Pipfile
