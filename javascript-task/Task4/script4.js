// Task4a
const items = [];
let result;

// Function to add an item to the list
function addItem() {
  // Get values from input 
  const key = document.getElementById('keyInput').value;
  const itemKey = document.getElementById('itemKeyInput').value;
  const selected = document.getElementById('selectedInput').value;

  // Push the new item  to the items 
  items.push({
    key: key,
    item_key: itemKey,
    selected: selected
  });


  console.log(items);
}

// Function to display all items in a formatted way
function displayAll() {
  // Map the items array to a new array with selected properties
  result = items.map(item => ({
    key: item.key,
    item_key: item.item_key,
    selected: item.selected
  }));

  // Log the result array to the console
  //console.log(result);

  // Display the result 
  document.getElementById('demo4').innerHTML = result.map(item => JSON.stringify(item, null, 2));
}

// Function to iterate and display items
function iterateDisplay() {
  // Clear previous content 
  document.getElementById('demo4').innerHTML = '';

  // Iterate through the result array and display key-value pairs
  for (let i = 0; i < result.length; i++) {
    let object = result[i];
    for (const [key, value] of Object.entries(object)) {
      document.getElementById("demo4").innerHTML += "<li>" + key + ": " + value + "</li>";
    }
  }
}

// Function to display selected items
function displaySelected() {
  // Filter items based on the 'selected' property
  const selectedItems = items.filter(item => item.selected === 'true');

  // Map the selected items to a new array with selected properties
  result = selectedItems.map(item => ({
    key: item.key,
    item_key: item.item_key,
    selected: item.selected
  }));

  // Log the result array to the console
  //console.log(result);

  // Display the result in the "demo4" element with line breaks
  document.getElementById('demo4').innerHTML = result.map(item => JSON.stringify(item, null, 2)).join('<br><br>');
}

// Task4b
// Array to store dictionaries
var dictionaryList = [];

// Function to add a dictionary to the list
function addDictionary() {
  // Get values from input fields
  var key = document.getElementById("keyInput").value;
  var value = document.getElementById("valueInput").value;

  // Check if the length of the list is less than 10
  if (dictionaryList.length < 10) {
    // Create a new dictionary
    var newDictionary = {
      key: key,
      value: value
    };

    // Add the new dictionary to the list
    dictionaryList.push(newDictionary);

    // Display the current list 
    var output = document.getElementById("demo5");
    output.innerHTML = "Current List:<br>" + JSON.stringify(dictionaryList, null, 2);

    // Clear input fields
    document.getElementById("keyInput").value = "";
    document.getElementById("valueInput").value = "";
  } else {
    
    alert("List is full. Cannot add more dictionaries.");
  }
}
