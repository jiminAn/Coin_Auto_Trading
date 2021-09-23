import React from 'react'
import './CoinInfoContents.css'

function CoinInfoContents() {
    return (
        <div className='coinInfoContentsContainer'>
            <div className='coinInfoContent'>자산</div>
            <div className='coinInfoContent'>고가(원)</div>
            <div className='coinInfoContent'>저가(원)</div>
            <div className='coinInfoContent'>시가(원)</div>
            <div className='coinInfoContent'>종가(원)</div>
            <div className='coinInfoContent'>거래량</div>
        </div>
    )
}

export default CoinInfoContents