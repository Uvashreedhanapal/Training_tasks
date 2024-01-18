import React from "react";
import { Link ,useNavigate} from 'react-router-dom';

function MainPage() {

  const navigate = useNavigate();

  const handleLogout = () => {
      
      navigate('/login');
  };
    return (
        <>
            <Link to="/Tables">Click here for Task1</Link><br/>
            <Link to="/AddNumbers">Click here for Task2</Link><br/>
            <Link to="/JsontoTable">Click here for Task3</Link><br/>
            <Link to="/WeatherApp">Click here for Task4</Link><br/>
            <button
            type="button"
            style={{
              position: 'absolute',
              top: '10px', 
              right: '10px', 
            }}
            onClick={handleLogout}
          >
            Logout
          </button>
            <br />
      
        </>
    );
}

export default MainPage;
