$(function () {

    $(".popup").fancybox({
        maxWidth	: 500,
        maxHeight: 500,
		fitToView: false,
        helpers: {
            overlay: {
                locked: false
            },
            title: {
                type: 'float'
            },
            openEffect: 'none',
            closeEffect: 'none'

        },
        afterClose: function () {
                window.location.reload();
            }
    });

})
