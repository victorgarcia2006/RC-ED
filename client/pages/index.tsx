import React, { useEffect } from 'react'
import { getSimulationData } from './api/monitoreo'

function HomePage() {
  useEffect(() => {
    getSimulationData()
      .then(response => console.log(response))
      .catch(error => console.error(error))
  }, [])

  return (
    <div>
      <h1>Home Page</h1>
    </div>
  )
}

export default HomePage
