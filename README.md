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
    - `./model`                            
      - models.py                   # DB table 정의 
    - _ _ init _ _.py                       # Flask 와 DB 연결
    - config.py                             # 환경설정
    - database.py                        # DB 관련 모듈들을 모아두는 곳
    - pybo.db
- main.py                                              # 실제 서버를 띄우는 역할
- Pipfile
