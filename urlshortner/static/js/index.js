$(function () {

  var $location = $(location);
  var arr = $location.attr('href').split("=");
  var $shortCode = $('#shortcode');
  var $modal = $('#modal');
  var $LongURL = $('#url');

  var $result = $('#result');
  var $shortUrl = $('#shortUrl')
  var $cross = $('#cross')


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
      $modal.html('<div id="loader"></div>')
      $.post('/api/url-create/', {
        url: $LongURL.val(),
      }, function (data) {
          console.log(data)
          if(data.site_popularity==-1||data.google_index===-1||data.has_https==-1)
          {
            result='<span class="safe">Safe<span>'
            shortCode_result = '<div id="shortUrl" class="short"><a id="trgt" href="'+data.longUrl+'">pd.ml:8000/'+data.shortCode+'</a><button id="copy" class="btn btn-filled hover-light copy" data-clipboard-target="#trgt"> Copy </button></div>'
          }
          else
          {
            result='<span class="phishing">Phishing<span>'
            shortCode_result = '<div class="alert alert-danger" role="alert" style="width: 70%;font-size: 15px;margin:auto;"><a href="#" class="alert-link">Following Site contains Malicious Contents.Site Can not be Shortened.</a></div>'
          }
          $shortUrl.html('<a id="trgt" href="'+data.longUrl+'">'+data.shortCode+'</a><button id="copy" class="btn btn-filled hover-light copy" data-clipboard-target="#trgt"> Copy </button>');
          if(data.site_popularity==-1)
          {
            site_popularity = 'High'
            site_popularity_class='HighOp'
          }
          else if(data.site_popularity==0)
          {
            site_popularity = 'Medium'
            site_popularity_class='Medium'
          }
          else
          {
            site_popularity = 'Low'
            site_popularity_class='LowOp'
          }


          if(data.a_tag==-1)
          {
            a_tag = 'Low'
            
          }
          else if(data.a_tag==0)
          {
            a_tag = 'Medium'
           
          }
          else
          {
            a_tag = 'High'
            
          }

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

          //subdomain_length
          if(data.subdomain_length==1)
          {
            subdomain_length = 'High'
          }
          else if(data.subdomain_length==0)
          {
            subdomain_length = 'Medium'
          }
          else
          {
            subdomain_length = 'Low'
          }
          
          longUrl = '<div class="alert alert-info" role="alert" style="width: 70%;margin: auto;margin-top: 20px;font-size: 15px;"><a href="'+data.longUrl+'" class="alert-link">'+data.longUrl+'</a></div>'
          ports = setCrossRight(data.ports)
          existing_dns_record = setCrossRight(data.existing_dns_record)
          age_of_domain = setCrossRight(data.age_of_domain)
          reliable_ip = setCrossRight(data.reliable_ip)
          shortened_url = setCrossRight(data.shortened_url)
          contains_at_the_rate = setCrossRightOpp(data.contains_at_the_rate)
          contains_double_slash = setCrossRightOpp(data.contains_double_slash)
          contains_hyphen = setCrossRightOpp(data.contains_hyphen)
          https_token = setCrossRight(data.https_token)
          dns_record = setCrossRight(data.dns_record)
          has_https = setCrossRight(data.has_https)
          form_tag = setCrossRightOpp(data.form_tag)
          abnormal_url = setCrossRightOpp(data.abnormal_url)
          using_mail = setCrossRightOpp(data.using_mail)
          google_index = setCrossRight(data.google_index)
          $modal.html('<div id="card" class="card"><div class="card-body" style="padding-top:8%;">'+

            shortCode_result+
            longUrl+
            '<div class="col-12" style="margin-top: 6%;">'+
                '<ul class="list-group" style="margin-bottom:0;">'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Site Popularity</div><div class="col-xs-6 '+site_popularity_class+'">'+site_popularity+'</div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Length Of URL</div><div class="col-xs-6 '+length_of_url+'">'+length_of_url+'</div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Length Of Subdomain</div><div class="col-xs-6 '+subdomain_length+'">'+subdomain_length+'</div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">A Tag</div><div class="col-xs-6 '+a_tag+'">'+a_tag+'</div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Existing DNS Record</div><div class="col-xs-6"><i class="fa fa'+existing_dns_record+'" aria-hidden="true"></i></div></div></li>'+
                  '<li  class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Age Of Domain</div><div class="col-xs-6"><i class="fa fa'+age_of_domain+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Ports</div><div class="col-xs-6"><i class="fa fa'+ports+'" aria-hidden="true"></i></div></div></li>'+


                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Reliable IP Address</div><div class="col-xs-6"><i class="fa fa'+reliable_ip+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Shortened URL</div><div class="col-xs-6"><i class="fa fa'+shortened_url+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Contains @ Token</div><div class="col-xs-6"><i class="fa fa'+contains_at_the_rate+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Contains Double Slash</div><div class="col-xs-6"><i class="fa fa'+contains_double_slash+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Contains Hyphen</div><div class="col-xs-6"><i class="fa fa'+contains_hyphen+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Https Token</div><div class="col-xs-6"><i class="fa fa'+https_token+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Has Https</div><div class="col-xs-6"><i class="fa fa'+has_https+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">DNS Record</div><div class="col-xs-6"><i class="fa fa'+dns_record+'" aria-hidden="true"></i></div></div></li>'+

                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Form Tag</div><div class="col-xs-6"><i class="fa fa'+form_tag+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Using Mail</div><div class="col-xs-6"><i class="fa fa'+using_mail+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Abnormal URL</div><div class="col-xs-6"><i class="fa fa'+abnormal_url+'" aria-hidden="true"></i></div></div></li>'+
                  '<li class="list-group-item d-flex align-items-center"><div class="row"><div class="col-xs-6 parameter">Google Index</div><div class="col-xs-6"><i class="fa fa'+google_index+'" aria-hidden="true"></i></div></div></li>'+


                  '<li class="list-group-item d-flex align-items-center text-center"><p><h3 style="font-weight:bolder;">Result:&nbsp;<span id="result">'+result+'</span></h3></p></li>'+
                  '<li class="list-group-item" style="height:60px;"><div><button id="cross" class="btn btn-danger" style="float: right;">Close</button></div></li>'+
                '</ul> </div></div></div>'
                )
          $cross = $("#cross")
          $cross.on('click',function(){
            console.log("clicks")
            $modal.css("display","none");
            $modal.val('')
            $LongURL.val('')
          })

        
      }) //post request ends here
    } //end of if else block
  });

  $shortUrl.on('click', '#shortUrl button', function () {
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
    $modal.css("display","block");
    $modal.val('')
    $LongURL.val('')
  })

  function setCrossRight(data)
  {
    if(data==-1)
    {
      return '-check right'
    }
    return '-times cross'
  }

  function setCrossRightOpp(data)
  {
    if(data==1)
    {
      return '-check rightOp'
    }
    return '-times crossOp'
  }

});