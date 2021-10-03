import React, { useState, useEffect } from 'react'
import { Route, Switch } from 'react-router-dom'
import { useMediaQuery } from 'react-responsive'
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import NotFound from 'Pages/NotFound'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(false)
  const [logs, setLogs] = useState<any>({})
  const isMobile = useMediaQuery({
    query: '(max-width: 920px)'
  })
  
  useEffect(() => {
    setIsLogin(sessionStorage.getItem('login') === 'true')
  }, [])

  // console.log(logs.log)

  return (
    <div className='App'>
      <GlobalNavigationBar setLogs={ setLogs }/>
      <div className='contents'>
        { !isMobile ?
          <Switch>
            { !isLogin ? 
              <Route path='/' component={ LoginPage } /> : 
              <Route path='/' render={ () => <HomePage value={ logs.log }/> } /> 
            }
            <Route component={ NotFound } />
          </Switch> :
          // TODO 1 :: mobile 페이지 코드 구현
          <div>mobile</div>
        }
      </div>
    </div>
  )
}

export default App
