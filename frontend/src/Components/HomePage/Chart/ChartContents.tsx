import React from 'react'
import './ChartContents.css'

function ChartContents() {
    return (
        <div className='chartItemContainer'>
            <div className='chartContent'>자산</div>
            <div className='chartContent'>구매가(원)</div>
            <div className='chartContent'>수량</div>
            <div className='chartContent'>구매시간</div>
        </div>
    )
}

export default ChartContents