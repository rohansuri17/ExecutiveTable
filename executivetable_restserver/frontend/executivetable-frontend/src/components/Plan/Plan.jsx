import React from 'react';
import '../../stylesheets/components/plan.scss';

class Plan extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div className="plan">
        <h1>Choose Your Plan</h1>
        <div className="plan-holder__container">
          <div><h3>Basic</h3></div>
          <div><h3>Premium</h3></div>
        </div>
      </div>
    )
  }
};

export default Plan;