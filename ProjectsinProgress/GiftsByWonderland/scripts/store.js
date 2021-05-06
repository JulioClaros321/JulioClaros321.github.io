$('#btn-1').click(function(){
    $('.text').hide();
	$('#text-1').show();
    $('#btn-1').toggleClass("clicked"); //<== toggleClass
});

$('#btn-2').click(function(){
    $('.text').hide();
	$('#text-2').show();
    $('#btn-2').toggleClass("clicked");
});