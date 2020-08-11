
$(function(){

        var login = {
            init: function(){
                $(".login-submit-text").click(function(){
                    var csrf_token = "{{ csrf_token }}";
//                    var email = $(".login-email").val();
//                    var password = $(".login-password").val();
                    var data = $("#login-form").serialize();
                    $.ajax({
                        headers: {"X-CSRFToken": csrf_token},
                        type: POST,
                        url: 'login/',
                        async: true,
                        data: data,
                        success: function(response){
//                            if response === true{
//                                window.location.replace("/");
//                                a[href="login.html"]{
//                                    display: none;
//                                }
//                                a[href="signup.html"]{
//                                    display: none;
//                                }
//                            }
                        }

                    })

                });


            }

        };

        login.init();
})