import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Setting = (props) => {
  const [inputValue, setInputValue] = useState(props.countdownSecond);

  // Event handler to handle input changes
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };
  const updateCountdownSeconds = () => {
    props.setCountdownSeconds(inputValue);
  };
  return (
    <div>
      <h1>Settings</h1>
      <p>This is the content of the settings page</p>
      <input
        type="text"
        value={inputValue} // Input value is controlled by state
        onChange={handleInputChange} // Event handler for input changes
      />
      <p>Autocapture Interval: {inputValue}</p>
      <div style={{ textAlign: 'center' }}>
        <Link to={{ pathname: "/", state: { countdownSeconds: inputValue } }} className="button" style={{ textDecoration: 'none' }} onClick={updateCountdownSeconds}>Go to App</Link>
      </div>
    </div>
  );
}

export default Setting;
