import React, { useEffect , useState } from 'react'
import './HomePage.css'
import CoinsContainer from 'Components/HomePage/CoinsContainer'

interface LogProps {
    value: any;
}

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

function HomePage({ value }: LogProps) {
    const [ownedCoins, setOwnedCoins] = useState<any>([{}])
    const [ownedRTCoins, setOwnedRTCoins] = useState<any>({})
    const [top20Coins, setTop20Coins] = useState<any>([{}])
    const [top20RTCoins, setTop20RTCoins] = useState<any>({})
    
    const response = async () => {
        setOwnedCoins(await getOwnedCoins())
        setTop20Coins(await getTop20Coins())
    }
    
    const rtResponse = async () => {
        setOwnedRTCoins(await getOwnedRealTimeCoins())
        setTop20RTCoins(await getTop20RealTimeCoins())
    }

    useEffect(() => {
        response()
        setInterval(() => {
            rtResponse()
        }, 10_000)
    }, [])

    // console.log(ownedCoins)
    // console.log(ownedRTCoins)
    // console.log(top20Coins)
    // console.log(top20RTCoins)
    return (
        <>
            <div className='homeContainer'>
                <CoinsContainer ownedCoins={ ownedCoins } ownedRTCoins={ ownedRTCoins } 
                                top20Coins={ top20Coins } top20RTCoins={ top20RTCoins }
                                logs={ value }
                />
            </div>
        </>
    )
}

export default HomePage