import './App.css';
import React, { useRef, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import CameraDropdown from './CameraDropdown.jsx';
import HeaderBox from './headerBox.jsx';

const { ipcRenderer } = window.require('electron');
// import { dialog } from '@electron/remote'
function App() {
  const webcamRef = useRef(null);
  const [autoCapture, setAutoCapture] = useState(false);
  const [autoCaptureInterval, setAutoCaptureInterval] = useState(null);
  const [fileLocation, setFileLocation] = useState(null);
  const [flashing, setFlashing] = useState(false);
  const [flashingInterval, setFlashingInterval] = useState(null);
  const [screenFlash, setScreenFlash] = useState(false);
  const [countdown, setCountdown] = useState(false);
  const count_array = [5,5,4,4,3,3,2,2,1,1,null];
  let count_idx = 0;

  useEffect(() => {
    // Handle responses from the main process
    ipcRenderer.on('choosePathResult', (event, result) => {
      // Log the selected path in the renderer process
      console.log('Selected Path (renderer process):', result);

      // Update the state with the selected path or perform other actions
      if (result) {
        setFileLocation(result);
      }
    });

    // Cleanup the event listener on component unmount
    return () => {
      ipcRenderer.removeAllListeners('choosePathResult');
    };
  }, []);

  const capture = () => {
    setScreenFlash(true);
    setTimeout(() => {
      setScreenFlash(false);
    }, 500);
    const imageSrc = webcamRef.current.getScreenshot();
    // Here you can save the image to a directory using backend logic
    // For demonstration purpose, you can log the base64 image data
    console.log(imageSrc);

    fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageSrc, filePath: fileLocation })
    })
      .then(response => response.json())
      //.then(data => { console.log(data); alert(JSON.stringify(data)) })
      .catch(error => console.log(error)
      )
    
  };

  const choosePath = () => {
    // Send a request to the main process to show directory selection dialog
    ipcRenderer.send('choosePath');
    console.log('choosePath called');
  };

  const deleteImages = () => {
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
  };

  // Auto-capture mode
  const toggleAutoCapture = () => {
    // Stop auto-capture mode if it's currently active
    if (autoCapture) {
      clearInterval(autoCaptureInterval);
      clearInterval(flashingInterval);
      setFlashing(false);
      setAutoCapture(false);
      count_idx = 0;
      setCountdown(null);
      return;
    }
    setCountdown(count_array[count_idx]);
    // Start auto-capture mode
    const intervalId = setInterval(() => {
      const imageSrc = webcamRef.current.getScreenshot();

      // Send the captured image to the backend
      fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageSrc, filePath: fileLocation })
      })
        .then(response => response.json())
        //.then(data => { console.log(data); alert(JSON.stringify(data)) })
        .catch(error => console.log(error));
    }, 5000); // Capture an image every 5 seconds

     //set red button to flash
    const flashIntervalId = setInterval(() => {
      if(count_idx<=9) {
        //setScreenFlash(false);
        count_idx++;
      }
      else {
        //setScreenFlash(true);
        count_idx = 1;
      }
      setCountdown(count_array[count_idx]);
      setFlashing(prevFlashing => !prevFlashing);
    }, 500);
    setFlashingInterval(flashIntervalId);

    // Set auto-capture mode to true
    setAutoCapture(true);
    setAutoCaptureInterval(intervalId);
  };

  return (
    <div className="container">
      <header className="Floc App">
        <HeaderBox/>
        <div className = "contentContainer">
          <div className="cameraBox">
            <div style={{ position: 'relative', width: 640, height: 480 }}>
              <Webcam className='video'
                audio={false}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={640}
                height={480}
              />
              {screenFlash && <div className="flash-overlay" />}
              <div
                style={{
                  position: 'relative',
                  width: '15%',
                  margin: '0 auto',
                  bottom: '9%',
                  zindex: 15
                }}>
                <CameraDropdown />
                <headerBox />
              </div>
              <p className={flashing ? 'clear': 'countdown'} >{countdown}</p>
              <button className="pic"
                style={{
                  position: 'absolute',
                  bottom: 10,
                  right: 10,
                  zIndex: 100,
                }}
                onClick={capture}
              >
              <img alt='' src='https://www.pngall.com/wp-content/uploads/13/Red-Button-PNG.png' width={30} height={30} className='solid'/>
              </button>

              <button className="autoCaptureButton"
                style={{
                  position: 'absolute',
                  bottom: 10,
                  left: 10,
                  zIndex: 100,
                }}
                onClick={toggleAutoCapture}>
                <img alt='' src='https://cdn3.iconfinder.com/data/icons/photography-vol-1-1/66/photography-05-1024.png' width={30} height={30} />
                {autoCapture ? 'Stop Auto-Capture' : 'Start Auto-Capture'}
              </button>
            </div>
          </div>
          <div className = "controlsBox">
          <button className="button" onClick={choosePath}>Set File Location</button>
            <button className="deleteButton" onClick={deleteImages}>
              <img src="https://cdn-icons-png.flaticon.com/512/3515/3515498.png" alt="Delete All Images" width={30} height={30} />
            </button>
          </div>
        </div>

      </header>
    </div>
  );
}

export default App
