$(function() {

        var datetimepicker = {
            init: function(){
                $("#datetimepicker1").datetimepicker();
            }
        }

        var increase_height_on_button_click = {
            init: function(){
                $('#stopover-button').click(function(){
                $('.departure-arrival-stopover-container').css({'height' : '+=25px'});
                console.log('Height is increased');
                });
            }
        }

        var add_arrival_datetime = {
            init: function(){
                 $('#checkbox').change(function(){
                    if(this.checked){
                        $('.date-time-submit-container').css({'height' : '+=100px'});
                        console.log('Height is increased and padding is added');
                        addDateandTime('date-and-time');
                    }
                    else{
                        var node = document.getElementById("arrival-date-time-block");
                        while (node.firstChild) {
                            console.log(node.lastChild);
                            node.removeChild(node.lastChild);
                        }
                        node.parentNode.removeChild(node);
                        $('.date-time-submit-container').css({'height' : '-=100px'});
                        console.log('Height and padding decreased');
                    }
                 });
            }
        }

        $("#stopover-button").on("click", function() {
            var counter = 1;
            var newdiv = document.createElement('div');
            newdiv.innerHTML = "<input type='text' name='stopover_" + counter + "' placeholder='Stopver location' class='form-control stopover'>";
            document.getElementById("dynamicInput").appendChild(newdiv);
            console.log('Function executed');
        });


        function addDateandTime(divName){
            var addHTMLstring = '<div class="arrival-date-time-block" id="arrival-date-time-block" style="margin-top: 30px"><label style="text-align: left; display: block; padding-left: 15px" id="arrival-date-time-label">Arrival Date & Time</label><div class="col-sm-6 clearfix"><div class="form-group"><div class="input-group date" id="datetimepicker2"><input type="text" class="form-control" name="datetimepicker-arrival"/><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div></div></div>';
            document.getElementById(divName).insertAdjacentHTML('beforeend', addHTMLstring);
            console.log('Arrival date & time panel added');
        }


        datetimepicker.init();
        add_arrival_datetime.init();
        increase_height_on_button_click.init();
});

