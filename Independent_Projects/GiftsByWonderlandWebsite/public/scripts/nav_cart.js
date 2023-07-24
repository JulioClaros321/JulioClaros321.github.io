if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready)
}
else {
    ready()
}




function ready() {

    if (sessionStorage.getItem("productsInCart") == null) {
        document.getElementById("number").innerHTML = 0
    }

    else {
        document.getElementById("number").innerHTML = JSON.parse(sessionStorage.getItem("productsInCart")).length
    }

}