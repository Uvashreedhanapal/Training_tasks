// import React, { useState } from 'react';

// const WeatherApp = () => {
//   const [query, setQuery] = useState('');
//   const [weatherData, setWeatherData] = useState(null);

//   const callWeatherAPI = async () => {
//     try {
//       const response = await fetch(
//         `https://weatherapi-com.p.rapidapi.com/current.json?q=${query}`,
//         {
//           method: 'GET',
//           headers: {
//             'X-RapidAPI-Key': 'ea1736c136msh0f5c187e704eedbp15d852jsn9c8eb45d2ffd',
//             'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
//           },
//         }
//       );

//       const data = await response.json();
//       setWeatherData(data);
//     } catch (error) {
//       console.error('Error fetching weather data:', error);
//     }
//   };

  
// return (
//     <div>
//       <h2>API CALL TASK</h2>
//       <input type="text" placeholder="Enter location" value={query} onChange={(e) => setQuery(e.target.value)}/>
//       <br/><button onClick={callWeatherAPI}>Get Weather</button>

//       {weatherData && (
//         <div>
//           <h2>Weather Information for {query}</h2>
//           <p>Temperature: {weatherData.current.temp_c}°C</p>
//           <p>Condition: {weatherData.current.condition.text}</p>        
//         </div>
//       )}
//     </div>
//   );



// }
// export default WeatherApp;

import React, { Component } from 'react';

class WeatherApp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      query: '',
      weatherData: null,
    };
  }

  callWeatherAPI = async () => {
    try {
      const response = await fetch(
        `https://weatherapi-com.p.rapidapi.com/current.json?q=${this.state.query}`,
        {
          method: 'GET',
          headers: {
            'X-RapidAPI-Key': 'ea1736c136msh0f5c187e704eedbp15d852jsn9c8eb45d2ffd',
            'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
          },
        }
      );

      const data = await response.json();
      this.setState({ weatherData: data });
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  };

  render() {
    const { query, weatherData } = this.state;

    return (
      <div>
        <h2>API CALL TASK</h2>
        <input
          type="text"
          placeholder="Enter location"
          value={query}
          onChange={(e) => this.setState({ query: e.target.value })}
        />
        <br />
        <button onClick={this.callWeatherAPI}>Get Weather</button>

        {weatherData && (
          <div>
            <h2>Weather Information for {query}</h2>
            <p>Temperature: {weatherData.current.temp_c}°C</p>
            <p>Condition: {weatherData.current.condition.text}</p>
          </div>
        )}
      </div>
    );
  }
}

export default WeatherApp;
