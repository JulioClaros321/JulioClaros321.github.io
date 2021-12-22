const myTitle = document.querySelector("title");
const myHeading = document.querySelector("p");
myHeading.textContent = "Hello world!";

myTitle.textContent = "Julio Claros' Lab_4";
var br = document.createElement("br");

var name = "Julio Claros";
var first_name = name.substring(0, 5)
var last_name = name.substring(5, 11)
var count = name.length - 1
var counter = 3

var total = first_name.length + last_name.length

const myHeader = document.querySelector(".header");
myHeader.textContent = "Julio Claros' Lab 4 " + total;


var paragraph = document.createElement("p");
var text = document.createTextNode("My name has " +count +" characters");
paragraph.appendChild(text);
paragraph.classList.add("para1");

var sec_paragraph = document.createElement("p");
var sec_text = document.createTextNode("The third character in my name is " +name[2].toUpperCase());
var third_text = document.createTextNode("ros")
sec_paragraph.appendChild(sec_text);
sec_paragraph.classList.add("para2");
sec_paragraph.appendChild(br)
sec_paragraph.appendChild(third_text)

var content = document.querySelector(".content"); 

content.appendChild(paragraph);
content.appendChild(sec_paragraph);

