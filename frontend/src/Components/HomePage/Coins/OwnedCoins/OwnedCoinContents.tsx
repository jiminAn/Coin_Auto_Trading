import React from 'react'
import './OwnedCoinContents.css'

function OwnedCoinContents() {
    return (
        <div className='ownedCoinItemContainer'>
            <div className='ownedCoinContent'>
                <div>자산</div><br/>
                <div>현재가(원)</div>
            </div>
            <div className='ownedCoinContent'>
                <div>구매가(원)</div><br/>
                <div>변동금액(원)</div>
            </div>
            <div className='ownedCoinContent'>
                <div>수량</div><br/>
                <div>변동률(%)</div>
            </div>
            <div className='ownedCoinContent'>
                <div>구매시간</div><br/>
                <div>누적거래금액(원)</div>
            </div>
        </div>
    )
}

export default OwnedCoinContents