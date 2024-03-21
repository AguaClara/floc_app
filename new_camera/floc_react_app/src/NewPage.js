import React from 'react';
import {Link} from 'react-router-dom';
import HeaderBox from './headerBox.jsx';


const NewPage = () => {
  return (
    <div>
      <HeaderBox currentTab={0}/>
      <div className="contentContainer">
        <h1>New Page</h1>
        <p>This is the content of the new page.</p>
        <div style={{ textAlign: 'center' }}>
          <Link to="/" className="button" style={{ textDecoration: 'none' }}>Go to App</Link>
        </div>
      </div>
    </div>
    
  );
}

export default NewPage;
