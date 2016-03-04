(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('a[href*=#]').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			var $target = $(this.hash);
			$target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
			 if ($target.length) {
			 	var targetOffset = $target.offset().top - 100;
				$('html,body').animate({scrollTop: targetOffset}, 1000);
				return false;
			}
		}
	});

  }); // end of document ready
})(jQuery); // end of jQuery name space