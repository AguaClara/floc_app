import Dropdown from 'react-bootstrap/Dropdown';
import './App.css';
import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
function App() {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);

  const capture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImgSrc(imageSrc);
    // Here you can save the image to a directory using backend logic
    // For demonstration purpose, you can log the base64 image data
    console.log(imageSrc);
  };
  const fetchData = () => {
    // Use the Fetch API to send a GET request to your Flask backend
    fetch('http://127.0.0.1:5000/test')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data); // Process and display the data as needed
        alert(JSON.stringify(data)); // Displaying the data in an alert for demonstration
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  };
  return (
    <div className="App">
      <p>Hello World</p>
      <header className="Floc App">
        <div className="cameraBox">
          <div style={{ position: 'relative', width: 640, height: 480 }}>
            <Webcam
              audio={false}
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              width={640}
              height={480}
            />
            <button
              style={{
                position: 'absolute',
                bottom: 10,
                right: 10,
                zIndex: 100,
              }}
              onClick={capture}
            >
              Take Picture
            </button>
          </div>
          {imgSrc && (
            <div>
              <h2>Preview:</h2>
              <img src={imgSrc} alt="Captured" />
            </div>
          )}

        </div>
        <div className="exportBox">
          <p>Export Data</p>
          <button className="exportButton" onClick={fetchData}>
            Export
          </button>
          <button className="flocSizeData">
            Get Floc Size Data
          </button>
        </div>
        <div className="cameraControlsBox">
          <button className="Start Button">Start</button>
          <button className="End Button">End</button>
          <button className="Change Save Location">Change Save Location</button>
          <Dropdown className="Select Camera">
            <Dropdown.Toggle variant="success" id="dropdown_basic">
              Select
            </Dropdown.Toggle>
            <Dropdown.Menu>
              <Dropdown.Item href="#/action-1">Camera1</Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </div>
      </header>
    </div>
  );
}

export default App
