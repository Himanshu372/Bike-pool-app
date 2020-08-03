import { show_rides } from './show_rides.js';

$(function(){

    var find_ride = {
        init: function(){
            $("#submit-button").click(function() {

            var csrf_token = '{{ csrf_token }}';
            var pickup = $(".pickup-textbox").val();
            var dropoff = $(".dropoff-textbox").val();
            var datetimepicker = $("#datetimepicker").val();

            $.ajax({
                headers: { "X-CSRFToken": csrf_token },
                type: "POST",
                url: "find_ride/",
                async: true,
                data: {
                    format: "html",
                    pickup: pickup,
                    dropoff: dropoff,
                    datetime: datetimepicker
                },
                dataType: "json",
                success: function(response){
                    $(".form-container").hide();
                    var div = document.createElement("div");
                    div.id = "rides-container";
                    document.body.appendChild(div);
                    addRides(response);
                }
             })
        });

//            Datepicker function
            $('#datetimepicker1').datetimepicker();

            function addRides(rides){
                var total_rides = new Map(Object.entries(rides)).size;
                for (var i = 0; i < total_rides; i++) {
                    var ride_div = document.createElement("div");
                    var ride_html = "<h3 class='ride-fare'>Fare: " + rides[i].fare +
                     "</h3><h3 class='ride-date'>Time: " + rides[i].depart_time +
                     "</h3><h3 class='user-info'>Name: " + rides[i].user_id + "</h3></div>";
                    ride_div.className = "ride-container";
                    ride_div.innerHTML = ride_html;
                    var ride_container = document.getElementById('rides-container').appendChild(ride_div);
                }
            };
        }
    }

    find_ride.init();
})