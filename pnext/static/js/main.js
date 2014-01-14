// Google Analytics
// var _gaq = _gaq || [];
// _gaq.push(['_setAccount', 'UA-2230191-1']);
// _gaq.push(['_trackPageview']);
// 
// (function() {
//   var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
//   ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
//   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
// })();


// jQuery Main events
// Not using loops for optmization
$(window).load(function(){
    $("#main").onepage_scroll({
        sectionContainer: "section", // sectionContainer accepts any kind of selector in case you don't want to use section
        easing: "ease", // Easing options accepts the CSS3 easing animation such "ease", "linear", "ease-in", "ease-out", "ease-in-out", or even cubic bezier value such as "cubic-bezier(0.175, 0.885, 0.420, 1.310)"
        animationTime: 1000, // AnimationTime let you define how long each section takes to animate
        pagination: true, // You can either show or hide the pagination. Toggle true for show, false for hide.
        updateURL: false, // Toggle this true if you want the URL to be updated automatically when the user scroll to each page.
        beforeMove: function(index) {}, // This option accepts a callback function. The function will be called before the page moves.
        afterMove: function(index) {}, // This option accepts a callback function. The function will be called after the page moves.
        loop: false, // You can have the page loop back to the top/bottom when the user navigates at up/down on the first/last page.
        responsiveFallback: 768 // You can fallback to normal page scroll by defining the width of the browser in which you want the responsive fallback to be triggered. For example, set this to 600 and whenever the browser's width is less than 600, the fallback will kick in.
      });   
});

// Uses jQuery throttle pluggin to optimize scroll
$(window).scroll($.throttle(50, executeAtScroll)); 
function executeAtScroll() {
	checkSrollForPNTag();
	
	// Usage: checkScrollFixedForNav(element, element ghost, min px, max px);
	// Last's max px must be set to 0.
	checkScrollFixedForNav($nav0, $nav0_ghost, $nav0_y, $nav1_y);
	checkScrollFixedForNav($nav1, $nav1_ghost, $nav1_y, $nav2_y);
	checkScrollFixedForNav($nav2, $nav2_ghost, $nav2_y, $maxHeight);
}

function checkSrollForPNTag(){
    if( $(window).scrollTop() > $pn_tag_display_height ){
        $pn_tag_el.slideDown('fast');
    }else{
        $pn_tag_el.slideUp('fast');
    }
}


