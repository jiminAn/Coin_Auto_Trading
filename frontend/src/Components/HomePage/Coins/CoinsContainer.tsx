/* eslint-disable camelcase */
import React, { useState, useEffect } from 'react'
import './CoinsContainer.css'
import ChartContainer from 'Components/HomePage/Chart/ChartContainer'
import CoinInfoContents from 'Components/HomePage/Coins/CoinsInfo/CoinInfoContents'
import CoinInfoItem from 'Components/HomePage/Coins/CoinsInfo/CoinInfoItem'
import OwnedCoinContents from 'Components/HomePage/Coins/OwnedCoins/OwnedCoinContents'
import OwnedCoinItem from 'Components/HomePage/Coins/OwnedCoins/OwnedCoinItem'

// NOTICE :: 상위 20개 코인 정보 대한 처리는 추후에 생각
// 보유 코인 정보
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

interface Coins {
    coins: [CoinInfo]
}

const ACTIVEBTN = 'tabBtn'
const DEACTIVEBTN = 'tabBtn deactiveBtn'

function SalesContainer({ coins }: Coins) {
    const [isOwned, setIsOwned] = useState<boolean>(true)
    const [isRealTime, setIsRealTime] = useState<boolean>(false)
    const [owned, setOwned] = useState<string>(ACTIVEBTN)
    const [realTime, setRealTime] = useState<string>(DEACTIVEBTN)
    const [ticker, setTicker] = useState<string>('default')

    // click 하면 state 저장, ChartContainer에 전달
    const ownedClickListener = () => {
        setIsOwned(true)
        setOwned(ACTIVEBTN)
        setIsRealTime(false)
        setRealTime(DEACTIVEBTN)
    }

    const realTimeClickListener = () => {
        setIsOwned(false)
        setOwned(DEACTIVEBTN)
        setIsRealTime(true)
        setRealTime(ACTIVEBTN)
    }

    useEffect(() => {
        console.log(ticker)
    }, [ticker])

    return (
        <>
            <div className='coinsContainer'>
                <div className='tabContainer'>
                    <button type='button' className={ owned } onClick={ ownedClickListener }>나의 보유 자산 정보</button>
                    <button type='button' className={ realTime } onClick={ realTimeClickListener }>실시간 코인 정보</button>
                </div>
                { isOwned ?
                    <div className='coinInfoContainer'>
                        <OwnedCoinContents />
                        { coins.map((coin) => (
                            <OwnedCoinItem key={coin.ticker} buyPrice={coin.buy_price} buyTime={coin.buy_time} fee={coin.fee} name={coin.name} quantity={coin.quantity} ticker={coin.ticker} setTicker={ setTicker }/>
                        ))}
                    </div> : <div/> 
                }
                { isRealTime ?
                    <div className='coinInfoContainer'>
                        <CoinInfoContents />
                        { coins.map((coin) => (
                            <CoinInfoItem key={coin.ticker} name={coin.name} ticker={coin.ticker} open={coin.open} close={coin.close} high={coin.high} low={coin.low} volume={coin.volume}/>
                        ))}
                    </div> : <div/>    
                }
            </div>
            {/* TODO :: default일 때 처리 필요 */}
            { coins.filter((coin) => coin.ticker === ticker).map((coin) => (
                <ChartContainer key={coin.ticker} buy_price={coin.buy_price} buy_time={coin.buy_time} fee={coin.fee} name={coin.name} quantity={coin.quantity} ticker={coin.ticker} />
            ))
            }
        </>
    )
}

export default SalesContainer