import React from 'react'

interface CoinInfo {
    buyPrice?: number;
    buyTime?: string;
    fee?: number;
    name?: string;
    ticker?: string;
}

function ChartItem({ buyPrice, buyTime, fee, name, ticker}: CoinInfo) {
    return (
        <>
            <div>{ buyPrice }</div>
            <div>{ buyTime }</div>
            <div>{ fee }</div>
            <div>{ name }</div>
            <div>{ ticker }</div>
        </>
    )
}

export default ChartItem