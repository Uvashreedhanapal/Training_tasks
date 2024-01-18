import React, { useState } from "react";
import { Link } from 'react-router-dom';

const SignupForm = () => {
  // input values
  const [email, setemail] = useState("");
  const [first_name, setFirstName] = useState('');
  const [company, setcompany] = useState('');
  const [password, setpassword] = useState("");
  const [confirmPassword, setconfirmPassword] = useState("");
  const [phone_number, setphone_number] = useState('');
  const [error, setError] = useState("");

  // Function to handle the signup process when the form is submitted
  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      // Validate phone number format
      if (!/^(\+[0-9]+)$/.test(phone_number)) {
        setError('Please enter a valid phone number with a country code.');
        return;
      }

      // username from email 
      const username = email.split('@')[0];

      // last name from first name 
      //here firstname >2 and <=20 otherwise empty
      const last_name = (first_name.length > 2 && first_name.length <= 20) ? first_name : '';

      // Make a POST request 
      const response = await fetch('https://app.qualdo.ai/iam/signup', {
        method: 'POST',
        body: JSON.stringify({
          email,
          username: username,
          first_name,
          last_name,
          company,
          password,
          phone_number,
          user_signup_type: 'qualdo_db_auth',
        }),
        headers: {
          'Content-Type': 'application/json',
          'Api-type': 'qualdo_db_auth'
        },
      });

      // Parse the response data
      const responseData = await response.json();

      
      if (responseData.code === 200) {
        console.log('User signed up successfully!');
        // Display success message to the user using alert
        alert(responseData.message);
        
      } else if (responseData.code === 401 && responseData.message === 'User already exists') {
        console.log('User already exists. Provide a different email address.');
        setError('User already exists. Provide a different email address.');
      } else {
        console.error('Error during signup:', responseData.message);
        setError('Signup failed');
      }
    } catch (error) {
      console.error('Error during signup:', error.message);
      setError('Signup failed');
    }
  }

  return (
    <div>
      <h2>Signup</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form>
        
        <label>Email:
          <input type="email" value={email} onChange={(e) => setemail(e.target.value)} />
        </label><br />
        <label>
          First Name:
          <input
            type="text"
            value={first_name}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </label><br />
        <label>
          Company:
          <input
            type="text"
            value={company}
            onChange={(e) => setcompany(e.target.value)}
          />
        </label><br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setpassword(e.target.value)} />
        </label><br />
        <label>
          Confirm Password:
          <input type="password" value={confirmPassword} onChange={(e) => setconfirmPassword(e.target.value)} />
        </label><br />
        <label>
          Phone Number (+Country Code):
          <input
            type="text"
            value={phone_number}
            onChange={(e) => setphone_number(e.target.value)}
            placeholder="+1234567890"
          />
        </label><br />
        
        <button type="submit" onClick={handleSignup}>Sign Up</button><br />
        <Link to="/login">If you have an account, Login here</Link>
      </form>
    </div>
  );
};

export default SignupForm;
