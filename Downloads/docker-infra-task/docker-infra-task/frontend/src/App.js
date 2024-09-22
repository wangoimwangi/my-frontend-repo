import React from 'react';
import logo from './logo.svg';
import './App.css';

// TODO: point frontend to backend url
const BACKEND_URL = "";

function App() {
  let [input, setInput] = React.useState('');
  let [message, setMessage] = React.useState('');

  function sendMessage() {
    console.log(`Sending message: "${input}"`);
    fetch(BACKEND_URL + '/api/msg/' + input, {
      method: 'POST', // or 'PUT'
    })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        fetchMessage(data.msg_id);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  function fetchMessage(msgId) {
    console.log(`Fetching message > msgId=${msgId}`)
    fetch(BACKEND_URL + '/api/msg/' + msgId)
      .then(response => response.json())
      .then(data => {
        console.log(`Success:`, data);
        setMessage(data.msg);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
          <label>
            Send a message:
            <input
              type={'text'}
              value={input}
              onChange={(event) => setInput(event.target.value)}
            />
            <button onClick={sendMessage}>Submit</button>
          </label>
        </div>
        <div><span>Last Message: </span> "<span style={{ color: 'orange' }}>{message}</span>"</div>
      </header>
    </div>
  );
}

export default App;
