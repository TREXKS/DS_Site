
// About Page Functonality
function about() {

  if (document.querySelector('#about').innerHTML == 'Hydrosphere is an Automated Hydroponic Monitoring System') {
      document.querySelector('#about').innerHTML = 'Hydrosphere stores your sensor data and automates the growing process using a variety of sensors'
      $('#about_logo2').fadeToggle(1);
      $('#about_logo3').fadeToggle(3000);
      $('#aboutButton').fadeToggle(1);
      $('#backButton').fadeToggle(3000);
      $('#about_small').fadeToggle(1);
      $('#about_small_3').delay(4000).fadeToggle(5000);
      $('#about_logo6').delay(4000).fadeToggle(5000);


  } else {
  document.querySelector('#about').innerHTML = 'Hydrosphere is an Automated Hydroponic Monitoring System'
  $('#about_logo').fadeToggle(1);
  $('#about_logo2').fadeToggle(3000);
  $('#about_small').delay(2000).fadeToggle(4000);

  }
  }

  function aboutSecond() {

    if (document.querySelector('#about').innerHTML == 'Our Sensors provide exactly what the plant needs to survive and to grow a healthy life') {
        document.querySelector('#about').innerHTML = 'So what do you say? Want to provide the best for your plant?'
        $('#about_logo4').fadeToggle(1);
        $('#backButton').fadeToggle(1);
        $('#shopButton').delay(6000).fadeToggle(2000);
        $('#registerButton').delay(2000).fadeToggle(3000);
        $('#about_small_2').fadeToggle(1);
        $('#about_logo').fadeToggle(8000);


    } else {
    document.querySelector('#about').innerHTML = 'Our Sensors provide exactly what the plant needs to survive and to grow a healthy life'
    $('#about_logo3').fadeToggle(1);
    $('#about_logo4').fadeToggle(3000);
    $('#about_small_2').delay(2000).fadeToggle(4000);
    $('#about_small_3').fadeToggle(1);
    $('#about_logo6').fadeToggle(1);
    }
    }

// Shop Functonality

$(function () {
  $('#btn1').on('click', function() {
    $('#panel1').fadeToggle(1000);
  });
  $('#btn2').on('click', function() {
    $('#panel2 ').fadeToggle(1000);
  });
  $('#btn3').on('click', function() {
    $('#panel3').fadeToggle(1000);
  });
  $('#btn4').on('click', function() {
    $('#panel4').fadeToggle(1000);
  });
})


$(function () {
  $('#start_info').on('click', function() {
    $('#start_img').fadeToggle(1);
    $('#start_pan').fadeToggle(1);

  });
  $('#adv_info').on('click', function() {
    $('#adv_img').fadeToggle(1);
    $('#adv_pan').fadeToggle(1);

  });

  $('#baro_info_toggle').on('click', function() {
    $('#baro_img').fadeToggle(1);
    $('#baro_pan').fadeToggle(1);

  });
  $('#ph_info').on('click', function() {
    $('#ph_img').fadeToggle(1);
    $('#ph_pan').fadeToggle(1);

  });
  $('#moist_info').on('click', function() {
    $('#moist_img').fadeToggle(1);
    $('#moist_pan').fadeToggle(1);

  });

  $('#water_info').on('click', function() {
    $('#water_img').fadeToggle(1);
    $('#water_pan').fadeToggle(1);

  });
  $('#air_info').on('click', function() {
    $('#hum_img').fadeToggle(1);
    $('#air_pan').fadeToggle(1);

  });
  $('#tds_info').on('click', function() {
    $('#tds_img').fadeToggle(1);
    $('#tds_pan').fadeToggle(1);

  });

})
