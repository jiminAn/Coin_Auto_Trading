import React from 'react'
import './ChartItem.css'

interface ChartValueProps {
    category?: string;
    value?: number | string;
}

function ChartItem({ category, value }: ChartValueProps) {
    return (
        <div className='chartItem'> 
            <div className='category'>{ category }</div>
            <div >{ value }</div>
        </div>
    )
}

export default ChartItem