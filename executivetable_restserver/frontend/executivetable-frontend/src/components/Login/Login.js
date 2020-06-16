import React from 'react';
import LoginForm from '../LoginForm';
import Profile from '../Profile/Profile';
// import { Button, Navbar, NavDropdown, Form, FormControl} from 'react-bootstrap';
import '../../stylesheets/components/login.scss';
import { Redirect } from 'react-router-dom';
export const isLogin = () => {
  if(localStorage.getItem('token'))
  {
    return true;
  }
}

class Login extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        displayed_form: '',
        logged_in: localStorage.getItem('token') ? true : false,
        username: localStorage.getItem('currentUser') ? localStorage.getItem('currentUser') : '',
      };
      this.handle_login = this.handle_login.bind(this)
      this.getUsername = this.getUsername.bind(this)
    }
  
    handle_login = (e, data) => {
      e.preventDefault();
      fetch('/executivetable_restserver/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      })
        .then(res => res.json())
        .then(res => {
          localStorage.setItem('token', res.token);
          localStorage.setItem('currentUser', res.user.username);
          this.setState({
            logged_in: true,
            displayed_form: '',
            username: res.user.username
          });
        });
    };
    
    handle_logout = () => {
      localStorage.removeItem('token');
      this.setState({ logged_in: false, username: '' });
    };
    getUsername = () => {
      if(this.state.username!==undefined){
        return this.state.username
      }
    }
  
    display_form = form => {
      this.setState({
        displayed_form: form
      });
    };

    render() {
        let form;
        form = <LoginForm handle_login={this.handle_login} />;
        
        return (
          
          <div className="Login">
            <img src="https://images.unsplash.com/photo-1527259216948-b0c66d6fc31f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80" alt="conference-room"></img>
            <div className="Login-form__text-wrapper">
              {form}
              <h3>
                {this.state.logged_in
                  ? <Redirect to = '/Profile' exact />
                  : 'Please Log In'}
              </h3>
              {/* console.log(this.state.username); */}
              {/* <Profile username={this.state.logged_in ? this.state.username:'NULL USER'} /> */}
              
            </div>
          </div>
        );
    }
} 
export default Login;