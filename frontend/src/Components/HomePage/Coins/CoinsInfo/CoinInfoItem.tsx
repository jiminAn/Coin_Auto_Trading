import React from 'react'
import './CoinInfoItem.css'

interface PrevCoinInfo {
    name?: string;
    ticker?: string;
    open?: number; // 시가
    close?: number; // 종가
    low?: number; // 저가
    high?: number; // 고가
    volume?: number; // 전일 거래량
}

function CoinInfoItem({ name, ticker, open, close, low, high, volume }: PrevCoinInfo) {
    return (
        <div className='coinInfoItemContainer'>
                <div className='coinInfoItem'>
                    <div className='name'>{ name }</div>
                    <div className='ticker'>/{ ticker }</div>
                </div>
                <div className='coinInfoItem'>{ high?.toLocaleString('ko-KR') }</div>
                <div className='coinInfoItem'>{ low?.toLocaleString('ko-KR') }</div>
                <div className='coinInfoItem'>{ open?.toLocaleString('ko-KR') }</div>
                <div className='coinInfoItem'>{ close?.toLocaleString('ko-KR') }</div>
                <div className='coinInfoItem'>{ volume?.toLocaleString('ko-KR') }</div>
        </div>
    )
}

export default CoinInfoItem