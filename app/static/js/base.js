$(document).ready(function () {
    var current_row=2;
    var count = 0;
   
    $.ajax({
        url: "/ajax/article_count",
        datatype: "json",
        success : function(resp) {
            if(resp.count){
                count = resp.count;
                $('#more').append(resp.count);
            }
            else{
                console.log('Invalid response!!');
            }
        },
        error : function(resp) {
            alert('No response!!, Server error');
        }
    });

});