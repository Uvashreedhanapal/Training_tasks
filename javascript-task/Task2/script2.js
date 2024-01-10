function task2a() {
    var userInput = parseFloat(document.getElementById("userInput").value);

    if (!isNaN(userInput) && Number.isInteger(userInput)) {
      var result = userInput;
    } else {
      var result = userInput.toFixed(2);
    }

    document.getElementById("demo").innerHTML = result;
  }

  function displayResult() {
    var userInput1 = document.getElementById("userInput1").value;
    var result = " ";

    for (let i = 0; i < userInput1.length; i++) {
      result += userInput1[i] + "$";
    }

    document.getElementById("demo1").innerHTML = "Result (add $ after each letter): " + result;
  }

  function sortString() {
    var userInput1 = document.getElementById("userInput1").value;
    var sort = userInput1.split('').sort().join('');
    document.getElementById("demo1").innerHTML = "Sorted String: " + sort;
  }