$(function() {
  $('.section').each(function(i, section) {
    var $section = $(section);
    $section
      .find('.text')
      .first()
      .bind('inview', function(event, inView, visibleX, visibleY) {
        var $this = $(this);
        console.log(event, inView, visibleX, visibleY, $this);
        if (inView) {
          if ($this.data('loaded') && visibleY == 'top') {
            $('.visible').removeClass('visible');
          }
          if (!$this.data('loaded')) {
            $this.data('loaded', true);
          }
          $(this).parent().addClass('visible');
        } else if (!inView){
          if ($this.data('loaded')) {
            $(this).parent().removeClass('visible');
          }
        }
      });
  });
});
