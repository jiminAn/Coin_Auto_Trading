# Backend



## 파일 계층 구조

- `./backend`
  - `./idea`
  - `./migrations : DB 생성을 위한 초기화 폴더`    
  - `./src : 백엔드 소스 디렉토리`
    - `./crawling : 크롤링 및 전처리 관련 폴더` 
      - CrawledInfo.py : 티커네임 크롤링 데이터를 전처리하여 딕셔너리로 반환
      - WebCrawler.py : 티커네임 크롤러
    - `./model : DB table 정의 및 업데이트 관련 폴더`                      
      - models.py : Coin, Client 테이블 컬럼 및 제약 지정   
      - Update.py : Coin, Client 테이블의 데이터 업데이트 관련 모듈      
    - `./pybithumb : bithumb api 관련 모듈 정의` 
      - ApiConnect.py : client API 연결 및 클라이언트의 빗썸 인스턴스 반환
      - ClientAsset.py : client 보유 자산 정보 조회 및 반환
      - RealTimeWebsocketProcess.py : 실시간 웹소켓 처리 코드
    - `./views : front<->back 데이터 전송 관련 뷰 ` 
      - main_view.py : 로그인/코인 정보 및 개인 자산 로딩/코인자동매매 뷰
    - .gitignore : git push 시, 무시할 파일 정의
    - _ _ init _ _.py: app에 Flask 와 db, 뷰 연결
    - bestk.py : k값 계산 코드
    - bitcoinAutoTrade.py : 코인자동매매 코드
    - coin.db : Coin, Client 데이터 테이블
    - coin.ini : 티커네임과 로그를 읽어오기 위한 path 설정 파일 
    - config.py : 환경설정
    - database.py : db 관련 객체 생성 파일
    - tickernames.txt : 티커네임 크롤링 원본 파일
  - .gitignore : git push 시, 무시할 파일 정의
  - Pipfile : 소스, 패키지, dev 패키지, requires 저장 파일
  - main.py : 서버 실행 파일
  - requirements.txt : 라이브러리 버전 



## API Information

------

### 1. /coin : 코인 구매 정보

```
{
	buy_price : number, 구매 가격
	buy_time : string, 구매 날짜
	close : number, 종가
	fee : float, 수수료
	high : number, 고가
	low : number, 저가
	name : string, 코인 이름
	open : number, 시가
	quantity: float, 보유 수량
	ticker : string, ticker명
	volume : float, 전일 거래량
}
```

### 2. /coin/clientassets : 보유하고 있는 코인의 실시간 정보

```
{
	ticker : string, ticker명
	accu_price : float, 누적거래금액
  	chg_rate : float, 변동금액
	cur_price : float, 현재금액
}
```

### 3. /coin/tickers_20 : 상위 20개 코인의 실시간 정보

- 해당하는 코인의 실시간으로 변경되는 값들이 ticker를 key로 하는 json으로 전송됨

```
{ ticker : ticker_KRW 형태로 명시됨(BTC_KRW)
	{
		chgAmt : string(number), 변동금액
		chgRate  : string(float), 변동률
		cur_price : number, 현재가
		ticker : string, ticker명
		value: string(float), 누적거래금액
	}
}
```

### 4. /coin/tickers_db : 상위 20개 코인의 고정된 정보들

* 상위 20개 코인의 정보들 배열에 담겨서 전송됨.
* /coin에서 거래금액, 보유량, 수수료를 제외한 것과 유사

```
{
	close : number, 종가
	datetime: string, 업데이트 날짜 -> 미사용
	high : number, 고가
	low : number, 저가
	name : string, 코인 이름
 	open : number, 시가
	ticker : string, ticker명
	volume : float, 전일 거래
}
```

