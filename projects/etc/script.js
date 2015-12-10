$(function() {
  $('.section .text').bind('inview', function(event, inView, visibleX, visibleY) {
    var $this = $(this);
    console.log('visibleY:', visibleY, 'inView', inView);
    if (!window.LOADED) {
      return;
    }
    if (inView) {
      $(this).parent().addClass('visible');
    } else {
      $(this).parent().removeClass('visible');
    }
  });
});
