import './App.css';

import {Routes, Route} from 'react-router-dom';

import Home from './components/Home'
import CoffeeVendors from './components/CoffeeVendors'
import Articles from './components/Articles'
import Admin from './components/Admin'
import Navbar from './components/Navbar'


function App() {
  return (

    <>
    <Navbar/>
    <div className="App">

      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/coffeevendors' element={<CoffeeVendors/>}/>
        <Route path='/articles' element={<Articles/>}/>
        <Route path='/admin' element={<Admin/>}/>

      </Routes>
    </div>
    </>
  );
}

export default App;
