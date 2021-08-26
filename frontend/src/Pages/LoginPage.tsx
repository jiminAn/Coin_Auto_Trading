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
    return fetch('http://localhost:5000/login', {
        method: 'POST',
        body: JSON.stringify(userInfo)
    })
    .then(data => data.text()) // 받아온 데이터를 처리하는 구문
    // .then(data => data.json())
}

function LoginPage() {
    const publicKey = useInput('')
    const privateKey = useInput('')

    const onSubmit = async (e: any) => {
        e.preventDefault()
        const response = await login({
            publicKey: publicKey.value,
            privateKey: privateKey.value
        })
        console.log(response)
        // 받아온 response에 대한 처리 후 페이지 이동
        if(publicKey.value === 'admin' && privateKey.value === 'admin') {
            localStorage.setItem('login', 'true')
            window.location.href = '/'
        } else {
            // 모달 창으로 구현할 것인가 ?
            alert('error')
        }
    }

    return (
        <div className='loginContainer'>
            <LoginInfo />
            <form method='POST' onSubmit={ onSubmit }>
                <input type='password' placeholder='public API key를 입력해주세요.' className='apiInput' {...publicKey}/><br/>
                <input type='password' placeholder='private API key를 입력해주세요.' className='apiInput' {...privateKey}/>
                <button type='submit'>Login</button>
            </form>
            <FindingAPIKey />
        </div>
    )
}

export default LoginPage