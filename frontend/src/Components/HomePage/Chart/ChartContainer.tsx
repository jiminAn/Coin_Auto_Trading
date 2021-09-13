/* eslint-disable camelcase */
import React from 'react'
import './ChartContainer.css'
import ChartItem from './ChartItem'

interface CoinInfo {
    buy_price?: number;
    buy_time?: string;
    fee?: number;
    name?: string;
    quantity?: number;
    ticker?: string;
}

interface Coins {
    coins: [CoinInfo]
}

function ChartContainer({ coins }: Coins) {
    return (
        <>
            <div className='chartContainer'>
                <div className='chartTitle'>나의 보유 자산</div>
                <div className='chartItems'>
                    <ChartItem key="classifier" buyPrice="Buy Price" buyTime="Buy Time" fee="Fee" name="Name" quantity="Quantity" ticker="ticker" />
                    { coins.map((coin) => (
                        <ChartItem key={coin.ticker} buyPrice={coin.buy_price} buyTime={coin.buy_time} fee={coin.fee} name={coin.name} quantity={coin.quantity} ticker={coin.ticker} />
                    ))}
                </div>
            </div>
        </>
    )
}

export default ChartContainer