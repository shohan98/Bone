(function($) {
    "use strict"; // Start of use strict
    let csrf_token = $("#csrf-token").val();
    // Toggle the side navigation
    $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
        $("body").toggleClass("sidebar-toggled");
        $(".sidebar").toggleClass("toggled");
        if ($(".sidebar").hasClass("toggled")) {
            $('.sidebar .collapse').collapse('hide');
        };
    });

    // Close any open menu accordions when window is resized below 768px
    $(window).resize(function() {
        if ($(window).width() < 768) {
            $('.sidebar .collapse').collapse('hide');
        };

        // Toggle the side navigation when window is resized below 480px
        if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
            $("body").addClass("sidebar-toggled");
            $(".sidebar").addClass("toggled");
            $('.sidebar .collapse').collapse('hide');
        };
    });

    // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
    $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
        if ($(window).width() > 768) {
            var e0 = e.originalEvent,
                delta = e0.wheelDelta || -e0.detail;
            this.scrollTop += (delta < 0 ? 1 : -1) * 30;
            e.preventDefault();
        }
    });

    // Scroll to top button appear
    $(document).on('scroll', function() {
        var scrollDistance = $(this).scrollTop();
        if (scrollDistance > 100) {
            $('.scroll-to-top').fadeIn();
        } else {
            $('.scroll-to-top').fadeOut();
        }
    });

    // Smooth scrolling using jQuery easing
    $(document).on('click', 'a.scroll-to-top', function(e) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top)
        }, 1000, 'easeInOutExpo');
        e.preventDefault();
    });
    $('.tag-close-icon').click(function() {
        $(this).closest('.tags-span').remove();
    });


    $('.header_search').keyup(function() {
        var searchValue = this.value;
        var url = window.location.href;
        var urlOrigin = window.location.origin;
        console.log(url)
        console.log(searchValue.length)
        var delete_icon = urlOrigin + "/static/boneadmin/img/delete_icon.png";
        var edit = urlOrigin + "/static/boneadmin/img/edit_icon.png";
        $('.video-list tbody').empty();
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
                var tableData = response.video_data;
                console.log(tableData);
                var html;
                $.each(tableData, function(index, data) {
                    console.log(data)
                    html = `<tr id=` + data.id + `>
                    <td class="video_image">
                        <img src=` + data.content_poster + ` alt="">
                    </td>
                    <td class="video_name">
                        <p>` + data.content_name + `
                        </p>
                    </td>
                    <td class="video_cateogry">
                        <p>` + data.category + `</p>
                    </td>
                    <td class="video_cateogry">
                        <p>` + data.content_link + `</p>
                    </td>
                    <td class="video_action">
                        <a href="#" class="edit"><img src=` + edit + ` alt=""></a>
                        <a href="#" class="delete_video_btn" data-toggle="modal" data-target="#delete_video_modal" onclick="deleteselect(this)"><img src=` + delete_icon + ` alt=""></a>
                    </td>
                </tr>`;
                    $('.video-list tbody').append(html)
                });
            },
            error: function(request, status, error) {
                console.log(request, status, error)
            }
        });
    });



})(jQuery); // End of use strict
let csrf_token = $("#csrf-token").val();

function addCategory() {
    var category_name = $('.add-category-input').val();
    if (category_name != '') {
        var html = '<span class="tags-span">' + category_name + '<span class="tag-close-icon"><i class="fas fa-times"></i></span></span>'
        $('.tag-section').append(html);
        $('.add-category-input').val('');
    }
}
let id;

function deleteselect(e) {
    id = parseInt(e.parentElement.parentElement.getAttribute('id'));
    console.log(id)
}

function deleteTr() {
    idDom = $('#' + id)
    var url = window.location.origin;
    console.log(url + '/boneadmin/api/contentdelete')
    $.ajax({
        type: "POST",
        url: url + '/boneadmin/api/contentdelete/',
        contentType: "application/x-www-form-urlencoded",
        data: {
            c_id: id,
            csrfmiddlewaretoken: csrf_token,
        },
        success: function(data, textStatus, xhr) {
            if (xhr.status == 204) {
                idDom.remove();
                $('.delete_video_modal').modal('toggle');
            }


        },
        error: function(request, status, error) {
            console.log(request, status, error)
        }
    });
}