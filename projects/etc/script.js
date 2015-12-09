$(function() {
  $('.section .text').bind('inview', function(event, inView, visibleX, visibleY) {
    var $this = $(this);
    if (inView) {
      if ($this.data('loaded')) {
        $(this).parent().addClass('visible');
      } else {
        $this.data('loaded', true);
      }
    } else {
      if ($this.data('loaded')) {
        $(this).parent().removeClass('visible');
      }
    }
  });
});
