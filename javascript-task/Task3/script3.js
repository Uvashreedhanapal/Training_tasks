var even, odd, stringList, newArrayAfterSplice, sorted;
function Task3a() {
  var userInput = document.getElementById("userInput2").value;

  // Convert the comma-separated string to an array
  var inputArray = userInput.split(',');
  even = [];
  odd = [];
  for (let i = 0; i < inputArray.length; i++) {
    if (i % 2 === 0) {
      even.push(inputArray[i]);
    } else {
      odd.push(inputArray[i]);
    }
  }

  // Remove Odd index values from the list
  stringList = even;
  // Add Two more string values after 3rd index of the list
  newArrayAfterSplice = inputArray.slice(); // Create a copy of the original array
  newArrayAfterSplice.splice(3, 0, "wonder", "awesome");
  sorted=inputArray.sort()

  document.getElementById("demo2").innerHTML = "Given Input: " +inputArray;
}

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

//task3b
var list = [];
  var mappedResult = [];
  var reducedResult = [];
  var sortedArray;

 function getValues() {
    var userInput = document.getElementById("userInput3").value;
    list = userInput.split(',').map(Number);
    // sort in ascending order
    sortedArray = list.slice().sort((a, b) => a - b);
    // using map to add 1 to each value
    mappedResult = list.map(function (a) {
       return a + 1;
    });
    //using reduce to add 1 to each value
    reducedResult = list.reduce((acc, value) => {
      acc.push(value + 1);
      return acc;
  }, []);
    document.getElementById("demo3").innerHTML = "Given input: " + list;
}

function sortArray() {
    document.getElementById("demo3").innerHTML = "Sorted Array: " + sortedArray;
}

function mapResult() {
    document.getElementById("demo3").innerHTML = "Mapped Result: " + mappedResult;
}

function reduceResult() {
            
document.getElementById("demo3").innerHTML = "Reduce Result: " + reducedResult;
}