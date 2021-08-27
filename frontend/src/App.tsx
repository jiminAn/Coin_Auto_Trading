import React, { useState, useEffect } from 'react'
import { Route } from 'react-router-dom'
import { useMediaQuery } from 'react-responsive'
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(false)
  const isMobile = useMediaQuery({
    query: '(max-width: 920px)'
  })
  
  useEffect(() => {
    setIsLogin(localStorage.getItem('login') === 'true')
  }, [])

  return (
    <div className='App'>
      <GlobalNavigationBar />
      <div className='contents'>
        { !isMobile ?
          <>
            { !isLogin ? 
              <Route path='/' component={LoginPage} /> : 
              <Route path='/' component={HomePage} /> 
            }
          </> :
          <div>mobile</div>
        }
      </div>
    </div>
  )
}

export default App
