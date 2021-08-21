import React from 'react'
import './LoginInfo.css'

function LoginInfo() {
    return (
        <div className='loginInfoContainer'>
            <div className='loginTitle'>Login</div>
            <div className='loginExplanation'>
                발급받은 bithumb API Key를 알맞게 입력해주세요.
            </div>
        </div>
    )
}

export default LoginInfo