import React, { useState, useEffect } from 'react';

const CameraDropdown = () => {
  const [cameras, setCameras] = useState([]);

  useEffect(() => {
    async function getCameras() {
      try {
        const devices = await navigator.mediaDevices.enumerateDevices();
        const videoDevices = devices.filter(device => device.kind === 'videoinput');
        setCameras(videoDevices);
      } catch (error) {
        console.error('Error getting cameras:', error);
      }
    }

    getCameras();
  }, []);

  return (
    <select>
      {cameras.map(camera => (
        <option key={camera.deviceId} value={camera.deviceId}>
          {camera.label || `Camera ${cameras.indexOf(camera) + 1}`}
        </option>
      ))}
    </select>
  );
};

export default CameraDropdown;