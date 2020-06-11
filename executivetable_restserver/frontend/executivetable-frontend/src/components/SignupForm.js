import React from 'react';
import PropTypes from 'prop-types';

class SignupForm extends React.Component {
  state = {
    username: '',
    password: ''
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

  render() {
    return (
      <form onSubmit={e => this.props.handle_signup(e, this.state)}>
        <h4>Sign Up Now</h4>
        <input
          type="text"
          name="username"
          value={this.state.username}
          onChange={this.handle_change}
          placeholder="Your Name"
        />
        <input
          type="text"
          name="email"
          value={this.state.email}
          onChange={this.handle_change}
          placeholder="Your Email"
        />
        <input
          type="password"
          name="password"
          value={this.state.password}
          onChange={this.handle_change}
          placeholder="Your Password"
        />
        <input type="submit" value="Next" onClick={(event) => {event.preventDefault(); return this.props.history.push("/Plan")}}/>
      </form>
    );
  }
}

export default SignupForm;

SignupForm.propTypes = {
  handle_signup: PropTypes.func.isRequired
};