$(function(){
    var location = window.location.href
    $('#main-menu a').each(function() {
    if (location.indexOf($(this).attr('href')) !=-1) {
      $(this).parent().addClass('active');
        //console.log(location.indexOf($(this).attr('href')))
    }
  });
})
