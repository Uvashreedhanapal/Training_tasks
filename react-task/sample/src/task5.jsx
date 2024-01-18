import React, { useState, } from "react";
import { Link } from 'react-router-dom';
import {Routes, Route, useNavigate} from 'react-router-dom';
// API_URL="";

function Loginpage(){
    const[email,setemail]=useState("");
    const[password,setpassword]=useState("");
    const[error,setError]=useState("");
    const navigate = useNavigate();

    
    const handleLogin = async () => {
    const response = await fetch('https://app.qualdo.ai/iam/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'api-type': 'qualdo_db_auth'
        },
        body: JSON.stringify({
          email,
          password,
        }),
      });
    const data=await response.json();
    
    if (data.code == 200) {
        console.log('Login Successful:', data);
        navigate('/MainPage');
      } else {
        console.error('Login Failed:', data);
        setError('Invalid credentials. Please try again.');
      }
      
      };
    // } catch (error) {
    //   console.error('Login Failed:', error.message);
    //   setError('An error occurred. Please try again.');
    // }
  // };

  return(
        <div>
           <h2>Login</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}    
            <form >
        <label>Email:<span>*</span></label>
        <input type="email" value={email} onChange={(e) => setemail(e.target.value)}/>
        <label>Password:<span>*</span></label>
        <input type="password" value={password} onChange={(e) => setpassword(e.target.value)}/>
        <br></br>
        <label>
        <input type="checkbox" name="remember"/> Remember Me
        </label>
        <button type="button" onClick={handleLogin}>Login</button><br/>
        {/* <button type="button" >Sign up</button> */}
        <Link to="/SignupForm"> Don't have an account? Sign up here</Link>
        
      </form>
        </div>

    );
  };



//   const FirstPage = () => {
//     return (
//       <div>
//         <Loginpage />
//         <SignupForm />
//       </div>
//     );
//   };

export default Loginpage;
