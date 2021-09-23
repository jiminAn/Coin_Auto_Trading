import React from 'react'
import './OwnedCoinContents.css'

function OwnedCoinContents() {
    return (
        <div className='ownedCoinItemContainer'>
            <div className='ownedCoinContent'>자산</div>
            <div className='ownedCoinContent'>구매가(원)</div>
            <div className='ownedCoinContent'>수량</div>
            <div className='ownedCoinContent'>구매시간</div>
        </div>
    )
}

export default OwnedCoinContents