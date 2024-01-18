import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Tables from './task1';
import AddNumbers from './task2';
import JsontoTable from './task3';
import WeatherApp from './task4';
import LoginPage from './task5';
import SignupForm from './signup';
import MainPage from './main';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
       

        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/SignupForm" element={<SignupForm />} />
          <Route path="/MainPage" element={<MainPage />} />
          <Route path="/Tables" element={<Tables />} />
          <Route path="/AddNumbers" element={<AddNumbers />} />
          <Route path="/JsontoTable" element={<JsontoTable />} />
          <Route path="/WeatherApp" element={<WeatherApp />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
