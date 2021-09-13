if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready)
}
else {
    ready()
}



function ready() {



    $('#text-1').show();
    $('#text-2').show();
    $('#text-3').show();
    $('#text-4').show();
    $("#btn-1").addClass("select");
    $("#second_display").detach().appendTo(".store_item_container");
    $("#third_display").detach().appendTo(".store_item_container");
    $("#fourth_display").detach().appendTo(".store_item_container");

    $("#first_display").show();
    $("#second_display").hide();
    $("#third_display").hide();
    $("#fourth_display").hide();



    $('#btn-1').click(function(){
        $("#btn-1").addClass("select");
        $('#btn-1').removeClass("top_disabled");


        $('#btn-2').addClass("top_disabled");
        $('#btn-3').addClass("top_disabled");
        $('#btn-4').addClass("top_disabled");

        $('#btn-2').removeClass("select");
        $('#btn-3').removeClass("select");
        $('#btn-4').removeClass("select");

        $("#first_display").show();
        $("#second_display").hide();
        $("#third_display").hide();
        $("#fourth_display").hide();

        

    });

    $('#btn-2').click(function(){
        $("#btn-2").addClass("select");
        $('#btn-2').removeClass("top_disabled");


        $('#btn-1').addClass("top_disabled");
        $('#btn-3').addClass("top_disabled");
        $('#btn-4').addClass("top_disabled");


        $('#btn-3').removeClass("select");
        $('#btn-4').removeClass("select");
        $('#btn-1').removeClass("select");

        $("#first_display").hide();
        $("#second_display").show();
        $("#third_display").hide();
        $("#fourth_display").hide();

    });

    $('#btn-3').click(function(){
        $("#btn-3").addClass("select");
        $('#btn-3').removeClass("top_disabled");


        $('#btn-4').addClass("top_disabled");
        $('#btn-1').addClass("top_disabled");
        $('#btn-2').addClass("top_disabled");


        $('#btn-4').removeClass("select");
        $('#btn-1').removeClass("select");
        $('#btn-2').removeClass("select");

        $("#first_display").hide();
        $("#second_display").hide();
        $("#third_display").show();
        $("#fourth_display").hide();
    });

    $('#btn-4').click(function(){
        $("#btn-4").addClass("select");
        $('#btn-4').removeClass("top_disabled");


        $('#btn-1').addClass("top_disabled");
        $('#btn-2').addClass("top_disabled");
        $('#btn-3').addClass("top_disabled");


        $('#btn-1').removeClass("select");
        $('#btn-2').removeClass("select");
        $('#btn-3').removeClass("select");



        $("#first_display").hide();
        $("#second_display").hide();
        $("#third_display").hide();
        $("#fourth_display").show();
    });


    /*For Him Buttons Functionality */

    $(".corona_button").click(function() {
        $(".corona_button").addClass("select");
        $(".corona_button").removeClass("disabled");

        $(".heineken_button").addClass("disabled");
        $(".heineken_button").removeClass("select");
        $(".monster_button").addClass("disabled");
        $(".monster_button").removeClass("select");
        $(".redbull_button").addClass("disabled");
        $(".redbull_button").removeClass("select");


    });


    $(".heineken_button").click(function() {
        $(".heineken_button").addClass("select");
        $(".heineken_button").removeClass("disabled");

        $(".corona_button").addClass("disabled");
        $(".corona_button").removeClass("select");
        $(".monster_button").addClass("disabled");
        $(".monster_button").removeClass("select");
        $(".redbull_button").addClass("disabled");
        $(".redbull_button").removeClass("select");


    });

    $(".monster_button").click(function() {
        $(".monster_button").addClass("select");
        $(".monster_button").removeClass("disabled");

        $(".corona_button").addClass("disabled");
        $(".corona_button").removeClass("select");
        $(".heineken_button").addClass("disabled");
        $(".heineken_button").removeClass("select");
        $(".redbull_button").addClass("disabled");
        $(".redbull_button").removeClass("select");


    });


    $(".redbull_button").click(function() {
        $(".redbull_button").addClass("select");
        $(".redbull_button").removeClass("disabled");

        $(".corona_button").addClass("disabled");
        $(".corona_button").removeClass("select");
        $(".heineken_button").addClass("disabled");
        $(".heineken_button").removeClass("select");
        $(".monster_button").addClass("disabled");
        $(".monster_button").removeClass("select");


    });

    $(".gamestop_button").click(function() {
        $('.starbucks_button').addClass("disabled");
        $('.starbucks_button').removeClass("select");
        $('.steam_button').addClass("disabled");
        $('.steam_button').removeClass("select");
        $('.xbox_button').addClass("disabled");
        $('.xbox_button').removeClass("select");
        

        $('.gamestop_button').addClass("select");
        $('.gamestop_button').removeClass("disabled")

    });

    $(".starbucks_button").click(function() {
        $('.gamestop_button').addClass("disabled");
        $('.gamestop_button').removeClass("select");
        $('.steam_button').addClass("disabled");
        $('.steam_button').removeClass("select");
        $('.xbox_button').addClass("disabled");
        $('.xbox_button').removeClass("select");
        

        $('.starbucks_button').addClass("select");
        $('.starbucks_button').removeClass("disabled")

    });

    $(".steam_button").click(function() {
        $('.starbucks_button').addClass("disabled");
        $('.starbucks_button').removeClass("select");
        $('.gamestop_button').addClass("disabled");
        $('.gamestop_button').removeClass("select");
        $('.xbox_button').addClass("disabled");
        $('.xbox_button').removeClass("select");
        

        $('.steam_button').addClass("select");
        $('.steam_button').removeClass("disabled")

    });

    $(".xbox_button").click(function() {
        $('.starbucks_button').addClass("disabled");
        $('.starbucks_button').removeClass("select");
        $('.gamestop_button').addClass("disabled");
        $('.gamestop_button').removeClass("select");
        $('.steam_button').addClass("disabled");
        $('.steam_button').removeClass("select");
        

        $('.xbox_button').addClass("select");
        $('.xbox_button').removeClass("disabled")

    });

    $(".chocolate_button").click(function() {
        $('.gummy_button').addClass("disabled");
        $('.gummy_button').removeClass("select");

        $('.chocolate_button').addClass("select");
        $('.chocolate_button').removeClass("disabled")

    });

    $(".gummy_button").click(function() {
        $('.chocolate_button').addClass("disabled");
        $('.chocolate_button').removeClass("select");

        $('.gummy_button').addClass("select");
        $('.gummy_button').removeClass("disabled")

    });




    /*for her section buttons */

    $(".second_corona_button").click(function() {
        $('.barefoot_button').addClass("disabled");
        $('.barefoot_button').removeClass("select");
        $('.whiteclaw_button').addClass("disabled");
        $('.whiteclaw_button').removeClass("select");
        $('.snapple_button').addClass("disabled");
        $('.snapple_button').removeClass("select");


        $('.second_corona_button').addClass("select");
        $('.second_corona_button').removeClass("disabled");

    });

    $(".barefoot_button").click(function() {
        $('.second_corona_button').addClass("disabled");
        $('.second_corona_button').removeClass("select");
        $('.whiteclaw_button').addClass("disabled");
        $('.whiteclaw_button').removeClass("select");
        $('.snapple_button').addClass("disabled");
        $('.snapple_button').removeClass("select");


        $('.barefoot_button').addClass("select");
        $('.barefoot_button').removeClass("disabled");

    });

    $(".whiteclaw_button").click(function() {
        $('.second_corona_button').addClass("disabled");
        $('.second_corona_button').removeClass("select");
        $('.barefoot_button').addClass("disabled");
        $('.barefoot_button').removeClass("select");
        $('.snapple_button').addClass("disabled");
        $('.snapple_button').removeClass("select");


        $('.whiteclaw_button').addClass("select");
        $('.whiteclaw_button').removeClass("disabled");

    });


    $(".snapple_button").click(function() {
        $('.second_corona_button').addClass("disabled");
        $('.second_corona_button').removeClass("select");
        $('.barefoot_button').addClass("disabled");
        $('.barefoot_button').removeClass("select");
        $('.whiteclaw_button').addClass("disabled");
        $('.whiteclaw_button').removeClass("select");


        $('.snapple_button').addClass("select");
        $('.snapple_button').removeClass("disabled");

    });

    $(".face_button").click(function() {
        $('.body_button').addClass("disabled");
        $('.body_button').removeClass("select");
        $('.hair_button').addClass("disabled");
        $('.hair_button').removeClass("select");


        $('.face_button').addClass("select");
        $('.face_button').removeClass("disabled");

    });

    $(".hair_button").click(function() {
        $('.body_button').addClass("disabled");
        $('.body_button').removeClass("select");
        $('.face_button').addClass("disabled");
        $('.face_button').removeClass("select");


        $('.hair_button').addClass("select");
        $('.hair_button').removeClass("disabled");

    });

    $(".body_button").click(function() {
        $('.face_button').addClass("disabled");
        $('.face_button').removeClass("select");
        $('.hair_button').addClass("disabled");
        $('.hair_button').removeClass("select");


        $('.body_button').addClass("select");
        $('.body_button').removeClass("disabled");

    });



    $(".Bed_Bath_button").click(function() {
        $('.second_starbucks_button').addClass("disabled");
        $('.second_starbucks_button').removeClass("select");
        $('.forever21_button').addClass("disabled");
        $('.forever21_button').removeClass("select");


        $('.Bed_Bath_button').addClass("select");
        $('.Bed_Bath_button').removeClass("disabled");

    });

    $(".second_starbucks_button").click(function() {
        $('.Bed_Bath_button').addClass("disabled");
        $('.Bed_Bath_button').removeClass("select");
        $('.forever21_button').addClass("disabled");
        $('.forever21_button').removeClass("select");

        
        $('.second_starbucks_button').addClass("select");
        $('.second_starbucks_button').removeClass("disabled");

    });

    $(".forever21_button").click(function() {
        $('.Bed_Bath_button').addClass("disabled");
        $('.Bed_Bath_button').removeClass("select");
        $('.second_starbucks_button').addClass("disabled");
        $('.second_starbucks_button').removeClass("select");
        

        $('.forever21_button').addClass("select");
        $('.forever21_button').removeClass("disabled");

    });


    $(".second_chocolate_button").click(function() {
        $('.second_gummy_button').addClass("disabled");
        $('.second_gummy_button').removeClass("select");

        $('.second_chocolate_button').addClass("select");
        $('.second_chocolate_button').removeClass("disabled")

    });

    $(".second_gummy_button").click(function() {
        $('.second_chocolate_button').addClass("disabled");
        $('.second_chocolate_button').removeClass("select");

        $('.second_gummy_button').addClass("select");
        $('.second_gummy_button').removeClass("disabled");

    });





    /* for parent buttons */



    $(".third_gamestop_button").click(function() {
        $('.third_starbucks_button').addClass("disabled");
        $('.third_starbucks_button').removeClass("select");

        $('.third_gamestop_button').addClass("select");
        $('.third_gamestop_button').removeClass("disabled")

    });

    $(".third_starbucks_button").click(function() {
        $('.third_gamestop_button').addClass("disabled");
        $('.third_gamestop_button').removeClass("select");
        
        $('.third_starbucks_button').addClass("select");
        $('.third_starbucks_button').removeClass("disabled")

    });

    $(".third_chocolate_button").click(function() {
        $('.third_gummy_button').addClass("disabled");
        $('.third_gummy_button').removeClass("select");

        $('.third_chocolate_button').addClass("select");
        $('.third_chocolate_button').removeClass("disabled")

    });

    $(".third_gummy_button").click(function() {
        $('.third_chocolate_button').addClass("disabled");
        $('.third_chocolate_button').removeClass("select");

        $('.third_gummy_button').addClass("select");
        $('.third_gummy_button').removeClass("disabled");

    });


    /*festive Box buttons */

    $(".fourth_gamestop_button").click(function() {
        $('.fourth_starbucks_button').addClass("disabled");
        $('.fourth_starbucks_button').removeClass("select");

        $('.fourth_gamestop_button').addClass("select");
        $('.fourth_gamestop_button').removeClass("disabled")

    });

    $(".fourth_starbucks_button").click(function() {
        $('.fourth_gamestop_button').addClass("disabled");
        $('.fourth_gamestop_button').removeClass("select");
        
        $('.fourth_starbucks_button').addClass("select");
        $('.fourth_starbucks_button').removeClass("disabled")

    });

    $(".fourth_chocolate_button").click(function() {
        $('.fourth_gummy_button').addClass("disabled");
        $('.fourth_gummy_button').removeClass("select");

        $('.fourth_chocolate_button').addClass("select");
        $('.fourth_chocolate_button').removeClass("disabled")

    });

    $(".fourth_gummy_button").click(function() {
        $('.fourth_chocolate_button').addClass("disabled");
        $('.fourth_chocolate_button').removeClass("select");

        $('.fourth_gummy_button').addClass("select");
        $('.fourth_gummy_button').removeClass("disabled")

    });

    var addToCartButtons = document.getElementsByClassName("add_to_cart")
    for (var i = 0; i < addToCartButtons.length; i++) {
        var button = addToCartButtons[i]
        button.addEventListener("click", addToCartClicked)
    
    }


    function addToCartClicked(event) {
        var button = event.target
        var shopItem = button.parentElement.parentElement
        var itemTitle = shopItem.title
        const items_included = []
        var container = shopItem.getElementsByClassName("button_container")
        var price = (shopItem.getElementsByClassName("price_tag").item(0).getElementsByClassName("price")[1].innerText).replace("$", "")




        if (itemTitle == "Him Box") {
            var item_graphic = document.createElement("img");
            item_graphic.src = "/ProjectsinProgress/GiftsByWonderland/images/for_him.jpg"
        
        } else if (itemTitle == "Her Box") {
            var item_graphic = document.createElement("img");
            item_graphic.src = "/ProjectsinProgress/GiftsByWonderland/images/for_her.jpg"

        }

        
        for (var i =0; i< container.length - 1; i++) {
            items_included.push(container[i].getElementsByClassName("select").item(0).value)

        }
        /*console.log(itemTitle)
        console.log(items_included)
        console.log(price)
        console.log(item_graphic)*/


        addItemToCart(itemTitle, items_included, price, item_graphic)
    }


    function addItemToCart(itemTitle, items_included, price, item_graphic) {

        
        let cartItems = localStorage.getItem("productsInCart");
        cartItems = JSON.parse(cartItems);



        
        var item = {

            title: itemTitle,
            description: items_included,
            price: price,
            item_image: item_graphic.src
        }
        

        var list_of_items = []
        
        
        if (cartItems == null) {
            list_of_items.push(item)
        }

        else {
            list_of_items = cartItems
            list_of_items.push(item)
            }
            

        localStorage.clear()
        localStorage.setItem("productsInCart", JSON.stringify(list_of_items))

        let transferList = localStorage.getItem("productsInCart");
        transferList = JSON.parse(transferList)
        
        

    }

    /*function transferStoragetoCart(transferList) {
        console.log(transferList, "it made it to the function")
        var cartRow = document.createElement("div")
        cartRow.classList.add("cart-row")
        var cartRowContents = `
        <div class="cart-item cart-column">
            <img class="cart-item-image" src="${item_graphic}" width="100" height="100">
            <span class="cart-item-title">${itemTitle}</span>
        </div>

        <span class="cart-price cart-column">${price}</span>

        <div class="cart-quantity cart-column">
            <input class="cart-quantity-input" type="number" value="1">
            <button class="btn btn-danger" type="button">REMOVE</button>
        </div>`

        cartRow.innerHTML = cartRowContents


    }
    */
}
