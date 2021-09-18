import React from 'react'
import './SalesContents.css'

function SalesContents() {
    return (
        <div className='salesItemContainer'>
            <div className='salesContent'>자산</div>
            <div className='salesContent'>고가(원)</div>
            <div className='salesContent'>저가(원)</div>
            <div className='salesContent'>시가(원)</div>
            <div className='salesContent'>종가(원)</div>
            <div className='salesContent'>거래량</div>
        </div>
    )
}

export default SalesContents