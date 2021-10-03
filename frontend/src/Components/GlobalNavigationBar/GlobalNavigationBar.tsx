import React, { useState, useEffect } from 'react'
import './GlobalNavigationBar.css'

// 거래 시작 주소
async function startTrading(flag: string) {
    return fetch('http://localhost:5000/coin/start', {
        // method: 'GET',
        // body: flag
    })
    .then(data => data.json())
}

// 거래 취소 주소
async function quitTrading(flag: string) {
    return fetch('http://localhost:5000/coin/start', {
        // method: 'GET',
        // body: flag
    })
}

function GlobalNavigationBar() {
    const [isStart, setIsStart] = useState<boolean>(true)

    const onSubmit = async (e: any) => {
        e.preventDefault()
        if(isStart) console.log('거래를 시작합니다.')
        else console.log('거래를 종료합니다.')
        // NOTICE :: 서버 작업 완료 시 주석 해제
        if(isStart) await startTrading(isStart.toString())
        else await quitTrading(isStart.toString())

        setIsStart(!isStart)
    }

    return (
        <div className="NavigationContainer">
            <nav>
                <div className='title'>
                    <a href='/' className='logo'>손절이 나의 멘탈을 지킨다.</a>
                </div>
                {/* 자동매매 시작 버튼 생성 */}
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