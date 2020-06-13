
import React from 'react';
import PropTypes from 'prop-types';
import Login from '../Login/Login.js';

class Profile extends React.Component{
    constructor(props) {
        super(props)
        //Obj = new Login();
        this.state = {
            //username: '',
            password: '',
            email: '',
         }
  
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };
//   test= () => {
//     Obj.getUsername();
//   };
  
  render() {
    console.log(localStorage.getItem('currentUser'))
    return (
      <form onSubmit={e => this.props.handle_signup(e, this.state)}>
        
        <h4>Welcome to your dashboard, {localStorage.getItem('currentUser')} </h4>
        <input
          type="text"
          name="username"
          value={this.state.username}
          onChange={this.handle_change}
          placeholder="Your Name"
        />
        <br/>
        <input
          type="text"
          name="email"
          value={this.state.email}
          onChange={this.handle_change}
          placeholder="Your Email"
        />
        <br/>
        <input
          type="password"
          name="password"
          value={this.state.password}
          onChange={this.handle_change}
          placeholder="Your Password"
          autoComplete="on"
        />
        <br/>
        <input type="submit" value="Next" />
      </form>
    );
  }
}

export default Profile;

// SignupForm.propTypes = {
//   handle_signup: PropTypes.func.isRequired
// };