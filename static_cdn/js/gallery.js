var main = function(){
  var slide = $('.slide');
  //slide.addClass('hidden');
  var currentSlide = slide.first();
  currentSlide.addClass('active-slide');
  var nextSlide = currentSlide.next();

  $(window).click(function(){
      if(nextSlide.length == 0){
        nextSlide = $('.slide').first();
        }
      currentSlide.fadeOut(600).removeClass('active-slide');
      nextSlide.fadeIn(600).addClass('active-slide');

  })
}

$(document).ready(main);
