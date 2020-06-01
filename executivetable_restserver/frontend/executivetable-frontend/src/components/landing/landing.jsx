import React from "react";
import '../../stylesheets/components/landing.scss';

class Landing extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: "",
      lastName: "",
      email: "",
    };
  }

  handleSubmit(e) {
    e.preventDefault();
    // const user = Object.assign({}, this.state);
  }

  update(field) {
    return (e) =>
      this.setState({
        [field]: e.currentTarget.value,
      });
  }

  render() {
    return (
      <div className="landing-outer__container">
        <div className="landing-header__outer-container">
          <div className="landing-header__title-container">
            <img
              height="55"
              src={process.env.PUBLIC_URL + "/the-executive-table-logo.png"}
              alt="logo"
            />
            <h1>The Executive Table</h1>
          </div>
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
                <input
                  type="text"
                  value={this.state.firstName}
                  onChange={this.update("firstName")}
                  placeholder={"First Name"}
                />
                <input
                  type="text"
                  value={this.state.lastName}
                  onChange={this.update("lastName")}
                  placeholder={"Last Name"}
                />
              </div>
              <input
                type="email"
                value={this.state.email}
                onChange={this.update("email")}
                placeholder={"Email Address"}
              />
              <button type="submit">Send</button>
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
              <path fill="white" d="M0 90c150-65 350 60 500-10V0H0z"></path>
            </svg>
          </div>
        </div>
        <div className="landing-info__container">
          <div className="landing-info__text-container">
            <h2>Velit Sed Ullamcorper morbi Tincidunt ornare Massa</h2>
            <p>
              Vulputate mi sit, amet mauris commodo quis imperdiet massa
              tincidunt nunc pulvinar sapien et ligula ullamcorper.
            </p>
          </div>

          <div className="landing-info__outer-box-container">
            <div className="landing-info__box-container">
              <img
                src="https://img.icons8.com/fluent/48/000000/link.png"
                alt="linked-chain"
              />
              <h5>Sit amet porttitor consectetur</h5>
              <p>
                Gravida in fermentum et sollicitudin ac orci phasellus egestas
                tellus, rutrum, tellus pellentesque.
              </p>
            </div>
            <div className="landing-info__box-container">
              <img
                src="https://img.icons8.com/cute-clipart/64/000000/globe.png"
                alt="globe"
              />
              <h5>Proin libero</h5>
              <p>
                At urna condimentum mattis pellentesque id nibh, tortor id
                aliquet, proin nibh nisl, condimentum id scelerisque.
              </p>
            </div>
            <div className="landing-info__box-container">
              <img
                src="https://img.icons8.com/cotton/64/000000/business-group.png"
                alt="group-of-people"
              />
              <h5>Scelerisque integer nunc</h5>
              <p>
                Blandit aliquam etiam erat velit scelerisque in dictum non
                consectetur a erat lectus condimentum pellentesque.
              </p>
            </div>
          </div>
          <button>Contact Us Now</button>
        </div>
      </div>
    );
  }
}

export default Landing;

