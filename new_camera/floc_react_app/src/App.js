import './App.css';
import React, { useRef, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import CameraDropdown from './CameraDropdown.jsx';
import HeaderBox from './headerBox.jsx';

const { ipcRenderer } = window.require('electron');
// import { dialog } from '@electron/remote'
function App(props) {
  const webcamRef = useRef(null);
  const [autoCapture, setAutoCapture] = useState(false);
  const [autoCaptureInterval, setAutoCaptureInterval] = useState(null);
  const [fileLocation, setFileLocation] = useState(null);
  const [flashing, setFlashing] = useState(false);
  const [flashingInterval, setFlashingInterval] = useState(null);
  const [countdownSeconds, setCountdownSeconds] = useState(props.countdownSecond || 5);
  const [screenFlash, setScreenFlash] = useState(false);
  const [countdown, setCountdown] = useState(false);
  const [fileError, setFileError] = useState(false);
  const count_array = [null, null, null, null, 3, 3, 2, 2, 1, 1, null];
  let count_idx = 0;

  useEffect(() => {
    // Handle responses from the main process
    ipcRenderer.on('choosePathResult', (event, result) => {
      // Log the selected path in the renderer process
      console.log('Selected Path (renderer process):', result);

      // Update the state with the selected path or perform other actions
      if (result) {
        setFileError(false);
        setFileLocation(result);
      }
    });

    // Cleanup the event listener on component unmount
    return () => {
      ipcRenderer.removeAllListeners('choosePathResult');
    };
  }, []);

  const capture = () => {
    if(fileLocation != null) {
      setFileError(false);
      setScreenFlash(true);
      setTimeout(() => {
        setScreenFlash(false);
      }, 500);
    }
    else {
      setFileError(true);
    }
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
      .then(data => { console.log(data)})
      .catch(error => {console.log(error); setFileError(true)})

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
    if(fileLocation !=null) {
      setFileError(false);
      capture();

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
      }, countdownSeconds * 1000); // Capture an image every 5 seconds

      //set red button to flash
      const flashIntervalId = setInterval(() => {
        if (count_idx === 9) {
          setScreenFlash(true);
        }
        else {
          setScreenFlash(false);
        }
        if (count_idx <= 9) {
          count_idx++;
        }
        else {
          count_idx = 1;
        }
        setCountdown(count_array[count_idx]);
        setFlashing(prevFlashing => !prevFlashing);
      }, 500);
      setFlashingInterval(flashIntervalId);

      // Set auto-capture mode to true
      setAutoCapture(true);
      setAutoCaptureInterval(intervalId);
    }
    else {
      setFileError(true);
    }
  };

  return (
    <div className="container">
      <header className="Floc App">
        <HeaderBox currentTab={1}/>
        <div className="contentContainer">
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
              <p className={flashing ? 'clear' : 'countdown'} >{countdown}</p>
              <button className="pic"
                style={{
                  position: 'absolute',
                  bottom: 10,
                  right: 10,
                  zIndex: 100,
                }}
                onClick={capture}
              >
                <img alt='' src='https://www.pngall.com/wp-content/uploads/13/Red-Button-PNG.png' width={30} height={30} className={flashing ? 'clear' : 'solid'} />
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
          <div className="controlsBox">
            <button className="button" onClick={choosePath}>Set File Location</button>
            {(fileError) && (
                <p className="fileErrMsg">Please select a file location.</p>
            )}
          </div>
        </div>
      </header>
    </div>

  );
}

export default App
