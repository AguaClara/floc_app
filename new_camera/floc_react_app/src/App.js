import './App.css';
import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
import CameraDropdown from './CameraDropdown.jsx';
function App() {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);
  const [autoCapture, setAutoCapture] = useState(false);
  const [autoCaptureInterval, setAutoCaptureInterval] = useState(null);

  const capture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImgSrc(imageSrc);
    // Here you can save the image to a directory using backend logic
    // For demonstration purpose, you can log the base64 image data
    console.log(imageSrc);

    fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageSrc })
    })
      .then(response => response.json())
      .then(data => { console.log(data); alert(JSON.stringify(data)) })
      .catch(error => console.log(error)
      )


  };

  // Auto-capture mode
  const toggleAutoCapture = () => {
    // Stop auto-capture mode if it's currently active
    if (autoCapture) {
      clearInterval(autoCaptureInterval);
      setAutoCapture(false);
      return;
    }

    // Start auto-capture mode
    const intervalId = setInterval(() => {
      const imageSrc = webcamRef.current.getScreenshot();
      setImgSrc(imageSrc);

      // Send the captured image to the backend
      fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageSrc })
      })
        .then(response => response.json())
        .then(data => { console.log(data); alert(JSON.stringify(data)) })
        .catch(error => console.log(error));
    }, 5000); // Capture an image every 5 seconds

    // Set auto-capture mode to true
    setAutoCapture(true);
    setAutoCaptureInterval(intervalId);
  };

  const fetchData = () => {
    // Use the Fetch API to send a GET request to Flask backend
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
    <div className="container">
      <header className="Floc App">
        <div>
          <img src="https://res.cloudinary.com/scalefunder/image/fetch/s--7ZiRgq59--/f_auto,fl_lossy,q_auto/https://github.com/AguaClara/public_relations/blob/master/AguaClara%2520Official%2520Logo/FINAL%2520LOGO%25202.0.png%3Fraw%3Dtrue" alt = "" width={290} height={95}/>
        </div>
        <div className="cameraBox">
          <div style={{ position: 'relative', width: 640, height: 480 }}>
          <Webcam className='video'
              audio={false}
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              width={640}
              height={480}
            />
            <div 
            style={{ 
              position: 'relative', 
              bottom: 43,
              right: -170,
              zindex: 15 }}>
                <CameraDropdown/>
            </div>
            <button className="pic"
              style={{
                position: 'absolute',
                bottom: 10,
                right: 10,
                zIndex: 100,
              }}
              onClick={capture}
            >
              <img alt='' src='https://www.pngall.com/wp-content/uploads/13/Red-Button-PNG.png' width={30} height={30} />
            </button>
            
            <button className="autoCaptureButton"
              style={{
                position: 'absolute',
                bottom: 10,
                left: 10,
                zIndex: 100,
              }}
            onClick={toggleAutoCapture}>
              <img alt='' src = 'https://cdn3.iconfinder.com/data/icons/photography-vol-1-1/66/photography-05-1024.png' width={30} height={30} />
              {autoCapture ? 'Stop Auto-Capture' : 'Start Auto-Capture'}
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
          <button className="button" onClick={fetchData}>
            Export
          </button>
          <button className="button">Change Save Location</button>
          <button className="button">
            Get Floc Size Data
          </button>
        </div>
      </header>
    </div>
  );
}

export default App
