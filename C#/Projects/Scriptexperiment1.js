// JavaScript source code

$(document).ready(function () {
    var linenum = 0
    $(this).click(function() {
        $("p").css("background-color", "red");
        $("p").eq(linenum).css("color","yellow");
        linenum++;
        if (linenum>3){$("p").delay(500).hide();}
    
    });

        });