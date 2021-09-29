/* eslint-disable camelcase */
import React, { useState } from 'react'
import './CoinsContainer.css'
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

function SalesContainer({ coins }: Coins) {
    const [isOwned, setIsOwned] = useState<boolean>(true)
    const [isRealTime, setIsRealTime] = useState<boolean>(false)

    const ownedClickListener = () => {
        setIsOwned(true)
        setIsRealTime(false)
    }

    const realTimeClickListener = () => {
        setIsOwned(false)
        setIsRealTime(true)
    }

    return (
        <div className='coinsContainer'>
            <div className='tabContainer'>
                <button type='button' className='tabBtn' onClick={ ownedClickListener }>나의 보유 자산 정보</button>
                <button type='button' className='tabBtn' onClick={ realTimeClickListener }>실시간 코인 정보</button>
            </div>
            { isOwned ?
                <div className='coinInfoContainer'>
                    <OwnedCoinContents />
                    { coins.map((coin) => (
                        <OwnedCoinItem key={coin.ticker} buyPrice={coin.buy_price} buyTime={coin.buy_time} fee={coin.fee} name={coin.name} quantity={coin.quantity} ticker={coin.ticker} />
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
    )
}

export default SalesContainer