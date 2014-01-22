// Tweaking viewport size for device scaling
w = $(window).width();
if (w < 1025 && w > 1000) {
    // iPad
    $('meta[name=viewport]').attr('content','width=device-width, initial-scale=1 minimum-scale=1, maximum-scale=1');
} else if ($(window).width() <= 1000) { 
    // iPhone
    $('meta[name=viewport]').attr('content','width=device-width, initial-scale=0.65, minimum-scale=0.65, maximum-scale=0.65');
}
//alert(w + " / " + $('meta[name=viewport]').attr('content'));
