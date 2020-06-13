import React, { Component } from 'react';
import SignupForm from '../SignupForm';
import '../../stylesheets/components/signup.scss';


// export const handle_logout = () => {
   
//     //this.setState({ logged_in: false, username: '' });
//   };
  
class Logout extends Component {

render() {
    localStorage.removeItem('token');
    return(<h1>TEST</h1>);

}
}
  
export default Logout