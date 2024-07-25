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

    var addToCartButtons = document.getElementsByClassName("add_to_cart")
    for (var i = 0; i < addToCartButtons.length; i++) {
        var button = addToCartButtons[i]
        button.addEventListener("click", addToCartClicked)
    
    }

    function addToCartClicked(event) {
        var button = event.target 
        var shopItem = button.parentElement
        
        var itemTitle = shopItem.title
        var item_graphic = "/images/" +(itemTitle.split(" ").join("")) +".jpeg"
        var price = (shopItem.getElementsByClassName("price")[0].innerHTML).replace("$", "")
        var items_included = shopItem.getElementsByClassName("description")[0].innerHTML

        addItemToCart(itemTitle, items_included, price, item_graphic)
    }

    function addItemToCart(itemTitle, items_included, price, item_graphic) {

        
        let cartItems = sessionStorage.getItem("productsInCart");
        cartItems = JSON.parse(cartItems);



        
        var item = {

            title: itemTitle,
            description: [items_included],
            price: price,
            item_image: item_graphic,
            quantity: 1
        }
        
        console.log(item)
        var list_of_items = []
        
        
        if (cartItems == null) {
            list_of_items.push(item)
        }

        else {
            list_of_items = cartItems
            list_of_items.push(item)
            }            
        
        
        
        

        sessionStorage.clear()
        sessionStorage.setItem("productsInCart", JSON.stringify(list_of_items))

        let updateNotification = sessionStorage.getItem("productsInCart");
        updateNotification = JSON.parse(updateNotification)

        document.getElementById("number").innerHTML = updateNotification.length
        
        
        

    }
}