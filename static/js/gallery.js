var main = function(){
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
    nextSlide.fadeIn(600).removeClass('hiddenDiv').addClass('active-slide');
  }

  function scrollLeft(){
    var currentSlide = $('.active-slide');
    var prevSlide = currentSlide.prev();
    if(prevSlide.length == 0){
      prevSlide = $('.slide').last();
    }
    currentSlide.fadeOut(600).addClass('hiddenDiv').removeClass('active-slide');
    prevSlide.fadeIn(600).removeClass('hiddenDiv').addClass('active-slide');
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

    // toggle sidebar in small screen
    $(document).ready(function () {
      $('[data-toggle="offcanvas"]').click(function () {
        $('.row-offcanvas').toggleClass('active')
      });
    });


  //owl-carousel
  $(document).ready(function() {

  $("#owl-demo").owlCarousel({

      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true

      // "singleItem:true" is a shortcut for:
      // items : 1,
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

    });

  });
}

$(document).ready(main);
