import React from 'react'
import moment from 'moment-timezone'
import './ChartItem.css'

// TODO :: 안내와 구분하고 | string 부분 제거
interface CoinInfo {
    buyPrice?: number | string; // 구매가
    buyTime?: string; // 구매 시점
    fee?: number | string;
    name?: string; // 코인 이름(KR)
    quantity?: number | string; // 보유 자산
    ticker?: string; // 코인 약어
}

function ChartItem({ buyPrice, buyTime, fee, name, quantity, ticker}: CoinInfo) {
    const time = moment(buyTime)
    console.log(time.tz('Asia/Seoul').format()) // 2021-09-08T20:24:45+09:00 -> 파싱해서 사용
    return (
        <>
            <div className='chartItemContainer'>
                <div className='chartItem'>{ name }/{ ticker }</div>
                <div className='chartItem'>{ buyPrice?.toLocaleString('ko-KR') }</div>
                <div className='chartItem'>{ quantity }</div>
                <div className='chartItem'>{ buyTime }</div>
                {/* <div className='chartItem'>{ fee }</div> */}
            </div>
        </>
    )
}

export default ChartItem