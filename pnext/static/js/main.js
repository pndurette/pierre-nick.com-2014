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
$(window).load(function(){
    // OnePage Scroll, tweaked
    // https://github.com/peachananr/onepage-scroll
    // https://github.com/pndurette/onepage-scroll
    $("#main").onepage_scroll({
        sectionContainer: "section",
        easing: "cubic-bezier(0.190, 1.000, 0.220, 1.000)", // http://matthewlein.com/ceaser/ 
        animationTime: 750,
        pagination: true, 
        updateURL: false,
        beforeMove: function(index) {},
        afterMove: function(index) {},
        loop: false,
        responsiveFallback: 970 
      });   
});
