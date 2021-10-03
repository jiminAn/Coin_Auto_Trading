/* eslint-disable prefer-destructuring */
/* eslint-disable camelcase */
import React, { useState, useEffect } from 'react'
import moment from 'moment-timezone'
import './ChartContainer.css'
import ChartItem from './ChartItem'

interface CoinInfo {
    // 보유 코인인지, 상위 코인인지
    type?: 'owned' | 'top';
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

function ChartContainer({ type, buy_price, buy_time, fee, name, quantity, ticker,
                          open, close, low, high, volume }: CoinInfo) {

    let date = ""
    let time = ""
    if(buy_time !== "") {
        const kstTime = moment(buy_time).tz('Asia/Seoul').format().split('T')
        date = kstTime[0] // 2021-09-08
        time = kstTime[1].split('+')[0] // 20:24:45
    } else {
        return <div>값 없음</div>
    }

    return (
        <>
            <div className='chartContainer'>
                <div className='chartTitle'>{ name } / { ticker }</div>
                { type === 'owned' &&
                    <div className='info'>
                        <div className='chartSubTitle'>소유 정보</div>
                        <ChartItem category='구매가(원)' value={ buy_price?.toLocaleString('ko-KR') } />
                        <ChartItem category='보유 수량' value={ quantity?.toLocaleString('ko-KR') } />
                        <ChartItem category='구매 일자' value={ `${date} ${time}`} />
                        <ChartItem category='수수료(원)' value={ fee?.toLocaleString('ko-KR') } />
                    </div>
                }
                <div className='info'>
                    <div className='chartSubTitle'>전일 코인 정보</div>
                    <ChartItem category='시가(원)' value={ open?.toLocaleString('ko-KR')  } />
                    <ChartItem category='종가(원)' value={ close?.toLocaleString('ko-KR') } />
                    <ChartItem category='저가(원)' value={ low?.toLocaleString('ko-KR') } />
                    <ChartItem category='고가(원)' value={ high?.toLocaleString('ko-KR') } />
                    <ChartItem category='거래량' value={ volume?.toLocaleString('ko-KR') } />
                </div>
            </div>
        </>
    )
}

export default ChartContainer