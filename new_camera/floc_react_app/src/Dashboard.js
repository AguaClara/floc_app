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
      <HeaderBox currentTab={0} />
      <div className="contentContainer" style={{ textAlign: 'center', overflowY: 'scroll' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <h1>Dashboard</h1>
          <img
            className="dashboardIcon"
            src="https://png.pngtree.com/png-vector/20230302/ourmid/pngtree-dashboard-line-icon-vector-png-image_6626604.png"
            alt=""
            width="50px"
            height="50px"
          />
        </div>
        <p style={{ marginTop: '-5px' }}>New Floc Images and Data</p>
        <div className="dashboardBoxWrapper" style={{ overflowX: 'scroll', whiteSpace: 'nowrap' }}>
          {/* Render the latest images data */}
          {Array.isArray(latestImagesData) && latestImagesData.length > 0 ? (
            latestImagesData.map((image, index) => (
              <div className="imageWrapper" key={index} style={{ display: 'inline-block', margin: '10px' }}>
                <img src={`data:image/jpeg;base64,${image.image}`} alt={`Image ${index}`} />
                <div className="image-data">
                  <p>ID: {image.id} | Name: {image.name}</p>
                  <p style={{ marginBottom: "0px" }}>
                    Floc data: {image.flocs.map((floc, idx) => (
                      <li key={idx}>ID: {floc.id}, Size: {floc.size}</li>
                    ))}
                  </p>
                </div>
              </div>
            ))
          ) : (
            <p>Loading...</p>
          )}
        </div>
      </div>
    </div>
  );}

export default Dashboard;
