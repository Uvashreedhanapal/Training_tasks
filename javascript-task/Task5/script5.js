class Mathoperation{
    constructor() {
        this.num1 = 0;
        this.num2 = 0;
    }
  
    // Method for addition
    add() {
        return this.num1 + this.num2;
    }
    // Method for subtraction
    subtract() {
        return this.num1 - this.num2;
    }
  
    // Method for multiplication
    multiply() {
        return this.num1 * this.num2;
    }
  }
  
  // Create object
  const mathoperation = new Mathoperation();
  
  // Function to update num1 and num2 from input fields
  function updateNumbers() {
    mathoperation.num1 = parseInt(document.getElementById('num1').value) || 0;
    mathoperation.num2 = parseInt(document.getElementById('num2').value) || 0;
  }
  
  // Function to perform the selected operation based on the button clicked
  function performOperation(operation) {
    updateNumbers(); // Update num1 and num2 from input fields
  
    let result;
  
    // Call the corresponding method based on the operation
    switch (operation) {
        case 'add':
            result = mathoperation.add();
            break;
        case 'subtract':
            result = mathoperation.subtract();
            break;
        case 'multiply':
            result = mathoperation.multiply();
            break;
        default:
            result = "Invalid operation";
    }
  
    // Display the result on the webpage
    document.getElementById('result').innerText = result;
  }
  