import React from "react";
import { Switch, Route } from 'react-router-dom';

import Landing from './landing/landing.jsx';
import '../stylesheets/base/reset.scss';


class App extends React.Component {
  render() {
    return (
      <div>
        <Switch>
          <Route path="/" component={Landing} />
        </Switch>
      </div>
    );
  }
}

// class App extends React.Component {
//   constructor() {
//     super();
//     this.state = {
//     'users': []
//     };
//   }

//   componentDidMount() {
//     this.getItems();
//   }

//   getItems()
//   {
//     fetch("http://127.0.0.1:8000/executivetable_restserver/executivetable/user")
//       .then(results => results.json())
//       .then(results => this.setState({'users' :results}));
//   }

//   render() {
//     return(
//       <ul>
//         {this.state.users.map(function(user, index)
//           {

//             return (
//             <div>
//             <h1>{user.first_name + " " + user.last_name}</h1>
//             <p>{user.email}</p>
//             </div>
//             )

//           }
//           )}
//       </ul>
//       )
//   }
// }


export default App;