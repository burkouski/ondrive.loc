$(function () {

    $(".popup").fancybox({
        maxWidth	: 500,
        maxHeight: 700,
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

    $('input[type=file]').bootstrapFileInput({
        'title': 'gdsgdsgds'
    });
})
