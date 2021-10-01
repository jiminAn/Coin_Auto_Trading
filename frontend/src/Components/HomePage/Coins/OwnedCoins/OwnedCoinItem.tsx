/* eslint-disable prefer-destructuring */
import React from 'react'
import moment from 'moment-timezone'
import './OwnedCoinItem.css'

interface CoinInfo {
    buyPrice?: number; // 구매가
    buyTime?: string; // 구매 시점
    fee?: number;
    name?: string; // 코인 이름(KR)
    quantity?: number; // 보유 자산
    ticker?: string; // 코인 약어
    setTicker?: any; // setting
}

function OwnedCoinItem({ buyPrice, buyTime, fee, name, quantity, ticker, setTicker}: CoinInfo) {
    // TODO :: 예외처리 -> ""가 넘어왔을 때 예외 처리 필요 -> 없을 때 렌더링되는 값이 다르도록
    let date = ""
    let time = ""
    if(buyTime !== "") {
        const kstTime = moment(buyTime).tz('Asia/Seoul').format().split('T')
        date = kstTime[0] // 2021-09-08
        time = kstTime[1].split('+')[0] // 20:24:45
    }
    const onClick = () => {
        setTicker(ticker)
    }

    return (
        <div className='ownedCoinItemContainer' onClick={ onClick }>
            <div className='ownedCoinItem'>
                <div className='name'>{ name }</div>
                <div className='ticker'>/{ ticker }</div>
            </div>
            <div className='ownedCoinItem'>{ buyPrice?.toLocaleString('ko-KR') }</div>
            <div className='ownedCoinItem'>{ quantity }</div>
            <div className='ownedCoinItem'>
                <div>{ date }</div>
                <div>{ time }</div>
            </div>
        </div>
    )
}

export default OwnedCoinItem