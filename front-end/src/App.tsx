import React, { useState, useEffect } from 'react'
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

// NOTICE :: 백엔드 구현 전까지 백엔드와 통신이 필요한 부분은 localStorage로 대체

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(true)

  // localStorage에 저장된 로그인 상태를 조회
  useEffect(() => {
    localStorage.setItem('login', String(isLogin))
  })

  return (
    <div className='App'>
      <GlobalNavigationBar />
      <div className='contents'>
        { !isLogin ? <LoginPage /> : <HomePage /> }
      </div>
    </div>
  )
}

export default App
