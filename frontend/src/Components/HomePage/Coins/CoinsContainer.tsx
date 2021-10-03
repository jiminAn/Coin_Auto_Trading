/* eslint-disable camelcase */
import React, { useState, useEffect } from 'react'
import './CoinsContainer.css'
import ChartContainer from 'Components/HomePage/Chart/ChartContainer'
import CoinInfoContents from 'Components/HomePage/Coins/CoinsInfo/CoinInfoContents'
import CoinInfoItem from 'Components/HomePage/Coins/CoinsInfo/CoinInfoItem'
import OwnedCoinContents from 'Components/HomePage/Coins/OwnedCoins/OwnedCoinContents'
import OwnedCoinItem from 'Components/HomePage/Coins/OwnedCoins/OwnedCoinItem'
import RTCoinItem from './RTCoins/RTCoinItem'

// 보유 코인 정보(고정)
interface OwnedCoinInfo {
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

// 상위 20개 코인 정보(고정)
interface Top20CoinInfo {
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
    datetime?: string; // 구매 시점
}

interface Coins {
    ownedCoins: [OwnedCoinInfo]
    ownedRTCoins: any;
    top20Coins: [Top20CoinInfo]
    top20RTCoins: any;
}

const ACTIVEBTN = 'tabBtn'
const DEACTIVEBTN = 'tabBtn deactiveBtn'

function SalesContainer({ ownedCoins, ownedRTCoins, top20Coins, top20RTCoins }: Coins) {
    const [isOwned, setIsOwned] = useState<boolean>(true)
    const [owned, setOwned] = useState<string>(ACTIVEBTN)
    const [realTime, setRealTime] = useState<string>(DEACTIVEBTN)
    const [ticker, setTicker] = useState<string>('default')
    
    useEffect(() => {
        // console.log(ticker)
    }, [ticker])

    const ownedClickListener = () => {
        setIsOwned(true)
        setOwned(ACTIVEBTN)
        setRealTime(DEACTIVEBTN)
    }

    const realTimeClickListener = () => {
        setIsOwned(false)
        setOwned(DEACTIVEBTN)
        setRealTime(ACTIVEBTN)
    }

    return (
        <>
            <div className='coinsContainer'>
                <div className='tabContainer'>
                    <button type='button' className={ owned } onClick={ ownedClickListener }>나의 보유 자산 정보</button>
                    <button type='button' className={ realTime } onClick={ realTimeClickListener }>코인 시장 현황(20개)</button>
                </div>
                { isOwned ?
                    <div className='coinInfoContainer'>
                        <OwnedCoinContents />
                        { ownedCoins.map((coin) => {
                            const { buy_price, buy_time, fee, name, quantity, ticker } = coin
                            const rtInfo = ownedRTCoins[ticker!]

                            // console.log(ownedRTCoins)

                            return (
                                <div className='ownedCoinContainer' key={ticker}>
                                    <OwnedCoinItem buyPrice={buy_price} buyTime={buy_time} fee={fee} name={name} quantity={quantity} ticker={ticker} setTicker={ setTicker }/>
                                    <RTCoinItem rtCoin={ rtInfo }/>
                                </div>
                            )
                        })}
                    </div> : 
                    <div className='coinInfoContainer'>
                        <CoinInfoContents />
                        { top20Coins.map((coin) => { // top20 코인 항목 저장
                            const { name, ticker, open, close, high, low, volume } = coin
                            const rtInfo = top20RTCoins[ticker!]

                            // console.log(rtInfo)

                            // DEBT :: 고정된 크기의 scollView로 변경
                            return (
                                <div className='ownedCoinContainer' key={ticker}>
                                    <CoinInfoItem key={ticker} name={name} ticker={ticker} open={open} close={close} high={high} low={low} volume={coin.volume} setTicker={ setTicker }/>
                                    <RTCoinItem rtCoin={ rtInfo }/>
                                </div>
                            )
                        })}
                    </div>
                }
            </div>
            {/* DEBT :: default일 때 처리 필요, 스크롤 중앙에 위치하도록 위치 조정 */}
            { isOwned ? 
                ownedCoins.filter((coin) => coin.ticker === ticker).map((coin) => (
                    <ChartContainer type='owned' key={coin.ticker} buy_price={coin.buy_price} buy_time={coin.buy_time} fee={coin.fee} name={coin.name} quantity={coin.quantity} ticker={coin.ticker}
                                    open={coin.open} close={coin.close} high={coin.high} low={coin.low} volume={coin.volume}/>
                )) :
                top20Coins.filter((coin) => coin.ticker === ticker).map((coin) => (
                    <ChartContainer key={coin.ticker} buy_time={coin.datetime} name={coin.name} ticker={coin.ticker} 
                                    open={coin.open} close={coin.close} high={coin.high} low={coin.low} volume={coin.volume}/>
                ))
            }
            {/* 거래 로그 기록 이동 */}
        </>
    )
}

export default SalesContainer