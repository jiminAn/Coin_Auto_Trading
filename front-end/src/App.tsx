import React, { useState } from 'react'
import { Route } from 'react-router-dom'
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(false) // localStorage 또는 sessionStorage 사용

  return (
    <div className='App'>
      <GlobalNavigationBar isLogin={ isLogin }/>
      <div className='contents'>
        {/* isLogin 값을 props로 넘겨서 해당 route에서 isLogin 여부에 따라 렌더링을 변경 */}
        <Route exact path='/' component={LoginPage} />
        <Route path='/home' component={HomePage} />
      </div>
    </div>
  )
}

export default App
