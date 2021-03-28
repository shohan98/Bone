$(document).ready(function() {
    $('.hero-slider').owlCarousel({
        loop: true,
        nav: true,
        dotsContainer: '#carousel-custom-dots',
        items: 1,
    });
    var hero_slider = $('.hero-slider');
    $('.slider_nav .customNextBtn').click(function() {
        hero_slider.trigger('next.owl.carousel', [1000]);
    });
    // Go to the previous item
    $('.slider_nav .customPrevBtn').click(function() {
        // With optional speed parameter
        // Parameters has to be in square bracket '[]'
        hero_slider.trigger('prev.owl.carousel', [1000]);
    });
    $('.owl-dot').click(function() {
        $(".owl-dot").removeClass("active");
        $(this).addClass('active');
        hero_slider.trigger('to.owl.carousel', [$(this).index(), 300]);
    });

    // categories slider 

    $('.category-slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 7,
        responsive: {
            0: {
                items: 1
            },
            424: {
                items: 3
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            },
            1440: {
                items: 6
            }
        }
    });

    // Go to the next item
    $('.slider_nav_category .customNextBtn').click(function() {
        $('#categories_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_category .customPrevBtn').click(function() {
        $('#categories_slider .owl-prev').click();
    });



    // latest video slider 

    $('.latest-video-slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            },
        }
    });

    // Go to the next item
    $('.slider_nav_Latest .customNextBtn').click(function() {
        $('#latest_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_Latest .customPrevBtn').click(function() {
        $('#latest_slider .owl-prev').click();
    });


    // slider_nav_movie 

    $('.movie_slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            },
        }
    });

    // Go to the next item
    $('.slider_nav_movie .customNextBtn').click(function() {
        $('#movie_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_movie .customPrevBtn').click(function() {
        $('#movie_slider .owl-prev').click();
    });


    // top regional

    $('.Top_Regeional_slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            },
        }
    });

    // Go to the next item
    $('.slider_nav_Topr .customNextBtn').click(function() {
        $('#Top_Regeional_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_Topr .customPrevBtn').click(function() {
        $('#Top_Regeional_slider .owl-prev').click();
    });

    // most action

    $('.most_action_slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            },
        }
    });

    // Go to the next item
    $('.slider_nav_m_action .customNextBtn').click(function() {
        $('#most_action_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_m_action .customPrevBtn').click(function() {
        $('#most_action_slider .owl-prev').click();
    });

    // most popular
    $('.most_popular_slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            },
        }
    });

    // Go to the next item
    $('.slider_nav_m_popular .customNextBtn').click(function() {
        $('#most_popular_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_m_popular .customPrevBtn').click(function() {
        $('#most_popular_slider .owl-prev').click();
    });

    // most viewed
    $('.most_viewed_slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            },
        }
    });

    // Go to the next item
    $('.slider_nav_m_viewed .customNextBtn').click(function() {
        $('#most_viewed_slider .owl-next').click();
    });
    // Go to the previous item
    $('.slider_nav_m_viewed .customPrevBtn').click(function() {
        $('#most_viewed_slider .owl-prev').click();
    });


});