import React from 'react';
import HeaderBox from './headerBox.jsx';
import './App.css';
import { useState, useEffect } from 'react';

const Setting = (props) => {
  const [inputValue, setInputValue] = useState(props.countdownSecond);
  const [storageCapacity, setStorageCapacity] = useState(5000);
  const [showPopup, setShowPopup] = useState(false);
  const [showAcInfo, setShowAcInfo] = useState(false);
  const [showAppInfo, setShowAppInfo] = useState(false);
  const [fileContent, setFileContent] = useState('');

  // Event handler to handle input changes
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
    props.setCountdownSeconds(event.target.value);
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('app_instructions.txt', {
          headers: {
            'Content-Type': 'text/plain'
          }
        });
        if (!response.ok) {
          throw new Error('Failed to fetch file');
        }
        // Assuming the file is in plaintext format
        const text = await response.text();
        setFileContent(text);
      } catch (error) {
        alert(error)
        console.error('Error fetching file:', error);
      }
    };
    fetchData();
  }, []);

  const handleClearDatabase = () => {
    setShowPopup(true);
  };

  const handleCancelClearDatabase = () => {
    setShowPopup(false);
  };

  const handleStorageInputChange = (event) => {
    setStorageCapacity(event.target.value);
  }
  const updateCountdownSeconds = () => {
    props.setCountdownSeconds(inputValue);
  };

  const handleAcInfoClick = () => {
    setShowAcInfo(true);
  }

  const handleCloseClick = () => {
    setShowAcInfo(false);
    setShowAppInfo(false);
  }

  const handleAppInfoClick = () => {
    setShowAppInfo(true);
  }

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
          </div>
        </div>
        <div className="infoHeader">
            <h1 className="settingsLabel">Info</h1>
            <img className="infoIcon" src="https://static-00.iconduck.com/assets.00/wrench-icon-2047x2048-jyerjpd9.png" alt="" width="40px" height="40px "></img>
          </div>
        <div className="infoBoxWrapper">
          <div className="infoBox">
            <button className="infoButton" onClick={handleAppInfoClick}>App Instructions and Documentation</button>
            <p></p>
            <button className="infoButton" onClick={handleAcInfoClick}>More about AguaClara Cornell</button>
          </div>
        </div>
      </div>
      {showPopup && (
        <div>
          <div className="popupWrapper"></div>
          <div className="popup">
              <p className="popupMsg">Are you sure you want to clear the database? </p>
              <button className="popupButton" onClick={handleConfirmClearDatabase}>Yes</button>
              <button className="popupButton" onClick={handleCancelClearDatabase}>Cancel</button>
          </div> 
        </div>)}
      {showAcInfo && (
        <div>
          <div className = "popupWrapper"></div>
          <div className = "acInfoBox">
          <img className = "logo_img" src="https://aguaclara.cornell.edu/assets/AguaClara_Logo-beebcdc8.png" alt="" width={440} height={90} />
            <p className="acMsg">Founded in 2005, AguaClara Cornell pioneers research in community-scale water treatment technologies. AguaClara Cornell has partnered with AguaClara Reach and other local organizations to build fourteen AguaClara plants that provide safe water on tap to over 65,000 people, with the flagship plant in Ojojona, Honduras and other plants in India. The research, invention, and design project courses specific to AguaClara are focused on developing technology that can be used to improve the drinking water quality of surface water sources in the Global South. The program is structured to allow students with different levels of expertise to collaborate, invent, and change the world. Our designs are meticulously created to use locally-sourced materials, ensuring they are environmentally friendly and easy to maintain for the communities we serve. This approach combines simplicity, ecological responsibility, and community empowerment into one cohesive vision.</p>
          <button className="closeButton" onClick={handleCloseClick}>X</button>
          </div>
        </div>
      )}
      {showAppInfo && (
        <div>
        <div className = "popupWrapper"></div>
        <div className = "acInfoBox">
        <p className="acMsg">[App instructions and documentation]</p>
        <button className="closeButton" onClick={handleCloseClick}>X</button>
        </div>
      </div>
      )}
    </div>
  );
}

export default Setting;