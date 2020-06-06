import React, {Component} from 'react';
import {NavLink, BrowserRouter} from 'react-router-dom';
import {Navbar, Nav} from 'react-bootstrap';
import Landing from './landing/landing.jsx';
import 'bootstrap/dist/css/bootstrap.min.css';
export class Navigation extends Component{
    render()
    {
        return(
            <Navbar dark="true" className="bg-dark">
            <Navbar.Toggle aria-controls = "basic-navbar-nav"/>
            <Navbar.Collapse id = "basic-navbar-nav">
            <Nav>
                 <NavLink className="d-inline p-2 bg-dark text-white"
                to= '/' >
                Home
                </NavLink>
                <NavLink className="d-inline p-2 bg-dark text-white"
                to= './Signup' >
                Sign up
                </NavLink>
                <NavLink className="d-inline p-2 bg-dark text-white"
                to= './Login' >
                Login
                </NavLink>
            </Nav>
            </Navbar.Collapse>
                
            </Navbar>
        )
    }
}

export default Navigation;