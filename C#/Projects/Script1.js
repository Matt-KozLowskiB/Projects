// JavaScript source code
$(document).ready(function () {

    $("p").hide();

    $("h4").click(function () {
        $(this).next().slideToggle(300);

        });
});