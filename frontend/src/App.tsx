import React, { useState, useEffect } from 'react'
import { Route } from 'react-router-dom' 
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

// NOTICE :: 백엔드 구현 전까지 백엔드와 통신이 필요한 부분은 localStorage로 대체

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(false)

  useEffect(() => {
    setIsLogin(localStorage.getItem('login') === 'true')
  }, [])

  return (
    <div className='App'>
      <GlobalNavigationBar />
      <div className='contents'>
        { !isLogin ? 
          <Route path='/' component={LoginPage} /> : 
          <Route path='/' component={HomePage} /> 
        }
      </div>
    </div>
  )
}

export default App
