import React from 'react'
import { Route } from 'react-router-dom'
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import './App.css'

function App() {
  return (
    <div className="App">
      손절이 나의 멘탈을 지킨다.
      <Route exact path='/' component={LoginPage} />
      <Route path='/home' component={HomePage} />
    </div>
  )
}

export default App
