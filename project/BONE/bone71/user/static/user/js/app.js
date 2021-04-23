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
        loop: false,
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



    // video and ad render to another page 

    var video = $('#video').length;
    if (video) {
        // document.getElementById('video').removeAttribute('muted');
        // document.getElementById('video').play();
        document.getElementById('video').addEventListener('ended', function(e) {
            var src = $('.main-video-section iframe').attr('src')
            $('.ad-video-section').slideToggle();
            $('.main-video-section').slideToggle();
            $('.main-video-section iframe').attr('src', src + '?autoplay=1')
        });
    }
    $('.signup-form').submit(function() {
        var password = $('#reg-password').val();
        var confirmPass = $('#confirm-password').val();
        if (password.length < 8) {
            $('.password-alert').text('Check password requirments');
            $('.password-alert').show();
            setTimeout(function() {
                $('.password-alert').hide();
            }, 5000);
            return false;
        }
        if (password != confirmPass) {
            $('.password-alert').text("Password didn't matched");
            $('.password-alert').show();
            setTimeout(function() {
                $('.password-alert').hide();
            }, 5000);
            return false;
        }
    });
    $('.selected_close').click(function() {
        $(this).closest('.category_selected_movies').hide();

    });
    showMore();
    var leftHeight = $('.single-video-section').height();
    $('.recommended-videos-section').height(leftHeight);

    let csrf_token = $('#csrf-token').val();
    // show category data 
    $('.movie_category').click(function() {
        var categoryname = $(this).text().toUpperCase();
        var catValue = parseInt($(this).attr('value'));
        $('.category_movie_list').empty();
        $('.selected_category').text(categoryname);
        $.ajax({
            type: "POST",
            url: "/boneuser/api/categorycontent/",
            contentType: "application/x-www-form-urlencoded",
            data: {
                category: catValue,
                csrfmiddlewaretoken: csrf_token,
            },
            success: function(response) {
                var categoryVideoList = response.video;
                $('.category_selected_movies').show();
                var html;
                $.each(categoryVideoList, function(index, data) {
                    html = `<div class="col-lg-3 col-md-4 col-sm-6 col-12 c_slider pl-0 mb-4">
                    <div class="owl-item">
                        <div class="item movie_poster" video-id=` + data.id + ` onclick="playMovie(this)">
                            <img src=` + data.poster + ` alt="" class="item-img">
                            <div class="right_icon">
                                <a href="#">
                                    <span class="favourite_movie"><img src="/static/user/image/favourite.png" alt=""></span>
                                </a>
                                <a href="#">
                                    <span class="share_movie"><img src="/static/user/image/share.png" alt=""></span>
                                </a>
                            </div>
                            <a href="javascript:void(0);">
                                <span class="movie_play_icon"><img src="/static/user/image/movie_play.png" alt=""></span>
                            </a>
                        </div>
                    </div>
                </div>`;
                    $('.category_movie_list').append(html)
                });
            },
            error: function(request, status, error) {
                console.log(request, status, error)
            }
        });
    });
    // show category data 


    $('.search-movie-input').keyup(function() {
        var searchValue = this.value;
        if (searchValue.length > 0) {
            $('.search-data').slideToggle()
        } else {
            $('.search-data').slideToggle()
        }
        var url = window.location.origin;
        console.log(searchValue);
        $('.search-data').empty();
        $.ajax({
            type: "POST",
            url: url,
            contentType: "application/x-www-form-urlencoded",
            data: {
                type: "search",
                key: searchValue,
                csrfmiddlewaretoken: csrf_token,
            },
            success: function(response) {
                var searchvideoLlist = response.video_data;
                console.log(searchvideoLlist);
                var html;
                $.each(searchvideoLlist, function(index, data) {
                    console.log(data)
                    html = `<a href="javascript:void(0);" video-id=` + data.id + ` onclick="playMovie(this)"><img src=` + data.poster + ` alt=""><span>` + data.title + `</span></a>`;
                    $('.search-data').append(html)
                });
            },
            error: function(request, status, error) {
                console.log(request, status, error)
            }
        });
    });
});


function showMore() {
    var showChar = 300;
    var ellipsestext = "...";
    var moretext = "more";
    var lesstext = "less";
    $('.video-description p').each(function() {
        var content = $(this).html();

        if (content.length > showChar) {

            var c = content.substr(0, showChar);
            var h = content.substr(showChar - 1, content.length - showChar);

            var html = c + '<span class="moreellipses">' + ellipsestext + '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a></span>';

            $(this).html(html);
        }

    });

    $(".morelink").click(function() {
        if ($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });
}

function playMovie(e) {
    var id = e.getAttribute('video-id');
    var url = window.location.origin;
    window.location.href = url + "/video" + '/' + id;
}