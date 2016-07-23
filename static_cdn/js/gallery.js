var main = function(){

  //stub function
/*  function empty(){
    return;
  }

  var timeoutID;
  function slightDelay() {
    timeoutID = window.setTimeout(empty, 5000);
  }
  function clearDelay() {
    window.clearTimeout(timeoutID);
  }  */

  var slide =  $('.slide');
  slide.addClass('hiddenDiv');
  var firstSlide = slide.first();
  firstSlide.removeClass('hiddenDiv');
  firstSlide.addClass('active-slide');

  function scrollRight(){
    var currentSlide = $('.active-slide');
    var nextSlide = currentSlide.next();
    if(nextSlide.length == 0){
      nextSlide = $('.slide').first();
    }
    currentSlide.fadeOut(600).addClass('hiddenDiv').removeClass('active-slide');
    nextSlide.fadeIn(300).removeClass('hiddenDiv').addClass('active-slide');
  }

  function scrollLeft(){
    var currentSlide = $('.active-slide');
    var prevSlide = currentSlide.prev();
    if(prevSlide.length == 0){
      prevSlide = $('.slide').last();
    }
    currentSlide.fadeOut(600).addClass('hiddenDiv').removeClass('active-slide');
    prevSlide.fadeIn(300).removeClass('hiddenDiv').addClass('active-slide');
  }

  //arrow keys navigation
  $(document).keyup(function(event){
    if (event.which == 37)
      scrollLeft();
      else if (event.which == 39) {
        scrollRight();
      }
  })

  //prev and next photo in album
    $('#prev').click(function(event){
      event.prevenDefault;
      scrollLeft();
    })

    $('#next').click(function(event){
      event.prevenDefault;
      scrollRight();
     })

     //slide functionality
    $(document).on("swipeleft", function(event){
      scrollLeft();
    })

    $(document).on("swipeRight", function(event){
      scrollRight();
    })


    // toggle sidebar in small screen
    $(document).ready(function () {
      $('[data-toggle="offcanvas"]').click(function () {
        $('.row-offcanvas').toggleClass('active')
      });
    });
}

$(document).ready(main);
