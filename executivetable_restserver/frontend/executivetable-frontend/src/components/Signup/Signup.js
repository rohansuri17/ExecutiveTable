import React, { Component } from 'react';
import Nav from '../Nav';
import SignupForm from '../SignupForm';
import LoginForm from '../LoginForm';
import '../../stylesheets/components/signup.scss';

class Signup extends Component {
  constructor(props) {
    super(props);
    this.state = {
      displayed_form: '',
      logged_in: localStorage.getItem('token') ? true : false,
      username: 'Logging in'
    };
    this.handle_signup = this.handle_signup.bind(this)
  }

  async componentDidUpdate(prevProps,prevState) {
      if (this.state.logged_in) {
        if (this.state.username !== prevState.username) {
          //this.fetchData(this.state.username);
        const response = await fetch('http://127.0.0.1:8000/executivetable_restserver/user', {
          headers: {
            Authorization: `Token ${localStorage.getItem('token')}`
          }
        })
        const res = await response.json()
          //.then(res => res.json())
          //.then(res => {
          this.setState({ username: res.username});
          //});
          //debugger
        }
      }

  }

  /*handle_login = (e, data) => {
    //this.state.username = "Logging in"
    e.preventDefault();
    fetch('http://127.0.0.1:8000/executivetable_restserver/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(res => {
        localStorage.setItem('token', res.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: res.username
        });
      });
  };
  */

  handle_signup = (e, data) => {
    //this.state.username = "Logging in"
    e.preventDefault();
    fetch('http://127.0.0.1:8000/executivetable_restserver/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(res => {
        localStorage.setItem('token', res.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: res.username
        });
      });
  };

  handle_logout = () => {
    localStorage.removeItem('token');
    this.setState({ logged_in: false, username: '' });
  };

  display_form = form => {
    this.setState({
      displayed_form: form
    });
  };

  render() {
    let form;
    form = <SignupForm handle_signup={this.handle_signup} history={this.props.history} />;
    
    return (
      <div className="Signup">
        <img src="https://images.unsplash.com/photo-1527259216948-b0c66d6fc31f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"></img>
        {form}
      </div>
    );
  }
}

export default Signup;
