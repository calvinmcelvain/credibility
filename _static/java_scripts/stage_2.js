/// Websocket sending ready signal
function validating() {
  document.getElementById('validation').disabled = true;
  document.querySelectorAll('input[type=radio]').forEach(function (radioButton) {
    radioButton.disabled = true
  });
  sessionStorage.setItem('IsClicked', 'true');
  liveSend('send');
}

/// Hiding Otree Timer
document.addEventListener("DOMContentLoaded", function (event) {
    $('.otree-timer__time-left').on('update.countdown', function (event) {
        if (event.offset.totalSeconds <= 10) {
            $('.otree-timer').show();
        }
    });
});

/// Player Confirmation
function ConfirmDecision() {
  let confirmed = confirm("Are you sure you want to continue?");
  if (confirmed) {
    document.submit();
    }
  else {
    event.preventDefault();
  }
}

/// Slider design | i.e. Value of outputs and optional input box
window.onload = function() {
    document.getElementById("slider").value = 0;
    document.getElementById("sliderInput").value = 0;
};
function updateInputValue(value) {
    document.getElementById("sliderInput").value = value;
}