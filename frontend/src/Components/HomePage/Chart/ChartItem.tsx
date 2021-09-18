import React from 'react'
import moment from 'moment-timezone'
import './ChartItem.css'

interface CoinInfo {
    buyPrice?: number; // 구매가
    buyTime?: string; // 구매 시점
    fee?: number;
    name?: string; // 코인 이름(KR)
    quantity?: number; // 보유 자산
    ticker?: string; // 코인 약어
}

function ChartItem({ buyPrice, buyTime, fee, name, quantity, ticker}: CoinInfo) {
    const kstTime = moment(buyTime).tz('Asia/Seoul').format().split('T')
    const date = kstTime[0] // 2021-09-08
    const time = kstTime[1].split('+')[0] // 20:24:45

    return (
        <div className='chartItemContainer'>
            <div className='chartItem'>
                <div className='name'>{ name }</div>
                <div className='ticker'>/{ ticker }</div>
            </div>
            <div className='chartItem'>{ buyPrice?.toLocaleString('ko-KR') }</div>
            <div className='chartItem'>{ quantity }</div>
            <div className='chartItem'>
                <div>{ date }</div>
                <div>{ time }</div>
            </div>
            {/* <div className='chartItem'>{ fee }</div> */}
        </div>
    )
}

export default ChartItem