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
    $('#more_btn').click(function(){
        $.ajax({
            url : '/ajax/article_more',
            dataTYpe : 'json',
            data : {
                current_row : current_row,
                count : count
            },
            success : function(resp){
                current_row += 2;
                more_data = resp.data;
                for(var i in more_data){
                    article = more_data[i];
                    string = "<div class='well' id='article_" + article.id + "'><h1><a href='article/detail/" + article.id + "'>" + article.title + "</a></h1><h3>" + article.author + "</h3><h6>" + article.date_created + "</h6><p>" + article.content + "</p></div>";
                    $("#more_data").append(string);
                }
            },
            error : function(resp){
                console.log('Invalid response!, Server error!');
            }
        });
    });
});


