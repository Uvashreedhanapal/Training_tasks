
var even, odd, stringList, newArrayAfterSplice, sorted;
// Task3a
function Task3a() {
  // Get user input 
  var userInput = document.getElementById("userInput2").value;

  // Convert the comma-separated string to an array
  var inputArray = userInput.split(',');

  // to store even and odd index values
  even = [];
  odd = [];

  // Loop through the inputArray and separate even and odd index values
  for (let i = 0; i < inputArray.length; i++) {
    if (i % 2 === 0) {
      even.push(inputArray[i]);
    } else {
      odd.push(inputArray[i]);
    }
  }

  // Remove Odd index values from the list
  stringList = even;

  // Add Two string after 3rd index of the list
  newArrayAfterSplice = inputArray.slice(); // Create a copy of the original array
  newArrayAfterSplice.splice(3, 0, "wonder", "awesome");

  // Sort 
  sorted = inputArray.sort();

  document.getElementById("demo2").innerHTML = "Given Input: " + inputArray;
}

// Functions to display specific results from Task3a
function showEvenIndex() {
  document.getElementById("demo2").innerHTML = "Even Index: " + even;
}

function showOddIndex() {
  document.getElementById("demo2").innerHTML = "Odd Index: " + odd;
}

function showStringList() {
  document.getElementById("demo2").innerHTML = "String List: " + stringList;
}

function spliceOperation() {
  document.getElementById("demo2").innerHTML = "After Splice: " + newArrayAfterSplice;
}

function showSortedValues() {
  document.getElementById("demo2").innerHTML = "Sorted Values: " + sorted;
}

//  Task3b
var list = [];
var mappedResult = [];
var reducedResult = [];
var sortedArray;


function getValues() {
  // Get user input 
  var userInput = document.getElementById("userInput3").value;

  // Convert the comma-separated str to an array 
  list = userInput.split(',').map(Number);

  // Sort in ascending order
  sortedArray = list.slice().sort((a, b) => a - b);

  // Use map to add 1 to each value in the array
  mappedResult = list.map(function (a) {
    return a + 1;
  });

  // Use reduce to add 1 to each value in the array
  reducedResult = list.reduce((acc, value) => {
    acc.push(value + 1);
    return acc;
  }, []);

  
  document.getElementById("demo3").innerHTML = "Given input: " + list;
}

// Functions to display specific results from Task3b
function sortArray() {
  document.getElementById("demo3").innerHTML = "Sorted Array: " + sortedArray;
}

function mapResult() {
  document.getElementById("demo3").innerHTML = "Mapped Result: " + mappedResult;
}

function reduceResult() {
  document.getElementById("demo3").innerHTML = "Reduce Result: " + reducedResult;
}
