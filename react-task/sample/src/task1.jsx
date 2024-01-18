
import React, { Component } from "react";

class Tables extends Component {
  render() {
    return (
      <>
        <div id='1'>
          <h2>Table creation</h2>
          <center>
            <table>
              <thead>
                <tr>
                  <th>id</th>
                  <th>name</th>
                  <th>marks</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>john</td>
                  <td>95</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Alice</td>
                  <td>93</td>
                </tr>
              </tbody>
            </table>
          </center>
        </div>
        <div id='2'>
          <h2>FORM</h2>
          <form action="/submit" method="post">
            {/* Text Input */}
            <label htmlFor="name">Name:</label>
            <input type="text" id="name" name="name" required />
            <br></br>
            {/* Email Input */}
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" name="email" required />
            <br></br>
            {/* Password Input */}
            <label htmlFor="password">Password:</label>
            <input type="password" id="password" name="password" required />
            <br></br>
            {/* Radio Buttons */}
            <label>Gender:</label>
            <label htmlFor="male">
              <input type="radio" id="male" name="gender" value="male" /> Male
            </label>
            <label htmlFor="female">
              <input type="radio" id="female" name="gender" value="female" /> Female
            </label>
            <br></br>
            {/* Checkbox */}
            <label>
              <input type="checkbox" name="newuser" value="yes" /> Tick if you are a new user
            </label>
            <br></br>
            {/* Select Dropdown */}
            <label htmlFor="country">Country:</label>
            <select id="country" name="country" >
            <option value="india">INDIA</option>
              <option value="usa">USA</option>
              <option value="canada">Canada</option>
              <option value="uk">UK</option>
            </select>
            <br></br>
            {/* Textarea */}
            <label htmlFor="message">Message:</label>
            <textarea id="message" name="message" rows="4" cols="50"></textarea>
            <br></br>
            {/* Submit Button */}
            <button type="submit">Submit</button>
          </form>
        </div>
      </>
    );
  }
}

export default Tables;
