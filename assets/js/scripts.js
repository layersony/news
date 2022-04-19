$(document).ready(()=>{
  $(window).on('resize', function() {
    if (window.innerWidth <= 980 ){
      $('.topcont').removeClass("container")
      $('.topcont').addClass("container-fluid")
    }else{
      $('.topcont').addClass("container")
      $('.topcont').removeClass("container-fluid")
    }
  });
})
