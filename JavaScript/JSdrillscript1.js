// JavaScript source code:  simple web functionality examples:

$(document).ready(function () {
	// Rudimentary color array used for menu items 2 and 3:
    var BGcolor=["#ff0000", "#483D8B", "DeepSkyBlue","DarkTurquoise", "Fuchsia", "Indigo","MediumSpringGreen","MediumAquaMarine"];
    var x = 0;                                  
    var y = 0
	
 //slide menu down when mouse hovers
    $(".item").slideUp();
    $("#Menu").mouseenter(function () {         
        $(".item").slideDown();
		
		 // Function:  Change text color of <p> elements on mouseclick menu item(2):
        $(".item").eq(1).click(function () {   
            $("p").css("color", BGcolor[x]);
            x++;
            if (y > 2) { ($(".item").eq(1).unbind(click)),(y=0),(x=0) };
            if (x >= 7) { (x = 0), (y++) }});
			
		// Simple function tochange background color on click menu item (3)	
        $(".item").eq(2).click(function ()  {               
            $("body").css("background-color", BGcolor[x]);
            x++;
			//Limit color changes to 2 full cycles and unbind function:
            if (y > 2) { $(".item").eq(2).unbind(click) };  
            if (x >= 7) { (x = 0), (y++) }
        });
		//Function to hide whole webpage on mouseclick menu item (1)
        $(".item").eq(0).click(function () {                
            $("main, header, footer").hide(500);
        })
        $(".item").eq(0).click(function () {
            $("main, header, footer").hide(500);
        });
		 //hide menu on mouse pointer exit menu area.
            $(".items").mouseleave(function () {           
                $(".item").slideUp(500);
            })



     
           


          


                       
        }) 
    })

