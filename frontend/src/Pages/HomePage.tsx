import React, { useEffect , useState } from 'react'
import './HomePage.css'
import ChartContainer from 'Components/HomePage/Chart/ChartContainer'
import SalesContainer from 'Components/HomePage/Sales/SalesContainer'

async function getCoins() {
    return fetch('http://localhost:5000/coin')
    .then(data => data.json())
}

/* TODO
    1. 화면 다시 켜질 때 다시 로그인하도록 하는 것 -> sessionStorage 확인
    2. sales에서 초기값은 가장 먼저 있는 놈으로 뜨도록 설정
*/

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
            <SalesContainer prevCoins={ coins }/>
            <ChartContainer coins={ coins }/>
        </div>
    )
}

export default HomePage