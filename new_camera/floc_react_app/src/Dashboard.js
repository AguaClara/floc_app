import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import HeaderBox from './headerBox.jsx';

const Dashboard = () => {
  const [latestImagesData, setLatestImagesData] = useState([]);

  useEffect(() => {
    fetchLatestImagesData(); // Fetch data when component mounts
  }, []);

  const fetchLatestImagesData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/images/');
      const data = await response.json();
      setLatestImagesData(data); // Update state with fetched data
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <HeaderBox currentTab={0}/>
      <div className="contentContainer" style={{textAlign: 'center', overflowY: 'scroll'}}>
        <h1 className="dashboard-title">Dashboard</h1>
        <p className="dashboard-text">New Floc Images and Data</p>
        {/* Render the latest images data */}
        {latestImagesData.map((image, index) => (
          <div className="dashboard-text" key={index}>
            <img src={`data:image/jpeg;base64,${image.image}`} alt={`Image ${index}`} />
            <div>
                <span>ID: {image.id} |  </span>
                <span>Name: {image.name} |  </span>
                <span>Flocs: {image.flocs.map(floc => `ID: ${floc.id}, Size: ${floc.size}`).join(', ')}</span>
              </div>
            {/* Render other data associated with each image */}
          </div>
        ))}
        <div style={{ textAlign: 'center' }}>
          <Link to="/" className="button" style={{ textDecoration: 'none' }}>Go to App</Link>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;