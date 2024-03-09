import './App.css';
import React, { useRef, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import CameraDropdown from './CameraDropdown.jsx';
const { ipcRenderer, ipcMain } = window.require('electron');
// import { dialog } from '@electron/remote'
function App() {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);
  const [autoCapture, setAutoCapture] = useState(false);
  const [autoCaptureInterval, setAutoCaptureInterval] = useState(null);
  const [fileLocation, setFileLocation] = useState(null);

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

  // const choosePath = async () => {
  //   // const filePaths = await window.showDirectoryPicker();

  //   const { filePaths } = await dialog.showOpenDialog({
  //     title: 'Save to Folder',
  //     properties: ['openDirectory'],
  //   });

  //   // save file path as string in filelocation state
  //   setFileLocation(filePaths[0]);
  //   alert(filePaths)
  //   return filePaths;
  // }

  // const choosePath = () => {
  //   const { dialog } = require('electron');

  //   // Options for the directory picker dialog
  //   const options = {
  //     title: 'Select Save Location',
  //     properties: ['openDirectory'],
  //   };

  //   // Show the directory picker dialog
  //   dialog.showOpenDialog(options)
  //     .then(result => {
  //       // result.canceled will be true if the user cancels the dialog
  //       if (!result.canceled) {
  //         // Get the selected directory path
  //         const selectedPath = result.filePaths[0];

  //         // Update the state with the selected path
  //         setFileLocation(selectedPath);

  //         // Optionally, you can do something with the selected path (e.g., save it to backend)
  //         console.log('Selected Path:', selectedPath);
  //       }
  //     })
  //     .catch(err => {
  //       console.error('Error in directory picker dialog:', err);
  //     });
  // };


  // const choosePath = async () => {
  //   console.log("js chhose path called")
  //   // Call the choose_path function directly from the main process
  //   ipcRenderer.send('choosePath');

  //   // const result = await remote.choose_path();

  //   // // Log the selected path (for demonstration purposes)
  //   // console.log('Selected Path:', result);

  //   // // Update the state with the selected path or perform other actions
  //   // if (result) {
  //   //     setFileLocation(result);
  //   // }
  // };


  const choosePath = () => {
    // Send a request to the main process to show directory selection dialog
    ipcRenderer.send('choosePath');
    console.log('choosePath called');
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
        body: JSON.stringify({ image: imageSrc, filePath: fileLocation })
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
              <img alt='' src='https://cdn3.iconfinder.com/data/icons/photography-vol-1-1/66/photography-05-1024.png' width={30} height={30} />
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
          <button className="button" onClick={choosePath}>Change Save Location</button>
          <button className="button">
            Get Floc Size Data
          </button>
        </div>
      </header>
    </div>
  );
}

export default App
