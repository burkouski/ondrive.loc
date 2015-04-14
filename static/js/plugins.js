$(function () {

    $(".popup").fancybox({
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
