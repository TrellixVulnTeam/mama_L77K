import React from 'react';
import './App.css';
import { BrowserRouter } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import Main from './components/Main'


function App() {
  

  return (
    <BrowserRouter>
    <div className="App"> 
          <Main/>
    </div>
    </BrowserRouter>
  
  );
}

export default App;
