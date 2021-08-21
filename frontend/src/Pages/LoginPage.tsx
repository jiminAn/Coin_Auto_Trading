import React from 'react'
import LoginInfo from 'Components/LoginPage/LoginInfo'
import FindingAPIKey from 'Components/LoginPage/FindingAPIKey'
import './LoginPage.css'

function LoginPage() {
    // TODO :: input 태그의 값을 담기 위한 hook 설정
    // const useInput = () => {
    //     return
    // }

    // const clickEventHandler = () => {

    // }

    return (
        <div className='loginContainer'>
            <LoginInfo />
            <form>
                <input type='password' placeholder='public API key를 입력해주세요.' className='apiInput'/><br/>
                <input type='password' placeholder='private API key를 입력해주세요.' className='apiInput'/>
            </form>
            <button type='button' onClick={ () => alert('click') }>Login</button>
            <FindingAPIKey />
        </div>
    )
}

export default LoginPage