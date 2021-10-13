import React, { useState, useEffect } from 'react'
import { Route, Switch } from 'react-router-dom'
import { HomePage, LoginPage, NotFound } from 'Pages'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(false)
  const [logs, setLogs] = useState<any>({})
  
  useEffect(() => {
    setIsLogin(sessionStorage.getItem('login') === 'true')
  }, [])

  // console.log(logs.log)

  return (
    <div className='App'>
      <GlobalNavigationBar setLogs={ setLogs }/>
      <div className='contents'>
        <Switch>
          { !isLogin ? 
            <Route path='/' component={ LoginPage } /> : 
            <Route path='/' render={ () => <HomePage value={ logs.log }/> } /> 
          }
          <Route component={ NotFound } />
        </Switch> :
      </div>
    </div>
  )
}

export default App
