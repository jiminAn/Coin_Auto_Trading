/* eslint-disable prefer-destructuring */
/* eslint-disable camelcase */
import React, { useState, useEffect } from 'react'
import moment from 'moment-timezone'
import './ChartContainer.css'

interface CoinInfo {
    // 공통 정보
    name?: string;
    ticker?: string;
    // 코인 정보
    open?: number;
    close?: number;
    low?: number;
    high?: number;
    volume?: number;
    // 나의 보유 코인 정보
    buy_price?: number; // 구매가
    buy_time?: string; // 구매 시점
    fee?: number;
    quantity?: number; // 보유 자산
}

function ChartContainer({ buy_price, buy_time, fee, name, quantity, ticker,
                          open, close, low, high, volume }: CoinInfo) {
    // TODO :: 비어 있는 객체를 받았을 때 처리(임시처리되어있음)
    let date = ""
    let time = ""
    if(buy_time !== "") {
        const kstTime = moment(buy_time).tz('Asia/Seoul').format().split('T')
        date = kstTime[0] // 2021-09-08
        time = kstTime[1].split('+')[0] // 20:24:45
    } else {
        return <div>값 없음</div> // TODO :: 확인해보기
    }
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
                <div className='chartTitle'>{ open?.toLocaleString('ko-KR') }</div>
                <div className='chartTitle'>{ close?.toLocaleString('ko-KR') }</div>
                <div className='chartTitle'>{ low?.toLocaleString('ko-KR') }</div>
                <div className='chartTitle'>{ high?.toLocaleString('ko-KR') }</div>
                <div className='chartTitle'>{ volume?.toLocaleString('ko-KR') }</div>
            </div>
        </>
    )
}

export default ChartContainer