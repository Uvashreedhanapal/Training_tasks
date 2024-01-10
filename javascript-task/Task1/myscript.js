function String_method() {
    // Get the input value from the form
    var userInput = document.getElementById("userInput").value;
    
    // Perform string methods on the input
    var result = "charAt--Result: " + userInput.charAt(0) + "<br>" +
                 "slice--Result: " + userInput.slice(6, 13) + "<br>" +
                 "slice 2--Result:" + userInput.slice(-12, -6) + "<br>" +
                 "substr--Result:" + userInput.substr(7, 2) + "<br>" +
                 "Uppercase--Result: " + userInput.toUpperCase();

    // Display the result in the demo element
    document.getElementById("demo").innerHTML = result;
}
function Number_method() {
    // Get the input value from the form
    var userInput =parseFloat( document.getElementById("userInput1").value);
    
    // Perform number methods on the input
    var result = "Exponential--Result: " + userInput.toExponential(2) + "<br>" +
                 "Fixed--Result: " + userInput.toFixed(2) + "<br>" +
                 "Precision--Result:" + userInput.toPrecision(2) + "<br>" +
                 "parseInt--Result: " + parseInt(userInput);

    // Display the result in the demo element
    document.getElementById("demo1").innerHTML = result;
}
function Array_method() {
    // Get the input value from the form
    var userInput = document.getElementById("arrayInput").value;

    // Convert the comma-separated string to an array
    var inputArray = userInput.split(',');
    let slice=inputArray.slice(2)
    let reverse=inputArray.reverse()
    let sort=inputArray.toSorted()

    let filter=inputArray.filter(myFunction);
    function myFunction(value, index, array) {
        return value > 18;
      }
   
    let mapping=inputArray.map(myFunction);
    function myFunction(value){
        return value*10
    }

    // Display the result
    document.getElementById("demo2").innerHTML ="slice: "+ slice + "<br>"+ 
            "reverse: "+reverse+ "<br>"+ 
            "sorted: "+sort+ "<br>"+
            "filter: "+filter+"<br>"+
            "map: "+mapping;
}
function Statement() {
    // Get the input value from the form
    var userInput =document.getElementById("Input").value;
        // Validate if the input is a valid number
    if (isNaN(userInput) || userInput === "" || userInput <0 || userInput > 1001) {
            document.getElementById("demo3").innerHTML = "Please enter a valid number within 1001.";
            return;
     }
    x=parseInt(userInput)
    switch(true){
        case x>20 && x<999:
            x="you have enough coins to play next round!"
            break;
        case x<20:
            x="you did not have enough coins to play :)"
            break;
        case x==1000:
            x="you are already finished the game"
            
    }
    // Display the result in the demo element
    document.getElementById("demo3").innerHTML =x;
}
function Loop() {
    var userInput = document.getElementById("Input1").value;

    // Convert the comma-separated string to an array
    var list  = userInput.split(',');
    // Perform number methods on the input
    var result =" "
    for(let i=0;i<list.length;i++){
        result+=list[i] +"<br>";
    }

    // Display the result in the demo element
    document.getElementById("demo4").innerHTML = result;
}
let userInputArray = [];

function map() {
  const key = document.getElementById('key').value;
  const value = document.getElementById('value').value;

  if (key && value) {
    const newItem = [key, parseInt(value)];
    userInputArray.push(newItem);
    
    // Display current user input
    document.getElementById('demo5').innerText =JSON.stringify(userInputArray);

    let text = "Entries: ";
    for (const entry of userInputArray.entries()) {
      text += entry + "\n" ;
    }
    document.getElementById('entriesResult').innerText = text;

    // Clear form inputs
    document.getElementById('key').value = '';
    document.getElementById('value').value = '';
    
  } else {
    alert('Please fill out both key and value.');
  }


}

