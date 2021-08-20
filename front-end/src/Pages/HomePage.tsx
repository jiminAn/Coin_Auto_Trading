import React from 'react'
import './HomePage.css'
import ChartContainer from 'Components/HomePage/ChartContainer'
import SalesContainer from 'Components/HomePage/SalesContainer'

function HomePage() {
    return (
        <div className='homeContainer'>
            <ChartContainer />
            <SalesContainer />
        </div>
    )
}

export default HomePage