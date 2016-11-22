// JavaScript source code

$(document).ready(function () {
    var BGcolor=["#ff0000", "#483D8B", "DeepSkyBlue","DarkTurquoise", "Fuchsia", "Indigo","MediumSpringGreen","MediumAquaMarine"];
    var x = 0;                                  // color array used for menu items 2 and 3
    var y = 0
 
    $(".item").slideUp();
    $("#Menu").mouseenter(function () {         //slide menu down when mouse hover
        $(".item").slideDown();
        $(".item").eq(1).click(function () {    //change text color of p elements on mouseclick menu item 2
            $("p").css("color", BGcolor[x]);
            x++;
            if (y > 2) { ($(".item").eq(1).unbind(click)),(y=0),(x=0) };
            if (x >= 7) { (x = 0), (y++) }});
        $(".item").eq(2).click(function ()  {               //change background color on click menu item 3
            $("body").css("background-color", BGcolor[x]);
            x++;
            if (y > 2) { $(".item").eq(2).unbind(click) };  //limit color changes to 2 full cycles
            if (x >= 7) { (x = 0), (y++) }
        });
        $(".item").eq(0).click(function () {                //hide whole page on mouseclick menu item 1
            $("main, header, footer").hide(500);
        })
        $(".item").eq(0).click(function () {
            $("main, header, footer").hide(500);
        });
            $(".items").mouseleave(function () {            //hide menu on mouse pointer exit menu area.
                $(".item").slideUp(500);
            })



     
           


          


                       
        }) 
    })

