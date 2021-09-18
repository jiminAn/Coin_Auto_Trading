import React from 'react'
import './SalesContainer.css'
import SalesContents from './SalesContents'
import SalesItem from './SalesItem'

interface PrevCoinInfo {
    name?: string;
    ticker?: string;
    open?: number;
    close?: number;
    low?: number;
    high?: number;
    volume?: number;
}

interface PrevCoins {
    prevCoins: [PrevCoinInfo]
}

function SalesContainer({ prevCoins }: PrevCoins) {
    return (
        <div className='salesContainer'>
            <div className='salesTitle'>나의 보유 자산 정보</div>
            <div className='salesItems'>
                <SalesContents />
                { prevCoins.map((coin) => (
                    <SalesItem key={coin.ticker} name={coin.name} ticker={coin.ticker} open={coin.open} close={coin.close} high={coin.high} low={coin.low} volume={coin.volume}/>
                ))}
            </div>
        </div>
    )
}

export default SalesContainer