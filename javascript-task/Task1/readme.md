Java script :
Number methods

    The toString() method returns a number as a string.
    The toExponential() Method
    toExponential() returns a string, with a number rounded and written using exponential notation.
    toFixed() returns a string, with the number written with a specified number of decimals:
    toPrecision() returns a string, with a number written with a specified length
    valueOf() returns a number as a number.
    Number.isInteger() Returns true if the argument is an integer
    Number.parseFloat() Converts a string to a number
    Number.parseInt() Converts a string to a whole number

String methods
    Extracting String Characters
    There are 4 methods for extracting string characters:
      The at(position) Method
      The charAt(position) Method
      The charCodeAt(position) Method
      Using property access [] like in arrays
    Extracting String Parts
    There are 3 methods for extracting a part of a string:
      slice(start, end)
      substring(start, end)
      substr(start, length)
    Converting to Upper and Lower Case
      A string is converted to upper case with toUpperCase()
      A string is converted to lower case with toLowerCase()
    JavaScript String concat()
      concat() joins two or more strings
    JavaScript String trim()
      The trim() method removes whitespace from both sides of a string





Arrays and Arrays methods
  The length()  property returns the length (size) of an array
  The JavaScript method toString() converts an array to a string of (comma separated) array values
  The at() method returns an indexed element from an array.
  The join() method also joins all array elements into a string.It behaves just like toString(), but in addition you can specify the separator
  The pop() method removes the last element from an array
  The push() method adds a new element to an array (at the end)
  The shift() method removes the first element of an array (and "shifts" the other elements to the left)
  The unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements
  The length property provides an easy way to append new elements to an array without using the push() method.
    fruits[fruits.length] = "Kiwi";
  The concat() method creates a new array by merging (concatenating) existing arrays
  const myChildren = myGirls.concat(myBoys);
  The splice() method adds new items to an array.1 ele->position where new elements should be added,2 ele->how many elements should be removed,3->ele need to be added
  The slice() method slices out a piece of an array.
Array search:
  The indexOf() method searches an array for an element value and returns its position.
    fruits.indexOf("Apple")
  Array.includes()  to check if an element is present in an array
    fruits.includes("Mango"); // is true
  The find() method returns the value of the first array element that passes a test function.
  The findIndex() method returns the index of the first array element that passes a test function.

Sorting array:
  Array sort()  method sorts an array alphabetically:
  Array reverse() method reverses the elements in an array
  Array toSorted() method as a safe way to sort an array without altering the original array
  Array toReversed() method as a safe way to reverse an array without altering the original array.

Array iteration:
  The map() method creates a new array by performing a function on each array element.
  The flatMap() method first maps all elements of an array and then creates a new array by flattening the array.
  The filter() method creates a new array with array elements that pass a test.
  The reduce() method runs a function on each array element to produce (reduce it to) a single value.
  The every() method checks if all array values pass a test.returns true/false
  The some() method checks if some array values pass a test.
  Array with() method as a safe way to update elements in an array without altering the original array.
    
Statements
    Semicolons separate JavaScript statements.
    JavaScript statements are composed of:
      Values, Operators, Expressions, Keywords, and Comments.
    JavaScript uses the keywords var, let and const to declare variables.
    Variables declared inside a { } block cannot be accessed from outside the block
    An expression is a combination of values, variables, and operators, which computes to a value.
    JavaScript keywords are used to identify actions to be performed.
    Code after double slashes // or between /* and */ is treated as a comment.

Looping conditions
  If-else
  Switch case
  For loop
  For in loop
  While loop

Maps
    Creating a map:
    Passing an Array to new Map()
      const fruits = new Map([
      ["apples", 500], ["bananas", 300],["oranges", 200]]);
    Create a Map and use Map.set()
    add elements to a Map with the set() method
    The get() method gets the value of a key in a Map
    The size property returns the number of elements in a Map
    The delete() method removes a Map element
    The has() method returns true if a key exists in a Map
    The forEach() method calls a function for each key/value pair in a Map
          fruits.forEach (function(value, key) {
            text += key + ' = ' + value;
          })
    The entries() method returns an iterator object with the [key, values] in a Map
        for (const x of fruits.entries()) {
          text += x;
        }

JS functions

  Syntax:
    function functionName(parameters) {
      // code to be executed
    }
  JavaScript Arrow Functions:
  With arrow functions, you don't have to type the function keyword, the return keyword, and the curly brackets.
      const x = (x, y) => x * y;
  this keyword refers to an object.

  The call() method is a predefined JavaScript method.

      const person = {
        fullName: function() {
          return this.firstName + " " + this.lastName;
        }
      }
      const person1 = {
        firstName:"John",
        lastName: "Doe"
      }
      document.getElementById("demo").innerHTML = person.fullName.call(person1); 

  With the apply() method, you can write a method that can be used on different objects and is similar to call() method.
  The difference is:
  The call() method takes arguments separately.
      person.fullName.call(person1, "Oslo", "Norway");
  The apply() method takes arguments as an array.
      person.fullName.apply(person1, ["Oslo", "Norway"]);
  bind() method, an object can borrow a method from another object.
      const person = {
        firstName:"John",
        lastName: "Doe",
        fullName: function() {
          return this.firstName + " " + this.lastName;
        }
      }
      const member = {
        firstName:"Hege",
        lastName: "Nilsen",
      }
        let fullName = person.fullName.bind(member);
  This will display the after 3s.
      setTimeout(person.display, 3000);
  Variables created without a declaration keyword (var, let, or const) are always global, even if they are created inside a function.
      function myFunction() {
        a = 4;
      }


  Variable Lifetime
    Global variables live until the page is discarded, like when you navigate to another page or close the window.
    Local variables have short lives. They are created when the function is invoked, and deleted when the function is finished.
    The self-invoking function only runs once.
        document.getElementById("demo").innerHTML = add();
        function add() {
          let counter = 0;
          function plus() {counter += 2;}
          plus();  
          return counter; 
        }

JS Classes
        Class Syntax:
        class ClassName {
          constructor() { ... }
        }
    To create a class inheritance, use the extends keyword.
    A class created with a class inheritance inherits all the methods from another class
    The "extends" keyword to inherit all methods from another class.
    The "super" method to call the parent's constructor function.
    Getter and setter:
        class Car {
          constructor(brand) {
            this._carname = brand;
          }
          get carname() {
            return this._carname;
          }
          set carname(x) {
            this._carname = x;
          }
        }

        const myCar = new Car("Ford");

        document.getElementById("demo").innerHTML = myCar.carname;
    Static class methods are defined on the class itself.You cannot call a static method on an object, only on an object class.


JS async and Await
    Where callbacks really shine are in asynchronous functions, where one function has to wait for another function.

        function myDisplayer(something) {
          document.getElementById("demo").innerHTML = something;
        }

        function myCalculator(num1, num2, myCallback) {
          let sum = num1 + num2;
          myCallback(sum);
        }

        myCalculator(5, 5, myDisplayer);

    Promises are used in JavaScript to handle asynchronous operations and manage the flow of asynchronous code.


jQuery

    Finding HTML Element by Id
        myElement = $("#id01");
    Finding HTML Elements by Tag Name
        myElements = $("p");
    Finding HTML Elements by Class Name
        myElements = $(".intro");
    Set Text Content
        myElement.text("Hello Sweden!");
    Get Text Content
        myText = $("#02").text();

    JavaScript objects are written with curly braces {}.
