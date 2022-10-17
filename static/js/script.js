  // Filtro portfólio

  $('.filter-btn').on('click', function() {

    let type = $(this).attr('id');
    let boxes = $('.project-box');

    $('.main-btn').removeClass('active');
    $(this).addClass('active');

    if(type == 'camp-btn') {
      eachBoxes('camp', boxes);
    } else if(type == 'dsg-btn') {
      eachBoxes('dsg', boxes);
    } else if(type == 'cri-btn') {
      eachBoxes('cri', boxes);
    } else if(type == 'loj-btn') {
      eachBoxes('loj', boxes);
    } else {
      eachBoxes('all', boxes);
    } 

  });

  function eachBoxes(type, boxes) {

    if(type == 'all') {
      $(boxes).fadeIn();
    } else {
      $(boxes).each(function() {
        if(!$(this).hasClass(type)) {
          $(this).fadeOut('slow');
        } else {
          $(this).fadeIn();
        }
      });
    }
  }
   
