const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');

let flaskProcess = null;

function createWindow() {
    // Start the Flask server
    flaskProcess = spawn('python3', ['src/app.py']);

    flaskProcess.stdout.on('data', (data) => {
        console.log(`Flask stdout: ${data}`);
    });

    flaskProcess.stderr.on('data', (data) => {
        console.error(`Flask stderr: ${data}`);
    });

    // Create the browser window.
    const win = new BrowserWindow({
        width: 680,
        height: 700,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    // Load the index.html of the app.
    win.loadURL('http://localhost:3000/'); // Ensure this matches your React development server URL
}

// This method will be called when Electron has finished initialization
app.whenReady().then(createWindow);

// Quit when all windows are closed, except on macOS
app.on('window-all-closed', () => {
    // if (process.platform !== 'darwin') {
    //     app.quit();
    // }
    app.quit();
});

app.on('quit', () => {
    // Kill the Flask process when the Electron app closes
    console.log('Quitting Electron, terminating Flask server...');
    flaskProcess.kill();
});

app.on('activate', () => {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
