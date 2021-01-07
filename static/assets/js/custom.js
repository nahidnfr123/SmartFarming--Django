function loadImagesOnScroll() {
    $.each($('img'), function () {
        if ($(this).attr('data-src') && $(this).offset().top < ($(window).scrollTop() + $(window).height() + 200)) {
            var source = $(this).data('src');
            $(this).attr('src', source);
            $(this).removeAttr('data-src');
        }
    });
}
loadImagesOnScroll();

// toggle profile icon ...
function ProfileMenuToggle() {
    var element = document.getElementById("Profile_Options").classList;
    var element2 = document.getElementById("Profile").classList;
    if (element.contains('show')) {
        element.remove('show');
        element2.remove('clicked');
        $('.MsgCountfront').show();
    } else {
        element.add('show');
        element2.add('clicked');
        $('.MsgCountfront').hide();
    }
}

$(document).ready(function () {
    // Responsive navigation bar menu ....
    $('.navTrigger').click(function () {
        $(this).toggleClass('active');
        $("#NavMenu").toggleClass("show_list");
        //$("#NavMenu").fadeIn();
        $(".navTrigger").toggleClass("light_up");
    });
});


// Sticky Navigation Bar.... //
window.onscroll = function () {
    StickyNavBar();
    loadImagesOnScroll();
};

let navbar = document.getElementById("Header");
let sticky = navbar.offsetTop;

function StickyNavBar() {

    if ($(window).width() < 600) {
        if (window.pageYOffset > 80) {
            navbar.classList.add("sticky");
        } else {
            navbar.classList.remove("sticky");
        }
    } else {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky");
        } else {
            navbar.classList.remove("sticky");
        }
    }

}
//  End   //