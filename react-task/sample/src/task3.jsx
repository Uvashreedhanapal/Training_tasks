// import React from "react";

// function JsontoTable() {
//   const data = [
//     {
//       "name": "uva",
//       "department": "Engg",
//       "dob": "18/12/2000"
//     },
//     {
//       "name": "Alice",
//       "department": "Medical",
//       "dob": "18/12/2001"
//     },
//     {
//       "name": "John",
//       "department": "Medical",
//       "dob": "11/10/2003"
//     },
//     {
//       "name": "Rose",
//       "department": "Engg",
//       "dob": "19/12/2001"
//     },
//     {
//       "name": "Jack",
//       "department": "Engg",
//       "dob": "16/11/2000"
//     }
//   ];

//   return (
//     <div className="jsontable">
//         <center>
//             <h1>Json data to Table</h1>
//       <table>
//         <thead>
//           <tr>
//             <th>Name</th>
//             <th>Department</th>
//             <th>DOB</th>
//           </tr>
//         </thead>
//         <tbody>
//           {data.map((item, index) => (
//             <tr key={index}>
//               <td>{item.name}</td>
//               <td>{item.department}</td>
//               <td>{item.dob}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table></center>
//     </div>
//   );
// }

// export default JsontoTable;


import React, { Component } from "react";

class JsontoTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
    // Add state if needed
    };
  }

  render() {
    const data = [
      {
        "name": "uva",
        "department": "Engg",
        "dob": "18/12/2000"
      },
      {
        "name": "Alice",
        "department": "Medical",
        "dob": "18/12/2001"
      },
      {
        "name": "John",
        "department": "Medical",
        "dob": "11/10/2003"
      },
      {
        "name": "Rose",
        "department": "Engg",
        "dob": "19/12/2001"
      },
      {
        "name": "Jack",
        "department": "Engg",
        "dob": "16/11/2000"
      }
    ];

    return (
      <div className="jsontable">
        <center>
          <h1>Json data to Table</h1>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Department</th>
                <th>DOB</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => (
                <tr key={index}>
                  <td>{item.name}</td>
                  <td>{item.department}</td>
                  <td>{item.dob}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </center>
      </div>
    );
  }
}

export default JsontoTable;
