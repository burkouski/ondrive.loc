$(function(){
    var location = window.location.href
    $('#main-menu a').each(function() {
    if (location.indexOf($(this).attr('href')) !=-1) {
      $(this).parent().addClass('active');
        //console.log(location.indexOf($(this).attr('href')))
    }
  });

  //$('.js-input__number').on("change keyup input click", function () {
  //      if (this.value.match(/[^0-9]/g)) {
  //          this.value = this.value.replace(/[^0-9]/g, '');
  //      }
  //  });
})
