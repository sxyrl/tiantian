/*====================django ajax ======*/
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
/*===============================django ajax end===*/



$(function(){
	var error_name = false;
	var error_password = false;


	$('#uname').blur(function() {
		check_user_name();
	});

	$('#upwd').blur(function() {
		check_pwd();
	});


	function check_user_name(){
		var len = $('#uname').val().length;
		if(len==0)
		{
			$('#uname').next().html('用户名不能为空');
			$('#uname').next().show();
			error_name = true;
		}
		else
		{
			$('#uname').next().hide();
			error_name = false;
		}
	}

	function check_pwd(){
		var len = $('#upwd').val().length;
		if(len==0)
		{
			$('#upwd').next().html('请输入密码');
			$('#upwd').next().show();
			error_password = true;
		}
		else
		{
			$('#upwd').next().hide();
			error_password = false;
		}
	}




	$('#input_submit').click(function() {
		check_user_name();
		check_pwd();
		if(error_name == false && error_password == false){
			var uname = $('#uname').val();
			var upwd = $('#upwd').val();
			$.post('/user/login_exist/',{'uname':uname,'upwd':upwd},function (data) {
				if(data==1){
					$('#login_form').submit();
				}else{
					$('.pwd_error').html('帐号或密码错误').show();
				}
			});
		}
	});
})