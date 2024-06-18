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
        { data.map((d) => (
            <div key = {d.id}>
                {d.id} , {d.name}, {d.vendor_type}, {d.user}
            </div>
            ))}
        </div>
    )
}

export default CoffeeVendors