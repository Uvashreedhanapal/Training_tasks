const items = [];
     let result;
 
     function addItem() {
       const key = document.getElementById('keyInput').value;
       const itemKey = document.getElementById('itemKeyInput').value;
       const selected = document.getElementById('selectedInput').value;
 
       items.push({
         key: key,
         item_key: itemKey,
         selected: selected
       });
 
       console.log(items);
     }
 
     function displayAll() {
       result = items.map(item => ({
         key: item.key,
         item_key: item.item_key,
         selected: item.selected
       }));
 
       console.log(result);
       document.getElementById('demo4').innerHTML = result.map(item => JSON.stringify(item, null, 2));
     }
 
     function iterateDisplay() {
     
       document.getElementById('demo4').innerHTML = ''; // Clear previous content
 
       for (let i = 0; i < result.length; i++) {
         let object = result[i];
         for (const [key, value] of Object.entries(object)) {
           document.getElementById("demo4").innerHTML += "<li>" + key + ": " + value + "</li>";
         }
       }
     }
 
     function displaySelected() {
       const selectedItems = items.filter(item => item.selected === 'true');
       result = selectedItems.map(item => ({
         key: item.key,
         item_key: item.item_key,
         selected: item.selected
       }));
 
       console.log(result);
       document.getElementById('demo4').innerHTML = result.map(item => JSON.stringify(item, null, 2)).join('<br><br>');
     }

     //task4b

// Empty list
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
      
      var output= document.getElementById("demo5");
      output.innerHTML = "Current List:<br>" + JSON.stringify(dictionaryList, null, 2);

        // Clear input fields
        document.getElementById("keyInput").value = "";
        document.getElementById("valueInput").value = "";
    } else {
        alert("List is full. Cannot add more dictionaries.");
    }
}