


(function ($) {
    "use strict";
    var mainApp = {
       
        scroll_fun:function()
        {
            //SCROLLING SCRIPTS

            $('.move-me a').bind('click', function (event) { //just pass 'move-me' in div and start scrolling between links
                var $anchor = $(this);
                $('html, body').stop().animate({
                    scrollTop: $($anchor.attr('href')).offset().top
                }, 1200, 'easeInOutExpo');
                event.preventDefault();

                //CLOSING MENU AFTER CLICK
                $('#side-menu').animate({ left: '-250px', top: '-1000px' });
                
            });

        },
        sidemenu_fun:function()
        {
            //SIDE MENU SCRIPTS

            $('.menu-close-icon').click(function (e) {
                e.preventDefault();
                $('#side-menu').animate({ left: '-250px', top: '-1000px' });
               
            });
            $('.menu-open-icon').click(function (e) {
                e.preventDefault();
                $('#side-menu').animate({ left: '0px', top: '0px' });
               
            });

        },
        socialmenu_fun:function()
        {
            //SOCIAL MENU SCRIPTS

            $('.menu-open-social').click(function (e) {
                e.preventDefault();
                $('.social-menu').animate({ right: '0px'});
            });
            $('.close-social').click(function (e) {
                e.preventDefault();
                $('.social-menu').animate({ right: '-340px' });
            });


        }, 
        nicescroll_fun: function () {
            $("html").niceScroll();
        },
        custom_fun:function()
        {


            /*====================================
             WRITE YOUR   SCRIPTS  BELOW
            ======================================*/




        },

    }
   
   
    $(document).ready(function () {
        mainApp.scroll_fun();
        mainApp.sidemenu_fun();
        mainApp.socialmenu_fun();
        mainApp.nicescroll_fun();
        mainApp.custom_fun();

    });
}(jQuery));


