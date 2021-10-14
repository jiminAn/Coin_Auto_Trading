import React, { useState, useEffect } from 'react'
import { Route, Switch } from 'react-router-dom'
import { HomePage, LoginPage, NotFound } from 'Pages'
import GlobalNavigationBar from 'Components/GlobalNavigationBar/GlobalNavigationBar'
import './App.css'

function App() {
  const [isLogin, setIsLogin] = useState<boolean>(false)
  // DEBT :: any 타입이 아닌 유효한 타입 이름 지정
  const [tradingRecords, setTradingRecords] = useState<any>({})

  // DEBT :: 로그인 로직 수정
  useEffect(() => {
    setIsLogin(sessionStorage.getItem('login') === 'true')
  }, [])

  // console.log(tradingRecords.logs)

  return (
    <div className='App'>
      <GlobalNavigationBar setTradingRecords={ setTradingRecords }/>
      <div className='applicationMain'>
        <Switch>
          { !isLogin ? 
            <Route exact path='/' component={ LoginPage } /> : 
            <Route exact path='/' render={ () => <HomePage tradingRecords={ tradingRecords.log }/> } />
          }
          <Route component={ NotFound } />
        </Switch>
      </div>
    </div>
  )
}

export default App
