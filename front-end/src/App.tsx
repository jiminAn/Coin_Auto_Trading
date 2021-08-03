import React from 'react'
import { Route } from 'react-router-dom'
import HomePage from 'Pages/HomePage'
import LoginPage from 'Pages/LoginPage'
import GlobalNavigationBar from 'Components/GlobalNavigationBar'
import './App.css'

function App() {
  return (
    <div className="App">
      <GlobalNavigationBar />
      <Route exact path='/' component={LoginPage} />
      <Route path='/home' component={HomePage} />
    </div>
  )
}

export default App
