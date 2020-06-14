import React, { Component } from 'react';
import { NavLink, Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../stylesheets/components/navigation.scss';

import logo from "../images/the-executive-table-logo.png";

export class Navigation extends Component{
    render()
    {
        return(
            <Navbar dark="true" className="bg-dark">
            <Navbar.Toggle aria-controls = "basic-navbar-nav"/>
            <Navbar.Collapse id = "basic-navbar-nav">
            <div className="navigation-logo__container">
                <img height="40" src={logo} alt="logo"></img>
                <h1>The Executive Table</h1>
            </div>
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
            <div className="navigation-login-signup__container">
                <Link to="/Signup">Sign Up</Link>
                <Link to="/Login">Sign In</Link>
            </div>
            </Navbar.Collapse>
                
            </Navbar>
        )
    }
}

export default Navigation;