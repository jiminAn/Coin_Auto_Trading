/* eslint-disable camelcase */
import React from 'react'
import './RTCoinItem.css'

// NOTICE :: 숫자인데 string인 값들은 바뀔 예정
interface RTCoinInfo {
    chgAmt?: number;
    chgRate?: number;
    cur_price?: number;
    value?: number;
}

interface RTCoinProps {
    rtCoin?: RTCoinInfo
}

function RTCoinItem({ rtCoin }: RTCoinProps) {
    // props가 비어있을 경우 undefined
    if(rtCoin === undefined) {
        return (
            <div className='ownedRTCoinContainer'>
                <div className='ownedRTCoinItem'>해당 코인 정보를 불러오는 중입니다.</div>
            </div>
        )
    }
    const { chgAmt, chgRate, cur_price, value } = rtCoin
    // console.log(rtCoin)

    return (
        <div className='ownedRTCoinContainer'>
            <div className='ownedRTCoinItem'>{ cur_price?.toLocaleString('ko-KR') }</div>
            <div className='ownedRTCoinItem'>{ chgAmt?.toLocaleString('ko-KR') }</div>
            <div className='ownedRTCoinItem'>{ chgRate?.toLocaleString('ko-KR') }</div>
            <div className='ownedRTCoinItem'>{ value?.toLocaleString('ko-KR') }</div>
        </div>
    )
}

export default RTCoinItem