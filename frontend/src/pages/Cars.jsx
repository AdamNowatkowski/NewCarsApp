import React from 'react'

import Layout from '../components/Layout'
import Card from '../components/Card'
import { useState, useEffect } from 'react'

const Cars = () => {
    const [cars, setCars] = useState([])
    const [brand, setBrand] = useState('')
    const [isPending, setIsPending] = useState(true)

    useEffect(() => {
      fetch(`http://localhost:8000/cars?brand=${brand}`)
      .then(response=>response.json())
      .then(json=>setCars(json))
      setIsPending(false)
      }, [brand]
    )

    const handleChangeBrand = (event) => {
      setCars([])
      setBrand(event.target.value)
      setIsPending(true)
    }


    return (
      <Layout >
          <h2 className='font-bold font-mono text-lg text-center my-4'>Cars - {brand?brand:"all brands"} </h2>
          <div className='mx-8'>
            <label htmlFor='cars'>Choose a brand:</label>
            <select name='cars' id='cars' onChange={handleChangeBrand}>
              <option value="">All cars</option>
              <option value="Fiat">Fiat</option>
              <option value="Opel">Opel</option>

            </select>
          </div>
          <div>
            {isPending && <div> <h2>Loading cars, brand: {brand} ...</h2> </div>}
          </div>

          <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
            {cars && cars.map(
              (el) => {
              return (<Card key={el._id} car = {el} />)
              }
            )
}
          </div>
      </ Layout>

      
    )
}

export default Cars;