import React from 'react'
import './HomePage.css'
import ChartContainer from 'Components/HomePage/Chart/ChartContainer'
import SalesContainer from 'Components/HomePage/Sales/SalesContainer'

function HomePage() {
    return (
        <div className='homeContainer'>
            <ChartContainer />
            <SalesContainer />
        </div>
    )
}

export default HomePage