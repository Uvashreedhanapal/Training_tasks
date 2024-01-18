// import React, { useState } from "react";
// function AddNumbers() {
//   const [num1, setNum1] = useState("");
//   const [num2, setNum2] = useState("");
//   const [result, setResult] = useState(null);

//   const handleNum1Change = (e) => {
//     const input = e.target.value;
//     // Only allow numeric input
//     if (!isNaN(input)) {
//       setNum1(input);
//     }
//   };

//   const handleNum2Change = (e) => {
//     const input = e.target.value;
//     // Only allow numeric input
//     if (!isNaN(input)) {
//       setNum2(input);
//     }
//   };

//   const handleAdd = () => {
//     const sum = parseFloat(num1) + parseFloat(num2);
//     setResult(sum);
//   };

//   return (
//     <div>
//       <label htmlFor="num1">Enter number 1:</label>
//       <input type="text" id="num1" value={num1} onChange={handleNum1Change} placeholder="Enter a number" />
//       <br />
//       <label htmlFor="num2">Enter number 2:</label>
//       <input
//         type="text" id="num2" value={num2} onChange={handleNum2Change} placeholder="Enter a number" />
//       <br />

//       <button class="button button4" onClick={handleAdd}>Add</button>

//       {result !== null && (
//         <p>
//           Result:{result}
//         </p>
//       )}
//     </div>
//   );
// }

// export default AddNumbers;


import React, { Component } from "react";

class AddNumbers extends Component {
  constructor(props) {
    super(props);
    this.state = {
      num1: "",
      num2: "",
      result: null,
    };
  }

  handleNum1Change = (e) => {
    const input = e.target.value;
    // Only allow numeric input
    if (!isNaN(input)) {
      this.setState({ num1: input });
    }
  };

  handleNum2Change = (e) => {
    const input = e.target.value;
    // Only allow numeric input
    if (!isNaN(input)) {
      this.setState({ num2: input });
    }
  };

  handleAdd = () => {
    const sum = parseFloat(this.state.num1) + parseFloat(this.state.num2);
    this.setState({ result: sum });
  };

  render() {
    const { num1, num2, result } = this.state;

    return (
      <div>
        <label htmlFor="num1">Enter number 1:</label>
        <input
          type="text"
          id="num1"
          value={num1}
          onChange={this.handleNum1Change}
          placeholder="Enter a number"
        />
        <br />
        <label htmlFor="num2">Enter number 2:</label>
        <input
          type="text"
          id="num2"
          value={num2}
          onChange={this.handleNum2Change}
          placeholder="Enter a number"
        />
        <br />

        <button className="button button4" onClick={this.handleAdd}>
          Add
        </button>

        {result !== null && <p>Result: {result}</p>}
      </div>
    );
  }
}

export default AddNumbers;


