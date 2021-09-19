if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready)
}
else {
    ready()
}


function ready() {

    addItemsToCart()
    document.getElementsByClassName("btn_purchase")[0].addEventListener("click", purchaseMade)
    

    
    var removeCartItemsButtons = document.getElementsByClassName('remove')
    for (var i=0; i < removeCartItemsButtons.length; i++) {
        var button = removeCartItemsButtons[i]
        button.addEventListener("click", removeCartItem) 
        }

    var quantityInputs = document.getElementsByClassName("cart_quantity_input")
    for (var i = 0; i < quantityInputs.length; i++) { 
        var input = quantityInputs[i]
        input.addEventListener("change", quantityChanged)

    }

    var stripeHandler = StripeCheckout.configure({
        key: stripePublicKey,
        local: "en",
        token: function(token) {
            var ServerProcessingItems = []
            var storage = JSON.parse(sessionStorage.getItem("productsInCart"))
            
            for (i=0; i < storage.length; i++) {
                var name = storage[i].name
                var quantity = storage[i].quantity

                ServerProcessingItems.push({
                    title: name,
                    quantity: quantity
                })

            }
            fetch("/purchase", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({
                    stripeTokenId: token.id,
                    items: ServerProcessingItems
                })
            }).then(function(res) {
                return res.json()
            }).then(function(data) {
                alert(data.message)
                var shopping_cart = document.getElementsByClassName("cart_items")[0]
                while (shopping_cart.hasChildNodes()) {
                    shopping_cart.removeChild(shopping_cart.firstChild)
                }
                sessionStorage.removeItem("productsInCart")
                updateCartTotal()
            }).catch(function(error) {
                console.log(error)
            })
        }
    })

    

    function purchaseMade() {
        var price = parseFloat((document.getElementsByClassName("cart_total_price")[0]).innerText.replace("$", "")) * 100
        stripeHandler.open({
            amount: price
        })
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
        var cartItemContainer = document.getElementsByClassName("cart_items")[0]
        var cartRows = cartItemContainer.getElementsByClassName("cart_row")
        var total = 0
    

        for (var i=0; i < cartRows.length; i++) {
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName("cart_price")[0]
            var quantityElement = cartRow.getElementsByClassName("cart_quantity_input")[0]

            var price = parseFloat(priceElement.innerHTML.replace("$", " "))
            var quantity = quantityElement.value
            total = total + (price * quantity)
            
            }

            total = Math.round(total * 100) / 100
            document.getElementsByClassName("cart_total_price")[0].innerText = "$" + total
        }



    function addItemsToCart() {
        cartList = sessionStorage.getItem("productsInCart")
        var cartList = JSON.parse(cartList)
        
        var cartItems = document.getElementsByClassName("cart_items")[0]
        hehe = cartItems.getElementsByClassName("cart_quantity_input")

        for(i=0; i< cartList.length; i++) {
            var cartRow = document.createElement("div") 
            cartRow.classList.add("cart_row")

            var cartRowContents = `
            <div class="cart_item column">
                <img class="cart_item_image" src="${cartList[i].item_image}" width="100" height="100">
                <span class="cart_item_title innertext">${cartList[i].title}</span>
            </div>
            <span class="cart_description column desc_innertext">${cartList[i].description}</span>
            <span class="cart_price column innertext">$${cartList[i].price}</span>
            <div class="cart_quantity column">
                <input class="cart_quantity_input" type="number" value="1">
                <button class="btn remove" type="button">REMOVE</button>
            </div>`

            cartRow.innerHTML = cartRowContents
            cartItems.append(cartRow)
            


        }

        updateCartTotal()
    }
}