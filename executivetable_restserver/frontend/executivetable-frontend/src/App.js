/*import React, { Component } from 'react';

class App extends Component {
  state = {
    'user': []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/executivetable_restserver/executivetable/user');
      const users = await res.json();
      console.log(users)
      this.setState({
        'user': users
      }); 
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return(
      <ul>
        {this.state.user.map(function(use, index)
          {
            return <h1>{use.title}</h1>

          }
          )}
      </ul>
      )
  }
}

export default App;
*/
import React from "react";

import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
    'users': []
    };
  }

  componentDidMount() {
    this.getItems();
  }

  getItems()
  {
    fetch("http://127.0.0.1:8000/executivetable_restserver/executivetable/user")
      .then(results => results.json())
      .then(results => this.setState({'users' :results}));
  }

  render() {
    return(
      <ul>
        {this.state.users.map(function(user, index)
          {

            return (
            <div>
            <h1>{user.first_name + " " + user.last_name}</h1>
            <p>{user.email}</p>
            </div>
            )

          }
          )}
      </ul>
      )
  }
}


export default App;