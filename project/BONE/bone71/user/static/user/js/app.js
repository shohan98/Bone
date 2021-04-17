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


    $('.customNextBtn').click(function() {
        $(this).closest('.slider_nav_arrow').siblings('.owl-carousel').children('.owl-nav').find('.owl-next').click()
    });
    $('.customPrevBtn').click(function() {
        $(this).closest('.slider_nav_arrow').siblings('.owl-carousel').children('.owl-nav').find('.owl-prev').click()
    });

    // video and ad render to another page 
    $('.movie_poster').click(function() {
        id = $(this).attr('video-id');
        mainVideoUrl = $(this).attr('main-video-url');
        // window.location.href = 'video' + '/' + id;
        window.location.href = 'video';
    });
    // video and ad render to another page 


    document.getElementById('video').addEventListener('ended', function(e) {
        var src = $('.main-video-section iframe').attr('src')
        $('.ad-video-section').slideToggle();
        $('.main-video-section').slideToggle();
        $('.main-video-section iframe').attr('src', src + '?autoplay=1')
    });
});