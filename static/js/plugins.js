$(function () {
var $container = $('.masonry').packery();
    $container.imagesLoaded(function () {
        $container.packery({
            itemSelector: '.post-preview',
            isResizable: false,
            gutter: 10
        });
    });

})
