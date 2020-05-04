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
                    pickup: pickup,
                    dropoff: dropoff,
                    datetime: datetimepicker
                },
                success: function(data){
                    console.log('Success');
                }
             })
        });

//            Datepicker function
            $('#datetimepicker1').datetimepicker();
        }
    }

    find_ride.init();
})