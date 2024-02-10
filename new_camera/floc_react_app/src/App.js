import Dropdown from 'react-bootstrap/Dropdown';
import './App.css';
function App() {
  return (
    <div className="App">
      <p>Hello World</p>
      <header className="Floc App">
        <div className="cameraBox">
          <img className="camera placeholder" imageUrl='https://i.imgur.com/yXOvdOSs.jpg' alt="Camera Placeholder"/>
        </div>
        <div className="exportBox">
          <p>Export Data</p>
          <button className="exportButton">
            Export
          </button>
          <button className="flocSizeData">
            Get Floc Size Data
          </button>
        </div>
        <div className="cameraControlsBox">
          <button className="Start Button">Start</button>
          <button className="End Button">End</button>
          <button className="Change Save Location">Change Save Location</button>
        </div>
      </header>
    </div>
  );
}
export default App