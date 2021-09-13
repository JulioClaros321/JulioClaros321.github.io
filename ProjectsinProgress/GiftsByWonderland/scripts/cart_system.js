if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready)
}
else {
    ready()
}


function ready() {

    addItemsToCart() 
    var removeCartItemsButtons = document.getElementsByClassName('btn-danger')

    for (var i=0; i < removeCartItemsButtons.length; i++) {
        var button = removeCartItemsButtons[i]
        button.addEventListener("click", removeCartItem) 
        }

    var quantityInputs = document.getElementsByClassName("cart-quantity-input")
    for (var i = 0; i < quantityInputs.length; i++) { 
        var input = quantityInputs[i]
        input.addEventListener("change", quantityChanged)

    }

    function quantityChanged(event) {
        var input = event.target
        if (isNaN(input.value) || input.value <= 0) {
            input.value = 1
        }
        updateCartTotal() 
    }

    function removeCartItem(event) {
        var buttonClicked = event.target 
        buttonClicked.parentElement.parentElement.remove()
        updateCartTotal()
    }


    function updateCartTotal() {
        var cartItemContainer = document.getElementsByClassName("cart-items")[0]
        var cartRows = cartItemContainer.getElementsByClassName("cart-row")
        var total = 0

        for (var i=0; i < cartRows.length; i++) {
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName("cart-price")[0]
            var quantityElement = cartRow.getElementsByClassName("cart-quantity-input")[0]

            var price = parseFloat(priceElement.innerHTML.replace("$", " "))
            var quantity = quantityElement.value
            total = total + (price * quantity)
            
            }
            total = Math.round(total * 100) / 100
            document.getElementsByClassName("cart-total-price")[0].innerText = "$" + total
        }


    function addItemsToCart() {
        cartList = localStorage.getItem("productsInCart")
        var cartList = JSON.parse(cartList)
        
        var cartItems = document.getElementsByClassName("cart-items")[0]
        console.log(cartItems)

        for(i=0; i< cartList.length; i++) {
            var cartRow = document.createElement("div") 
            cartRow.classList.add("cart-row")
            console.log(cartList[i].item_image)

            var cartRowContents = `
            <div class="cart-item cart-column">
                <img class="cart-item-image" src="${cartList[i].item_image}" width="100" height="100">
                <span class="cart-item-title">${cartList[i].title}</span>
            </div>
            <span class="cart-price cart-column">$${cartList[i].price}</span>
            <div class="cart-quantity cart-column">
                <input class="cart-quantity-input" type="number" value="1">
                <button class="btn btn-danger" type="button">REMOVE</button>
            </div>`

            cartRow.innerHTML = cartRowContents
            cartItems.append(cartRow)
            updateCartTotal()
        }

    }
}