import React from 'react'
import './GlobalNavigationBar.css'

function GlobalNavigationBar() {
    return (
        <div className="NavigationContainer">
            <nav>
                <div className='title'>
                    <a href='/'>손절이 나의 멘탈을 지킨다.</a>
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