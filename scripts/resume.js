let data_science_button = document.getElementsByClassName("data_science")
let javascript_button = document.getElementsByClassName("javascript")
let unity_button = document.getElementsByClassName("unity")

data_science_button[0].addEventListener("click", data_scroll)
javascript_button[0].addEventListener("click", javascript_scroll)
unity_button[0].addEventListener("click", unity_scroll)

function data_scroll() {
    document.getElementsByClassName("data_science_projects")[0].scrollIntoView();
}

function javascript_scroll() {
    document.getElementsByClassName("javascript_projects")[0].scrollIntoView();
}

function unity_scroll() {
    document.getElementsByClassName("unity_projects")[0].scrollIntoView();
}