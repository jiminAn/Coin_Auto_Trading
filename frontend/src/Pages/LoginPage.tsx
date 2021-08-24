/* eslint-disable @typescript-eslint/no-unused-vars */
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

async function login(userInfo: any) {
    return fetch('http://localhost:5000/', {
        method: 'POST',
        body: JSON.stringify(userInfo)
    })
    .then(data => data.json())
}

function LoginPage() {
    const publicKey = useInput('')
    const privateKey = useInput('')

    // const onClick = () => {
    //     if(publicKey.value === 'admin' && privateKey.value === 'admin') {
    //         localStorage.setItem('login', 'true')   
    //         window.location.href = '/'     
    //     } else {
    //         alert('로그인 실패')
    //     }
    // }

    const onSubmit = async (e: any) => {
        e.preventDefault()
        const response = await login({
            publicKey: publicKey.value,
            privateKey: privateKey.value
        })
        if(publicKey.value === 'admin' && privateKey.value === 'admin') {
            localStorage.setItem('login', 'true')
            window.location.href = '/'
        } else {
            alert('error')
        }
    }

    return (
        <div className='loginContainer'>
            <LoginInfo />
            <form>
                <input type='password' placeholder='public API key를 입력해주세요.' className='apiInput' {...publicKey}/><br/>
                <input type='password' placeholder='private API key를 입력해주세요.' className='apiInput' {...privateKey}/>
            </form>
            <button type='submit' onClick={ onSubmit }>Login</button>
            <FindingAPIKey />
        </div>
    )
}

export default LoginPage