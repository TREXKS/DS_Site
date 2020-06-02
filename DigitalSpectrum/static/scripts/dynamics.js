
$('#bologna-list a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})

$(function () {
  $('#user_button').on('click', function() {
    $('#packages').fadeToggle(1);
    $('#packages_display').fadeToggle(1);
    $('#user_info').fadeToggle(1);
    $('#user_info_display').fadeToggle(1);
    $('#user_button').fadeToggle(1);

  });

})
