import React from 'react';
import './App.css';
import {Link, useNavigate} from 'react-router-dom';

const HeaderBox = (props) => {

    const currTab = props.currentTab;
    const navigate = useNavigate();

    const handleTabClick = (event, tabIndex) => {
        //fixme: button appearance doesn't update
            //when first navigating to newpage
        event.preventDefault();
        console.log(currTab);
        let route;
        if (tabIndex === 0)
            route = '/new';
        else if (tabIndex === 1)
            route = '/';
        else if (tabIndex === 2)
            route = '/Setting';
        navigate(route);
    };

    return (
    <div className = "headerBox">
        <div className = "logoBox">
            <img className = "logo" src="https://res.cloudinary.com/scalefunder/image/fetch/s--7ZiRgq59--/f_auto,fl_lossy,q_auto/https://github.com/AguaClara/public_relations/blob/master/AguaClara%2520Official%2520Logo/FINAL%2520LOGO%25202.0.png%3Fraw%3Dtrue" alt="" width={200} height={60} />
        </div>
        <div className = "tabsBox">
            <Link className={currTab === 0 ? 'dataPageButton active' : 'dataPageButton'} onClick={(e) => handleTabClick(e,0)} style={{ textDecoration: 'none'}} >Dashboard</Link>
            <Link className={currTab === 1 ? 'cameraPageButton active' : 'cameraPageButton'} onClick={(e) => handleTabClick(e,1)} style={{ textDecoration: 'none'}} >Camera</Link>
            <Link className={currTab === 2 ? 'settingsPageButton active' : 'settingsPageButton'} onClick={(e) => handleTabClick(e,2)} style={{ textDecoration: 'none'}} >Settings</Link>
        </div>
    </div>
    );
  };
  
  export default HeaderBox;