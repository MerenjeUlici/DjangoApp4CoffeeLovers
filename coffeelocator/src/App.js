import './App.css';

import {Routes, Route} from 'react-router-dom';

import Home from './components/Home'
import CoffeeVendors from './components/CoffeeVendors'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/home' element={<Home/>}/>
        <Route path='/coffeevendors' element={<CoffeeVendors/>}/>

      </Routes>
    </div>
  );
}

export default App;
