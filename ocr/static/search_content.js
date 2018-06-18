
  $(document).ready(function() {
  console.log($);
    var content = [
    { title: 'Cash Transfer' },
    { title: 'Security Transfer' },
    { title: 'Incoming Wires' },
    { title: 'Ach-out' },
    { title: 'Ach-in' },
    { title: 'Albania' },
    { title: 'Armenia' },
    { title: 'Netherlands Antilles' },
    { title: 'Angola' },
    { title: 'Argentina' },




  ];

  $('.ui.search')
    .search({
      searchFields: ['title'],
      source: content
    })
  ;

  $('.ui.button')
    .on('click', function() {
      $('.ui.search').search('show results');
    })
  ;

});