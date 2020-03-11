const myTitle = document.querySelector("title");
myTitle.textContent = "lab_5";

const lol = countries[1].name;

const myHeading = document.querySelector(".header");
myHeading.textContent = "Julio's List of Countries";




var content = document.querySelector(".content");
var order_list = document.createElement("ol");
order_list.classList.add("countries");
content.appendChild(order_list);

