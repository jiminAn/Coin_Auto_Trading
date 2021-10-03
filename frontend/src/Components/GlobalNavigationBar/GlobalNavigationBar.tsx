import React, { useState, useEffect } from 'react'
import './GlobalNavigationBar.css'

interface LogProps {
    setLogs?: any;
}

// 거래 시작 주소
async function startTrading() {
    return fetch('http://localhost:5000/coin/start')
    .then(data => data.json())
}

// 거래 취소 주소
async function quitTrading() {
    return fetch('http://localhost:5000/coin/start')
    .then(data => data.json())
}

function GlobalNavigationBar({ setLogs }: LogProps) {
    const [isStart, setIsStart] = useState<boolean>(true)

    const onSubmit = async (e: any) => {
        e.preventDefault()
        if(isStart) {
            console.log('거래를 시작합니다.')
            await startTrading()
        } else {
            console.log('거래를 종료합니다.')
            setLogs(await quitTrading())
        }
        setIsStart(!isStart)
    }

    return (
        <div className="NavigationContainer">
            <nav>
                <div className='title'>
                    <a href='/' className='logo'>손절이 나의 멘탈을 지킨다.</a>
                </div>
                <ul>
                    <li><div className='menu'>자동거래</div></li>
                    <li><div className='menu'>거래소</div></li>
                    <li><div className='menu'>도움말</div></li>
                    { isStart ?
                        <button type='button' className='tradingBtn' onClick={ onSubmit }>거래 시작</button> :
                        <button type='button' className='tradingBtn quit' onClick={ onSubmit }>거래 종료</button>
                    }
                </ul>
            </nav>
        </div>
    )
}

export default GlobalNavigationBar