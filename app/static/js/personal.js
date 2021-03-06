
//head pic upload
$(document).ready(function(){
    $('#upload_head_pic_form').submit(function(e){
        e.preventDefault();
        if ($("#headpic_input").get(0).files[0]) {
            var image_data = new FormData($("#upload_head_pic_form")[0]);
            $.ajax({
                type: 'post',
                url: '/avatar',
                data: image_data,
                processData: false,
                contentType: false,
                success: function(resp){
                    document.getElementById("upload_head_pic_form").style.display="none"
                    $('#current_avatar').attr('src', resp)
                    $('#change_pic').attr('src', resp)
                    var temp_win = document.getElementById('background')
                    temp_win.style.display = 'none'
                }
            });
        }else{
            alert("please upload your head picture")
        }
    });
});


//upload window
var btn = document.getElementById('open_button');
var div = document.getElementById('background');
var form=document.getElementById('upload_head_pic_form')
var close = document.getElementById('close-button');
 
btn.onclick = function show() {
	div.style.display = "block";
    form.style.display = "block";
    
}
 
close.onclick = function close() {
	div.style.display = "none";
    form.style.display = "none";
}
 
window.onclick = function close(e) {
	if (e.target == div) {
		div.style.display = "none";
        form.style.display = "none";
	}
}
