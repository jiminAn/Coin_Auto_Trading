import React from 'react'
import './SalesItem.css'

interface PrevCoinInfo {
    name?: string;
    ticker?: string;
    open?: number; // 시가
    close?: number; // 종가
    low?: number; // 저가
    high?: number; // 고가
    volume?: number; // 전일 거래량
}

function SalesItem({ name, ticker, open, close, low, high, volume }: PrevCoinInfo) {
    return (
        <div className='salesItemContainer'>
                <div className='salesItem'>
                    <div className='name'>{ name }</div>
                    <div className='ticker'>/{ ticker }</div>
                </div>
                <div className='salesItem'>{ high?.toLocaleString('ko-KR') }</div>
                <div className='salesItem'>{ low?.toLocaleString('ko-KR') }</div>
                <div className='salesItem'>{ open?.toLocaleString('ko-KR') }</div>
                <div className='salesItem'>{ close?.toLocaleString('ko-KR') }</div>
                <div className='salesItem'>{ volume?.toLocaleString('ko-KR') }</div>
        </div>
    )
}

export default SalesItem