console.log('hello')
import memo_id
const hello = () => {
    console.log('hello')
    console.log(memo_id)
    $.ajax({
        type: "POST",
        url: "/memos/api/memos",
        data: dataString,
        success: function() {
          $('#contact_form').html("<div id='message'></div>");
          $('#message').html("<h2>Contact Form Submitted!</h2>")
          .append("<p>We will be in touch soon.</p>")
          .hide()
          .fadeIn(1500, function() {
            $('#message').append("<img id='checkmark' src='images/check.png' />");
          });
        }
      });
}
const memo = document.getElementById('save-memo-btn')
memo.addEventListener('click', hello)