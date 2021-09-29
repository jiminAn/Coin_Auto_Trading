import React, { useEffect , useState } from 'react'
import './HomePage.css'
import ChartContainer from 'Components/HomePage/Chart/ChartContainer'
import CoinsContainer from 'Components/HomePage/Coins/CoinsContainer'

async function getCoins() {
    return fetch('http://localhost:5000/coin')
    .then(data => data.json())
}

function HomePage() {
    const [coins, setCoins] = useState<any>([{
        buyPrice: 0, buyTime: "", fee: 0, name: "", quantity: 0, ticker: "",
        high: 0, low: 0, open: 0, close: 0, volume: 0
    }])
    const response = async () => {
        setCoins(await getCoins())
    }

    useEffect(() => {
        response()
    }, [])

    // console.log(coins)
    return (
        <div className='homeContainer'>
            {/* coins정보 전달 */}
            <CoinsContainer coins={ coins } />
            <ChartContainer coins={ coins }/>
        </div>
    )
}

export default HomePage