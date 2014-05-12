$(document).ready(function() {  

    // It's prettier when a section is full height
    // (if its content's height allows)
    window_height = $(window).height();
   
    $('section').each(function() {
        section = $(this);
        content = section.children('.content');
        content_height = content.outerHeight();

        if (content_height < window_height) {
            section.height(window_height);
        }
    });
}); 
