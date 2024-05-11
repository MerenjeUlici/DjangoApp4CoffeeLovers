import React from 'react'
import {useState, useEffect} from 'react';

const CoffeeVendors = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://0.0.0.0:8000/api/vendors/')
          .then(res => res.json())
          .then(data => setData(data));
        }, [])

    return(
        <div>
        <div> CoffeeVendors </div>
        <p> {JSON.stringify(data)} </p>
        </div>
    )
}

export default CoffeeVendors