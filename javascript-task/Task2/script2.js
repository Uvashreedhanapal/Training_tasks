// Function for task2a
function task2a() {
  // Get user input and convert it to a float
  var userInput = parseFloat(document.getElementById("userInput").value);

  // Check if the userInput is not null and an integer
  if (!isNaN(userInput) && Number.isInteger(userInput)) {
      // If it's a valid integer, add it to  result 
      var result = userInput;
  } else {
      // If not an integer, round the number to 2 decimal 
      var result = userInput.toFixed(2);
  }

  // Display the result 
  document.getElementById("demo").innerHTML = result;
}

// Function to display result with $ after each letter
function displayResult() {
  // Get user input 
  var userInput1 = document.getElementById("userInput1").value;
  
  var result = " ";

  // Loop through each character in userInput1
  for (let i = 0; i < userInput1.length; i++) {
      // add each character with "$" and add it to the result 
      result += userInput1[i] + "$";
  }

  // Display the result 
  document.getElementById("demo1").innerHTML = "Result (add $ after each letter): " + result;
}

// Function to sort the characters 
function sortString() {
  // Get user input 
  var userInput1 = document.getElementById("userInput1").value;
  // Split the string , sort, and join
  var sort = userInput1.split('').sort().join('');
  // Display the sorted string in the "demo1" element
  document.getElementById("demo1").innerHTML = "Sorted String: " + sort;
}
