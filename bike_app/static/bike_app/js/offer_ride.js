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
                    $('.form-group-submit').css({'top' : '+=40px'});
                    console.log('Height is increased and padding is added');
                }
                else{
                    $('.date-time-submit-container').css({'height' : '-=100px'});
                    $('.form-group-submit').css({'top' : '-=40px'});
                    console.log('Height and padding decreased');
                }
             });
        }
      }


      datetimepicker.init();
      add_arrival_datetime.init();
      increase_height_on_button_click.init();

});

