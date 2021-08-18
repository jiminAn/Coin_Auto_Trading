import React from 'react'
import LoginInfo from 'Components/LoginPage/LoginInfo'
import FindingAPIKey from 'Components/LoginPage/FindingAPIKey'
import './LoginPage.css'

function LoginPage() {
    return (
        <div className='loginContainer'>
            <LoginInfo />
            <form>
                <input type='password' placeholder='public API key를 입력해주세요.' /><br/>
                <input type='password' placeholder='private API key를 입력해주세요.' />
            </form>
            <button type='button' onClick={ () => console.log('click') }>Login</button>
            <FindingAPIKey />
        </div>
    )
}

export default LoginPage