import React from "react";
import '../../stylesheets/components/landing.scss';

class Landing extends React.Component {
  render() {
    return (
      <div className="landing-outer__container">
        <h1>The Executive Table</h1>
        <div className="landing-header__text-form__container">
          <div className="landing-header__text-container">
            <h1>
              Pharetra sit. <br /> In aliquam.
            </h1>
            <h5>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </h5>
            <p>Elit at, imperdiet dui accumsan sit</p>
          </div>
          <form className="landing-header__form-container">
            <h1>Get More Information</h1>
            <div className="landing-header__form-name-container">
              <input type="text" placeholder="First Name" />
              <input type="text" placeholder="Last Name" />
            </div>
            <input type="email" placeholder="Email Address" />
            <button value="Send" />
          </form>
        </div>
      </div>
    );
  }
}

export default Landing;

