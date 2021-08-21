/* eslint-disable react/jsx-props-no-spreading */
/* eslint-disable no-shadow */
import React, { useState } from 'react'
import LoginInfo from 'Components/LoginPage/LoginInfo'
import FindingAPIKey from 'Components/LoginPage/FindingAPIKey'
import './LoginPage.css'

function useInput(defaultValue: string) {
    const [value, setValue] = useState<string>(defaultValue)

    const onChange = (e: any) => {
        const {
            target: { value }
        } = e
        setValue(value)
    }

    return { value, onChange }
}

function LoginPage() {
    const publicKey = useInput('')
    const privateKey = useInput('')

    const onClick = () => {
        if(publicKey.value === 'admin' && privateKey.value === 'admin') {
            localStorage.setItem('login', 'true')   
            window.location.href = '/'      
        } else {
            alert('로그인 실패')
        }
    }

    return (
        <div className='loginContainer'>
            <LoginInfo />
            <form>
                <input type='password' placeholder='public API key를 입력해주세요.' className='apiInput' {...publicKey}/><br/>
                <input type='password' placeholder='private API key를 입력해주세요.' className='apiInput' {...privateKey}/>
            </form>
            <button type='submit' onClick={ onClick }>Login</button>
            <FindingAPIKey />
        </div>
    )
}

export default LoginPage