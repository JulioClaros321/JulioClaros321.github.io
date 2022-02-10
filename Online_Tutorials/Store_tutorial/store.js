if (document.readyState == "loading") { 
    document.addEventListener("DOMContentLoaded", ready)
}

else { 
    ready() 
}


function ready() {
    var removeCartItemsButtons = document.getElementsByClassName("btn-danger")

    for (var i = 0; i < removeCartItemsButtons.length; i++) {
        var button = removeCartItemsButtons[i]
        button.addEventListener("click", removeCartItem)
            
    }

    var quantityInputs = document.getElementsByClassName("cart-quantity-input")
    for (var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i] 
        input.addEventListener("change", quantityChanged) 
    }

    var addCartButtons = document.getElementsByClassName("shop-item-button")
    for (var i = 0; i < addCartButtons.length; i++) { 
        var button = addCartButtons[i] 
        button.addEventListener("click", addToCartClicked)
    }

    document.getElementsByClassName("btn-purchase")[0].addEventListener("click", purchaseClicked)
}

function purchaseClicked(event) { 
    alert("Thank you for your purchase")
    var cart_items = document.getElementsByClassName("cart-items")[0]
    while (cart_items.hasChildNodes()) {
        cart_items.removeChild(cart_items.firstChild)
    }
    updateCartTotal()
}

function removeCartItem(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateCartTotal()
}

function quantityChanged(event) {
    var input = event.target

    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }

    updateCartTotal()

}
function addToCartClicked(event) { 
    var button = event.target
    var shopitem = button.parentElement.parentElement
    var title = shopitem.getElementsByClassName("shop-item-title")[0].innerText
    var price = shopitem.getElementsByClassName("shop-item-price")[0].innerText
    var imageSrc = shopitem.getElementsByClassName("shop-item-image")[0].src 
    
    addItemToCart(title, price, imageSrc) 

}

function addItemToCart(title, price, imageSrc) {
    var cartRow = document.createElement("div")
    cartRow.classList.add('cart-row')
    var cartItems = document.getElementsByClassName("cart-items")[0]
    var cartItemNames = cartItems.getElementsByClassName("cart-item-title")
    for (var i = 0; i < cartItemNames.length; i++) {
        if (cartItemNames[i].innerText == title) { 
            alert("This item is already added to the cart")
            return
        }
    }
    var cartRowContents = `
        <div class="cart-item cart-column">
            <img class="cart-item-image" src="${imageSrc}" width="100" height="100">
            <span class="cart-item-title">${title}</span>
        </div>
        <span class="cart-price cart-column">${price}</span>
        <div class="cart-quantity cart-column">
                <input class="cart-quantity-input" type="number" value="1">
                <button class="btn btn-danger" type="button">REMOVE</button>
            </div>`
    cartRow.innerHTML = cartRowContents 
    cartItems.append(cartRow)
    cartRow.getElementsByClassName("btn-danger")[0].addEventListener("click", removeCartItem)
    cartRow.getElementsByClassName("cart-quantity-input")[0].addEventListener("change", quantityChanged)
    updateCartTotal()

}

function updateCartTotal() { 
    var cartItemContainer = document.getElementsByClassName("cart-items")[0]
    var cartRows = cartItemContainer.getElementsByClassName("cart-row")
    total = 0
    for (var i = 0; i < cartRows.length; i++) {
        var cartRow = cartRows[i] 
        var priceElement = cartRow.getElementsByClassName("cart-price")[0]

        var quantityElement = cartRow.getElementsByClassName("cart-quantity-input")[0]
        var price = parseFloat(priceElement.innerText.replace("$", ""))
        var quantity = quantityElement.value
        total = (total + (price * quantity))
    }
    total = Math.round(total * 100) / 100
    document.getElementsByClassName("cart-total-price")[0].innerText = "$" + total 

}