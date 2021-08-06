import React from 'react'
import './GlobalNavigationBar.css'

interface LoginInfo {
    isLogin: boolean
}

function GlobalNavigationBar({ isLogin }: LoginInfo) {
    return (
        <div className="NavigationContainer">
            <nav>
                <div className='title'>
                    { !isLogin ?
                        <a href='/'>손절이 나의 멘탈을 지킨다.</a> :
                        <a href='/home'>손절이 나의 멘탈을 지킨다.</a>
                    }
                </div>
                <ul>
                    <li><div className='menu'>자동거래</div></li>
                    <li><div className='menu'>거래소</div></li>
                    <li><div className='menu'>도움말</div></li>
                </ul>
            </nav>
        </div>
    )
}

export default GlobalNavigationBar