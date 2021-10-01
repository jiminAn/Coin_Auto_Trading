/* eslint-disable camelcase */
import React, { useState, useEffect } from 'react'
import moment from 'moment-timezone'
import './ChartContainer.css'

interface CoinInfo {
    buy_price?: number;
    buy_time?: string;
    fee?: number;
    name?: string;
    quantity?: number;
    ticker?: string;
}

function ChartContainer({ buy_price, buy_time, fee, name, quantity, ticker }: CoinInfo) {
    // TODO :: 비어 있는 객체를 받았을 때 처리
    const kstTime = moment(buy_time).tz('Asia/Seoul').format().split('T')
    const date = kstTime[0] // 2021-09-08
    const time = kstTime[1].split('+')[0] // 20:24:45
    // TODO :: 디자인 수정
    return (
        <>
            <div className='chartContainer'>
                <div className='chartTitle'>{ ticker }</div>
                <div className='chartTitle'>{ buy_price?.toLocaleString('ko-KR') }</div>
                <div className='chartTitle'>{ date } { time }</div>
                <div className='chartTitle'>{ fee }</div>
                <div className='chartTitle'>{ name }</div>
                <div className='chartTitle'>{ quantity }</div>
            </div>
        </>
    )
}

export default ChartContainer