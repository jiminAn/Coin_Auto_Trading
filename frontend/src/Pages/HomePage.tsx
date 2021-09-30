import React, { useEffect , useState } from 'react'
import './HomePage.css'
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
    // const [ws, setWs] = useState<WebSocket>(new WebSocket('ws:localost:5000/coin/test'))

    const response = async () => {
        setCoins(await getCoins())
    }

    useEffect(() => {
        response()
        // ws.onopen = () => {
        //     console.log('connected !')
        // }
    }, [])

    // console.log(coins)
    return (
        <>
            <div className='homeContainer'>
                {/* coins정보 전달 */}
                <CoinsContainer coins={ coins } />
            </div>
            <div>자동 거래 로그 컴포넌트</div>
        </>
    )
}

export default HomePage