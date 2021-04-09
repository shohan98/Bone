$(document).ready(function() {


    $('#example2').dataTable({
        "paging": false,
        // "ordering": false,
        "info": false
    });
    $('#example3').dataTable({
        "paging": false,
        // "ordering": false,
        "info": false
    });

    $(".owl-carousel").owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dot: true,
        items: 4,
        // autoplay: true,
        autoplayTimeout: 3000,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            1024: {
                items: 3,
            },
            1440: {
                items: 4,
            },
        },
    });
 

});