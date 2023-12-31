/// Websocket sending ready signal
function validating() {
  document.getElementById('validation').disabled = true;
  document.querySelectorAll('input[type=radio]').forEach(function (radioButton) {
    radioButton.disabled = true
  });
  sessionStorage.setItem('IsClicked', 'true');
  liveSend('send');
}

/// ID screen
function validateForm(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    var playerId = document.getElementById("player_id").value;
    var errorMessage = document.getElementById("errorMessage");

    if (playerId.trim() === "") {
        errorMessage.textContent = "Please enter your player ID"; // Error message for empty input
        errorMessage.style.display = "block"; // Show error message if the input is empty
    } else if (playerId.length > 2) {
        errorMessage.textContent = "Player ID cannot be more than 2 digits"; // Error message for more than 2 digits
        errorMessage.style.display = "block"; // Show error message for more than 2 digits
    } else {
        errorMessage.style.display = "none"; // Hide error message if input is not empty and within 2 digits
        let confirmed = confirm("Are you sure your ID is correct?");
        if (confirmed) {
            document.forms[0].submit();
        } else {
            event.preventDefault();
        }
    }
}

/// Decision Table errors
function DecisionFormadvisor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const lowError = document.getElementById("low_error");
    const medError = document.getElementById("med_error");
    const highError = document.getElementById("high_error");

    const lowChecked = document.querySelector('input[name="pa_low_advice"]:checked');
    const medChecked = document.querySelector('input[name="pa_med_advice"]:checked');
    const highChecked = document.querySelector('input[name="pa_high_advice"]:checked');

    if (!lowChecked) {
        lowError.textContent = "Field must be selected";
        lowError.style.display = "block";
    } else {
        lowError.style.display = "none";
    }

    if (!medChecked) {
        medError.textContent = "Field must be selected";
        medError.style.display = "block";
    } else {
        medError.style.display = "none";
    }

    if (!highChecked) {
        highError.textContent = "Field must be selected";
        highError.style.display = "block";
    } else {
        highError.style.display = "none";
    }

    // Check if all three are checked before submitting the form
    if (lowChecked && medChecked && highChecked) {
        let confirmed = confirm("Are you sure you want to continue?");
        if (confirmed) {
              document.forms[0].submit();
        } else {
            event.preventDefault();
        }
    }
}
function DecisionForminvestor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const Error = document.getElementById("error");
    const ErrorChecked = document.querySelector('input[name="pb_decision"]:checked');

    if (!ErrorChecked) {
        Error.textContent = "Field must be selected";
        Error.style.display = "block";

    } else {
        Error.style.display = "none";
        let confirmed = confirm("Are you sure you want to continue?");
        if (confirmed) {
              document.forms[0].submit();
        } else {
            event.preventDefault();
        }
    }
}

/// Sample Decision Table errors
function DecisionFormsampleadvisor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const lowError = document.getElementById("low_error");
    const medError = document.getElementById("med_error");
    const highError = document.getElementById("high_error");

    const lowChecked = document.querySelector('input[name="pa_low_advice"]:checked');
    const medChecked = document.querySelector('input[name="pa_med_advice"]:checked');
    const highChecked = document.querySelector('input[name="pa_high_advice"]:checked');

    if (!lowChecked) {
        lowError.textContent = "Field must be selected";
        lowError.style.display = "block";
    } else {
        lowError.style.display = "none";
    }

    if (!medChecked) {
        medError.textContent = "Field must be selected";
        medError.style.display = "block";
    } else {
        medError.style.display = "none";
    }

    if (!highChecked) {
        highError.textContent = "Field must be selected";
        highError.style.display = "block";
    } else {
        highError.style.display = "none";
    }

    // Check if all three are checked before submitting the form
    if (lowChecked && medChecked && highChecked) {
        let confirmed = confirm("Are you sure you want to continue?");
        if (confirmed) {
              document.getElementById('validation').disabled = true;
              sessionStorage.setItem('IsClicked', 'true');
              liveSend('send');
        } else {
            event.preventDefault();
        }
    }
}
function DecisionFormsampleinvestor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const Error = document.getElementById("error");
    const ErrorChecked = document.querySelector('input[name="pb_decision"]:checked');

    if (!ErrorChecked) {
        Error.textContent = "Field must be selected";
        Error.style.display = "block";

    } else {
        Error.style.display = "none";
        let confirmed = confirm("Are you sure you want to continue?");
        if (confirmed) {
              document.getElementById('validation').disabled = true;
              sessionStorage.setItem('IsClicked', 'true');
              liveSend('send');
        } else {
            event.preventDefault();
        }
    }
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

///Instructions Quiz Answer Validation
function checkAnswers() {
var answers = {
  Q1a: document.querySelector('input[name="Q1a"]').value.trim(),
  Q1b: document.querySelector('input[name="Q1b"]').value.trim(),
  Q1c: document.querySelector('input[name="Q1c"]').value.trim(),
  Q2a: document.querySelector('input[name="Q2a"]').value.trim(),
  Q2b: document.querySelector('input[name="Q2b"]').value.trim(),
  Q2c: document.querySelector('input[name="Q2c"]').value.trim(),
  Q3a: document.querySelector('input[name="Q3a"]:checked') ? document.querySelector('input[name="Q3a"]:checked').value : null,
  Q3b: document.querySelector('input[name="Q3b"]:checked') ? document.querySelector('input[name="Q3b"]:checked').value : null,
  Q3c: document.querySelector('input[name="Q3c"]:checked') ? document.querySelector('input[name="Q3c"]:checked').value : null,
  Q4: document.querySelector('input[name="Q4"]:checked') ? document.querySelector('input[name="Q4"]:checked').value : null,
};

var correctAnswers = {
  Q1a: '1',
  Q1b: '12',
  Q1c: '3',
  Q2a: '14',
  Q2b: '12',
  Q2c: '0',
  Q3a: 'True',
  Q3b: 'False',
  Q3c: 'False',
  Q4: 'True',
};

var correct = true;

// Clear previous error messages
var errorSpans = document.querySelectorAll('[id^="errorQ"]');
errorSpans.forEach(function (errorSpan) {
  errorSpan.textContent = '';
  errorSpan.style.display = 'none';
});

// Check if all answers are correct
for (var key in answers) {
  if (answers[key] !== correctAnswers[key]) {
    showErrorMessage(key);
    correct = false;
  }
}

if (correct) {
  // Submit the form
  document.forms[0].submit();
}
}
function showErrorMessage(question) {
var errorSpan = document.getElementById('error' + question);
errorSpan.textContent = 'Incorrect';
errorSpan.style.display = 'inline';
}