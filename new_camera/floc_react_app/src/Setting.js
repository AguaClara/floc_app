import React, { useState } from 'react';
import HeaderBox from './headerBox.jsx';
import './App.css';

function ConfirmationPopup({ onConfirm }) {
  return (
    <div className="popup">
      <>Are you sure you want to clear the database? </>
      <button onClick={onConfirm}>Yes</button>
      <button onClick={() => {}}>Cancel</button>
    </div>
  );
}

const Setting = (props) => {
  const [inputValue, setInputValue] = useState(props.countdownSecond);
  const [storageCapacity, setStorageCapacity] = useState(5000);
  const [showPopup, setShowPopup] = useState(false);

  // Event handler to handle input changes
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
    props.setCountdownSeconds(event.target.value);
  };

  const handleClearDatabase = () => {
    setShowPopup(true);
  };

  const handleCancelClearDatabase = () => {
    setShowPopup(false);
  };
/*
  const handleStorageInputChange = (event) => {
    setStorageCapacity(event.target.value);
  }
  const updateCountdownSeconds = () => {
    props.setCountdownSeconds(inputValue);
  };
*/
  const handleConfirmClearDatabase = () => {
    fetch('http://127.0.0.1:5000/images/', {
      method: 'DELETE'
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Image deletion failed');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
        alert(JSON.stringify(data));
      })
    setShowPopup(false);
  };

  return (
    <div >
      <HeaderBox currentTab={2}/>
      <div className="settingsContainer">
        <div className="settingsHeader">
          <h1 className="settingsLabel">Settings</h1>
          <img className="settingsIcon" src="https://static-00.iconduck.com/assets.00/settings-icon-1964x2048-8nigtrtt.png" alt="" width="40px" height="40px "></img>
        </div>
        <div className = "settingsComponentBoxWrapper">
          <div className = "settingsComponentBox">
            <>Autocapture Interval: </>
            <input
              type="text"
              className='inputBox'
              value={inputValue}
              defaultValue='5'
              onChange={handleInputChange}
            />
            <> seconds</>
            <p></p>
            <>Database Storage Capacity: </><input
              type="text"
              className='inputBox'
              value={storageCapacity} // Input value is controlled by state
              onChange={handleInputChange} // Event handler for input changes
            />
            <> images</>
            <p></p>
            <button className="deleteButton" onClick={handleClearDatabase}>Clear Database Images</button>
            {showPopup && (
              <ConfirmationPopup
                onConfirm={handleConfirmClearDatabase}
                onCancel={handleCancelClearDatabase}
              />
            )}
          </div>
        </div>
        <div className="infoHeader">
            <h1 className="settingsLabel">Info</h1>
            <img className="infoIcon" src="https://static-00.iconduck.com/assets.00/wrench-icon-2047x2048-jyerjpd9.png" alt="" width="40px" height="40px "></img>
          </div>
        <div className="infoBoxWrapper">
          <div className="infoBox">
            <button className="infoButton">App Instructions and Documentation</button>
            <p></p>
            <button className="infoButton">More about AguaClara Cornell</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Setting;