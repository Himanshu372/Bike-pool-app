$(function(){

    export var show_rides = {
        init: function(response){
            if typeof response === 'string' {
                var div = document.createElement("div");
                div.className = "container";
                document.body.appendChild(div);
            }
        }
    }
    show_rides.init();
})