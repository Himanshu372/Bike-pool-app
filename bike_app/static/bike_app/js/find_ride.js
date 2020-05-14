import { show_rides } from './show_rides.js';

$(function(){

    var find_ride = {
        init: function(){
            $("#submit-button").click(function() {

            var csrf_token = '{{csrf_token}}';
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
                success: function(response){
                    show_rides(response);

                }
             })
        });

//            Datepicker function
            $('#datetimepicker1').datetimepicker();
        }
    }

    find_ride.init();
})