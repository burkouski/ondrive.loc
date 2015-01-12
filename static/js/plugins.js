$(function () {
var $container = $('.masonry').masonry();
    $container.imagesLoaded(function () {
        $container.masonry({
            itemSelector: '.post-preview',
            isResizable: true
        });
    });

})
