from src.database import db

class coin_information(db.Model):
    name = db.Column(db.String(128), nullable=False)
    ticker = db.Column(db.String(10), primary_key=True, nullable=False)
    open = db.Column(db.Float) # 시작가
    high = db.Column(db.Float) # 고가
    low = db.Column(db.Float) # 저가
    close = db.Column(db.Float) # 종가
    prev_close = db.Column(db.Float) # 전날 종가
    volume = db.Column(db.Float) # 거래금액


class client_information(db.Model):
    name = db.Column(db.String(128), nullable=False)
    ticker = db.Column(db.String(10), primary_key=True, nullable=False)
    holding_krw = db.Column(db.Float) # 보유 원화 잔고
    buy_price = db.Column(db.Float) # 구매 당시 가상화폐 개당 가격 (평균)
    buy_time = db.Column(db.DateTime()) # 가상화폐 구매 시각
    buy_total_price = db.Column(db.Float) # 총 매수 금액
    quantity = db.Column(db.Float) # 가상화폐 수량