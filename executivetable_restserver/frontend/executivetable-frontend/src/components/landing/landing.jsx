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
              Pharetra in sit. <br /> In aliquam.
            </h1>
            <h5>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </h5>
            <p>Elit at, imperdiet dui accumsan sit</p>
          </div>
          <form className="landing-header__form-container">
            <div className="landing-header__form-top-border-line"></div>
            <h1>Get more information</h1>
            <div className="landing-header__form-name-container">
              <input type="text" placeholder="First Name" />
              <input type="text" placeholder="Last Name" />
            </div>
            <input type="email" placeholder="Email Address" />
            <button>Send</button>
          </form>
        </div>
        <div className="container">
          <svg preserveAspectRatio="xMinYMin meet" viewBox="0 0 500 500">
            <defs>
              <linearGradient id="Gradient1" x1="0" x2="1" y1="0" y2="1">
                <stop offset="0%" stopColor="#5ae7bd"></stop>
                <stop offset="100%" stopColor="#2cd5ce"></stop>
              </linearGradient>
            </defs>
            <path
              fill="white"
              d="M0 90c150-65 350 60 500-10V0H0z"
            ></path>
          </svg>
        </div>
      </div>
    );
  }
}

export default Landing;

