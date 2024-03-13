import './App.css';
import React, { useRef, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import CameraDropdown from './CameraDropdown.jsx';
import {Link} from 'react-router-dom';

const { ipcRenderer, ipcMain } = window.require('electron');
// import { dialog } from '@electron/remote'
function App() {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);
  const [autoCapture, setAutoCapture] = useState(false);
  const [autoCaptureInterval, setAutoCaptureInterval] = useState(null);
  const [fileLocation, setFileLocation] = useState(null);
  const [flashing, setFlashing] = useState(false);
  const [flashingInterval, setFlashingInterval] = useState(null);
  const [countdownSeconds, setCountdownSeconds] = useState(5);

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
      body: JSON.stringify({ image: imageSrc, filePath: fileLocation })
    })
      .then(response => response.json())
      .then(data => { console.log(data); alert(JSON.stringify(data)) })
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
      return;
    }

    capture();

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
        body: JSON.stringify({ image: imageSrc, filePath: fileLocation })
      })
        .then(response => response.json())
        .then(data => { console.log(data); alert(JSON.stringify(data)) })
        .catch(error => console.log(error));
    }, countdownSeconds * 1000); // Capture an image every 5 seconds

     //set red button to flas
    const flashIntervalId = setInterval(() => {
      setFlashing(prevFlashing => !prevFlashing);
    }, 500);
    setFlashingInterval(flashIntervalId);

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
          <img src="https://res.cloudinary.com/scalefunder/image/fetch/s--7ZiRgq59--/f_auto,fl_lossy,q_auto/https://github.com/AguaClara/public_relations/blob/master/AguaClara%2520Official%2520Logo/FINAL%2520LOGO%25202.0.png%3Fraw%3Dtrue" alt="" width={290} height={95} />
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
                right: 0,
                zindex: 15
              }}>
              <CameraDropdown className="camera_dropdown" />
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
            <img alt='' src='https://www.pngall.com/wp-content/uploads/13/Red-Button-PNG.png' width={30} height={30} className={flashing ? 'clear': 'solid'}/>
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
        <div className="exportBox">
          <p>Export Data</p>
          <button className="button" onClick={fetchData}>
            Export
          </button>
          <button className="button" onClick={choosePath}>Set File Location</button>
          <button className="button">
            Get Floc Size Data
          </button>
          <div style={{ textAlign: 'center', margin: 25}}>
            <Link to="/new" className="button" style={{ textDecoration: 'none' }} >Go to New Page</Link>
          </div>
        </div>
        
        <div>
          <button className="deleteButton" onClick={deleteImages}>
            <img src="https://cdn-icons-png.flaticon.com/512/3515/3515498.png" alt="Delete All Images" width={30} height={30} />
          </button>
        </div>

      </header>
    </div>
  );
}

export default App
