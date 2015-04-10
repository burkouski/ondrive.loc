$(function () {

$(".popup").fancybox({
		maxWidth	: 600,
        padding:   0,
		openEffect	: 'none',
		closeEffect	: 'none',
        afterClose: function () {
                parent.location.reload(true);
            }
	});

})
