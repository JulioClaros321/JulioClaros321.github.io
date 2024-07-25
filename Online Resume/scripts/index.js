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

    var counter = 1;
    setInterval(function(){
        document.getElementById('radio' + counter).checked = true;
        counter++;
        if(counter > 6){
            counter = 1;
        }
    }, 5000);

    var indeed_counter = 1;
    setInterval(function(){
        document.getElementById('indeed_radio' + indeed_counter).checked = true;
        indeed_counter++;
        if(indeed_counter > 4){
            indeed_counter = 1;
        }
    }, 5000);

}