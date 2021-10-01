import React, { useEffect , useState } from 'react'
import './HomePage.css'
import CoinsContainer from 'Components/HomePage/Coins/CoinsContainer'

async function getOwnedCoins() {
    return fetch('http://localhost:5000/coin')
    .then(data => data.json())
}

async function getOwnedRealTimeCoins() {
    return fetch('http://localhost:5000/coin/clientassets')
    .then(data => data.json())
}

async function getTop20Coins() {
    return fetch('http://localhost:5000/coin/tickers_db')
    .then(data => data.json())
}

async function getTop20RealTimeCoins() {
    return fetch('http://localhost:5000/coin/tickers_20')
    .then(data => data.json())
}

function HomePage() {
    const [ownedCoins, setOwnedCoins] = useState<any>([{}])
    const [realTimeOwnedCoins, setRTOwnedCoins] = useState<any>({})
    const [top20Coins, setTop20Coins] = useState<any>([{}])
    const [realTimeTop20Coins, setRTTop20Coins] = useState<any>({})
    
    const response = async () => {
        setOwnedCoins(await getOwnedCoins())
        setRTOwnedCoins(await getOwnedRealTimeCoins())
        setTop20Coins(await getTop20Coins())
        setRTTop20Coins(await getTop20RealTimeCoins())
    }

    useEffect(() => {
        response()
    }, [])

    // console.log(ownedCoins)
    // console.log(realTimeOwnedCoins)
    // console.log(top20Coins)
    // console.log(realTimeTop20Coins)
    return (
        <>
            <div className='homeContainer'>
                <CoinsContainer ownedCoins={ ownedCoins } ownedRTCoins={ realTimeOwnedCoins } 
                                top20Coins={ top20Coins } top20RTCoins={ realTimeTop20Coins }
                />
            </div>
            {/* TODO :: 자동 거래 로그 컴포넌트 작성 */}
            <div>자동 거래 로그 컴포넌트</div>
        </>
    )
}

export default HomePage