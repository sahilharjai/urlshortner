/**
 * Created by bhavyaagg on 27/08/17.
 */

$(function () {

  var $location = $(location);
  var arr = $location.attr('href').split("=");
  var $loginButton = $('#login-button');
  var $menu = $('#menu');
  var $shortCode = $('#shortcode');
  var $modal = $('#modal');
  var $LongURL = $('#url');

  var $result = $('#result');
  var $shortUrl = $('#shortUrl')
  var $cross = $('#cross')

  var $site_popularity = $('#site_popularity')
  var $length_of_url = $('#length_of_url')
  var $existing_dns_record = $('#existing_dns_record')
  var $ports = $('#ports')
  var $age_of_domain = $('#age_of_domain')

  if (arr.length === 2) {
    $.post('/auth', {code: arr[1]}, function (authtoken) {
      if (authtoken.success === true) {
        localStorage.setItem("authtoken", authtoken.token);
        $loginButton.remove();
        $menu.append('<li><a href="#">' + authtoken.user + '</a></li>');
      } else {
        $location[0].replace("/admin");
      }
    })
  }

  $('.nav-container').load('/admin/includes/nav-container.html');

  $('#submit').click(function () {

    var URLregex = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/g;

    if ($LongURL.val().length === 0) {

      $shortCode.html('<div class=\'alert alert-danger\'><strong>URL field is empty</strong> </div>   ');
      $LongURL.css('border-color', 'red');

    } else if (URLregex.test($LongURL.val()) === false) {

      $shortCode.html('<div class=\'alert alert-warning\'><strong>Invalid URL format</strong> <p> The URL must be of form </br>\"www.example.com"\ </br> \"https://example.com\" </br> \"mailto:foo@bar.com\" </p> </div> ');
      $LongURL.css('border-color', 'red');

    } else {
      $modal.css("display","block");
      $.post('http://127.0.0.1:8000/api/url-create/', {
        url: $LongURL.val(),
      }, function (data) {
          console.log(data)
        /*if (typeof data === 'string') {*/
          if(data.result==1)
          {
            $result.append('<span class="safe">Safe<span>')
          }
          else
          {
            $result.append('<span class="phishing">Phishing<span>')
          }
          $shortUrl.html('<a id="trgt" href="'+data.longUrl+'">'+data.shortCode+'</a><button id="copy" class="btn btn-filled hover-light copy" data-clipboard-target="#trgt"> Copy </button>');
          if(data.site_popularity==-1)
          {
            site_popularity = 'High'
          }
          else if(data.site_popularity==0)
          {
            site_popularity = 'Medium'
          }
          else
          {
            site_popularity = 'Low'
          }
          $site_popularity.append('<div class="col-xs-6 '+site_popularity+'">'+site_popularity+'</div>')


          if(data.length_of_url==1)
          {
            length_of_url = 'High'
          }
          else if(data.length_of_url==0)
          {
            length_of_url = 'Medium'
          }
          else
          {
            length_of_url = 'Low'
          }
          $length_of_url.append('<div class="col-xs-6 '+length_of_url+'">'+length_of_url+'</div>')


          ports = setCrossRight(data.ports)
          $ports.append('<div class="col-xs-6"><i class="fa fa'+ports+'" aria-hidden="true"></i></div>')

          existing_dns_record = setCrossRight(data.existing_dns_record)
          $existing_dns_record.append('<div class="col-xs-6"><i class="fa fa'+existing_dns_record+'" aria-hidden="true"></i></div>')

          age_of_domain = setCrossRight(data.age_of_domain)
          $age_of_domain.append('<div class="col-xs-6"><i class="fa fa'+age_of_domain+'" aria-hidden="true"></i></div>')
        
      }) //post request ends here
    } //end of if else block
  });

  $shortUrl.on('click', '#shortUrl button', function () {
    console.log("clicked")
    var range = document.createRange();
    range.selectNode($('.shortcode a')[0]);
    window.getSelection().addRange(range);
    document.execCommand("Copy");
    window.alert('Link Copied to your clipboard')
  });

  var $heading = $('#homeHeading');
  var $form = $('#shortcodeform');
  $("#shortForm").click(function () {
    $heading.css('display', 'none');
    $form.css('display', "block");
  });

  $cross.on('click',function(){
    $modal.css("display","none");
    console.log("last",$site_popularity.last())
    $site_popularity.children().last().remove()
    $length_of_url.children().last().remove()
    $existing_dns_record.children().last().remove()
    $age_of_domain.children().last().remove()
    $ports.children().last().remove()
    $LongURL.val(' ')
  })

  function setCrossRight(data)
  {
    if(data==-1)
    {
      return '-check right'
    }
    return '-times cross'
  }




});