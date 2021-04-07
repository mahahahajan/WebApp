
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Navbar, Nav, NavDropdown } from 'react-bootstrap';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import HomePage from "./components/HomePage"
import LoginPage from "./components/LoginPage"
import RegisterPage from "./components/RegisterPage"

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(() => {
    axios.get('http://localhost:5000/').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App">
      <Router>
        <Switch>

          <Route path="/login">
            <LoginPage></LoginPage>
          </Route>

          <Route path="/register">
            <RegisterPage></RegisterPage>
          </Route>

          <Route path="/account">
            {/* <Projects /> */}
          </Route>
          <Route path="/createProject">
            {/* <Projects /> */}
          </Route>
          <Route path="/project">
            {/* <Projects /> */}
          </Route>
          <Route path="/editProject">
            {/* <Projects /> */}
          </Route>
          <Route path="/hardware">
            {/* <Projects /> */}
          </Route>
          <Route path="/datasets">
            {/* <Projects /> */}
          </Route>

          <Route path="/">
            <HomePage></HomePage>
            {/* <div>{getMessage.status === 200 ?
              <h3>{getMessage.data.username}</h3>
              :
              <h3>Not found</h3>}
            </div> */}
          </Route>
        </Switch>

      </Router>

    </div>
  );
}

export default App;