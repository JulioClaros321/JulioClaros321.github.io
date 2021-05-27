$('#text-1').show();
$('#text-2').show();
$('#text-3').show();
$('#text-4').show();


$('#btn-1').click(function(){
    $('.text').hide();
	$('#text-1').show();
    $('.store_item_details').show();
    $('.store_item_description').show();
    $('.second_store_item_details').hide();
    $('.second_store_item_description').hide();
});

$('#btn-2').click(function(){
    $('.text').hide();
	$('#text-2').show();
    $('.second_store_item_details').show();
    $('.second_store_item_description').show();
    $('.store_item_details').fade();
    $('.store_item_description').fade();
});

$(".gamestop_button").click(function() {
    $('.starbucks_button').addClass("disabled");
    $('.starbucks_button').removeClass("select");

    $('.gamestop_button').addClass("select");
    $('.gamestop_button').removeClass("disabled")

});

$(".starbucks_button").click(function() {
    $('.gamestop_button').addClass("disabled");
    $('.gamestop_button').removeClass("select");
    
    $('.starbucks_button').addClass("select");
    $('.starbucks_button').removeClass("disabled")

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









$(".second_gamestop_button").click(function() {
    $('.second_starbucks_button').addClass("disabled");
    $('.second_starbucks_button').removeClass("select");

    $('.second_gamestop_button').addClass("select");
    $('.second_gamestop_button').removeClass("disabled")

});

$(".second_starbucks_button").click(function() {
    $('.second_gamestop_button').addClass("disabled");
    $('.second_gamestop_button').removeClass("select");
    
    $('.second_starbucks_button').addClass("select");
    $('.second_starbucks_button').removeClass("disabled")

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
    $('.second_gummy_button').removeClass("disabled")

});
