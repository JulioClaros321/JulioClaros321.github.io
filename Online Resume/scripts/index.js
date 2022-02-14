if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready)
}
else {
    ready()
}

function ready() {

    function myFunction(tags, number) {
        var div = tags[number]
        div.scrollIntoView({behavior: "smooth"})
    }


    var tags = document.getElementsByTagName("h1")

    $(".data_science").click(function(){
        myFunction(tags, 0);
    });

    $(".javascript").click(function(){
        myFunction(tags, 1);
    });

    $(".unity").click(function(){
        myFunction(tags, 2);
    });


}