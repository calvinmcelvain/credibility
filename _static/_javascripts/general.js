/// Otree timeout
document.addEventListener("DOMContentLoaded", function () {
    const timeout_id = document.getElementById("timeout_id");
    setTimeout(function () {
        timeout_id.textContent = "Please Make Your Decision";
        timeout_id.classList.add("flashing-red");
    }, js_vars.timeout);
});

/// Stage 1 recap timeout
document.addEventListener("DOMContentLoaded", function () {
    const recap_table = document.getElementById("recap_table");
    const cont_button = document.getElementById("validation");
    setTimeout(function () {
        recap_table.hidden = true;
        cont_button.classList.add("flashing-red");
    }, js_vars.timeout_instr);
});


/// Websocket to check if all players are ready
function liveRecv(data) {
    if (data === 'all_ready') {
        sessionStorage.setItem('IsClicked', 'false')
        document.forms[0].submit();
    }
}

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
function idconfirmation(event) {
    event.preventDefault();
    var playerId = document.getElementById("player_id").value;
    var errorMessage = document.getElementById("errorMessage");

    if (playerId.trim() === "") {
        errorMessage.textContent = "Please enter your player ID";
        errorMessage.style.display = "block";
    } else if (playerId.length > 2) {
        errorMessage.textContent = "Player ID cannot be more than 2 digits";
        errorMessage.style.display = "block";
    } else {
        errorMessage.style.display = "none";
        // Show the Bootstrap modal
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function() {
            confirmationModal.hide();
            document.forms[0].submit();
        };
    }
}

/// Stage 1 instructions quiz answer validation
function CheckQuizAnswersP1() {
    var answers = {
      Q1a: document.querySelector('input[name="Q1a"]').value.trim(),
      Q1b: document.querySelector('input[name="Q1b"]').value.trim(),
      Q1c: document.querySelector('input[name="Q1c"]').value.trim(),
      Q2a: document.querySelector('input[name="Q2a"]').value.trim(),
      Q2b: document.querySelector('input[name="Q2b"]').value.trim(),
      Q2c: document.querySelector('input[name="Q2c"]').value.trim(),
    };

    var correctAnswers = {
      Q1a: '0',
      Q1b: '12',
      Q1c: '3',
      Q2a: '24',
      Q2b: '12',
      Q2c: '0',
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
function CheckQuizAnswersP2() {
    var answers = {
      Q3a: document.querySelector('select[name="Q3a"]').value.trim(),
      Q3b: document.querySelector('select[name="Q3b"]').value.trim(),
      Q3c: document.querySelector('select[name="Q3c"]').value.trim(),
      Q4: document.querySelector('select[name="Q4"]').value.trim(),
    };

    var correctAnswers = {
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


// Showing error message
function showErrorMessage(question) {
    var errorSpan = document.getElementById('error' + question);
    errorSpan.textContent = 'Incorrect';
    errorSpan.style.display = 'inline';
}

/// Stage 1 Advisor decision confirmation button
function ConfirmationAdvisorStg1(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const lowError = document.getElementById("low_error");
    const medError = document.getElementById("med_error");
    const highError = document.getElementById("high_error");

    const lowChecked = document.querySelector('input[name="advisor_low_advice"]:checked');
    const medChecked = document.querySelector('input[name="advisor_med_advice"]:checked');
    const highChecked = document.querySelector('input[name="advisor_high_advice"]:checked');

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
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function () {
            confirmationModal.hide();
            document.forms[0].submit();
        };
    }
}

/// Stage 1 Investor decision confirmation button
function ConfirmationInvestorStg1(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const Error = document.getElementById("error");
    const ErrorChecked = document.querySelector('input[name="investor_decision"]:checked');

    if (!ErrorChecked) {
        Error.textContent = "Field must be selected";
        Error.style.display = "block";

    } else {
        Error.style.display = "none";
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function () {
            confirmationModal.hide();
            document.forms[0].submit();
        };
    }
}

/// Stage 2 slider functions
function updateSliderFromNumber() {
    var value = parseInt(document.getElementById('numberInput').value);
    document.getElementById('slider').value = value;
}
function updateInputValues(value) {
    document.getElementById("numberInput").value = value;
}


// Slider functions for slider practice
function updateSliderFromNumber1() {
    var value = parseInt(document.getElementById('numberInput1').value);
    document.getElementById('slider1').value = value;
}
function updateInputValues1(value) {
    document.getElementById("numberInput1").value = value;
}

function updateSliderFromNumber2() {
    var value = parseInt(document.getElementById('numberInput2').value);
    document.getElementById('slider2').value = value;
}
function updateInputValues2(value) {
    document.getElementById("numberInput2").value = value;
}

function updateSliderFromNumber3() {
    var value = parseInt(document.getElementById('numberInput3').value);
    document.getElementById('slider3').value = value;
}
function updateInputValues3(value) {
    document.getElementById("numberInput3").value = value;
}

function SliderCheckAndSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    var Value1 = parseInt(document.getElementById('numberInput1').value);
    var Value2 = parseInt(document.getElementById('numberInput2').value);
    var Value3 = parseInt(document.getElementById('numberInput3').value);

    // Define target values
    var targetValues = {
        slider1: 30,
        slider2: 270,
        slider3: 240,
    };

    var isValid = true;

    // Check if all sliders match the target values
    if (Value1 !== targetValues.slider1) {
        displayError('error1', 'Please put Minimum Endowment to 30');
        isValid = false;
    } else {
        hideError('error1');
    }

    if (Value2 !== targetValues.slider2) {
        displayError('error2', 'Please put Minimum Endowment to 270');
        isValid = false;
    } else {
        hideError('error2');
    }

    if (Value3 !== targetValues.slider3) {
        displayError('error3', 'Please put  Minimum Endowment to 240');
        isValid = false;
    } else {
        hideError('error3');
    }

    // If all sliders are set correctly, submit the form
    if (isValid) {
        sessionStorage.setItem('IsClicked', 'true');
        liveSend('send');
        document.getElementById('validation').disabled = true;
        document.getElementById('slider1').disabled = true;
        document.getElementById('numberInput2').disabled = true;
        document.getElementById('slider3').disabled = true;
        document.getElementById('numberInput3').disabled = true;
    }
}

function displayError(errorId, message) {
    var errorElement = document.getElementById(errorId);
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}

function hideError(errorId) {
    var errorElement = document.getElementById(errorId);
    errorElement.style.display = 'none';
}

/// Stage 2 Advisor decision confirmation button
function ConfirmationAdvisorStg2(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const lowError = document.getElementById("low_error");
    const highError = document.getElementById("high_error");

    const lowChecked = document.querySelector('input[name="advisor_low_advice"]:checked');
    const highChecked = document.querySelector('input[name="advisor_high_advice"]:checked');

    if (!lowChecked) {
        lowError.textContent = "Field must be selected";
        lowError.style.display = "block";
    } else {
        lowError.style.display = "none";
    }

    if (!highChecked) {
        highError.textContent = "Field must be selected";
        highError.style.display = "block";
    } else {
        highError.style.display = "none";
    }

    // Check if all three are checked before submitting the form
    if (lowChecked && highChecked) {
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function () {
            confirmationModal.hide();
            document.forms[0].submit();
        };
    }
}

/// Stage 2 Investor decision confirmation button
function ConfirmationInvestorStg2() {
    const Error = document.getElementById("error");
    const numbox = document.getElementById("numberInput").value;

    if (!numbox) {
        Error.textContent = "Slider must be set";
        Error.style.display = "block";
    } else {
        Error.style.display = "none";
        const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function () {
            confirmationModal.hide();
            document.forms[0].submit();
        };
    }
}

/// Final Investor confirmation slider functions
function s1updateInputValues(value) {
    document.getElementById("s1numberInput").value = value;
}
function s2updateInputValues(value) {
    document.getElementById("s2numberInput").value = value;
}
function s3updateInputValues(value) {
    document.getElementById("s3numberInput").value = value;
}

function s1updateSliderFromNumber() {
    var value = parseInt(document.getElementById('s1numberInput').value);
    document.getElementById('s1slider').value = value;
}
function s2updateSliderFromNumber() {
    var value = parseInt(document.getElementById('s2numberInput').value);
    document.getElementById('s2slider').value = value;
}
function s3updateSliderFromNumber() {
    var value = parseInt(document.getElementById('s3numberInput').value);
    document.getElementById('s3slider').value = value;
}
function ShowConfirmation() {
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();

    // Handle confirm button click inside the modal
    document.getElementById("confirmButton").onclick = function () {
        confirmationModal.hide();
        document.forms[0].submit();
    };
}

/// Demographics page errors
function CheckDemoFields() {
    var Q1 = document.querySelector('input[name="age"]').value;
    var Q2 = document.querySelector('select[name="gender"]').value;
    var Q3 = document.querySelector('select[name="ethnicity"]').value;
    var Q4 = document.querySelector('select[name="hol"]').value;
    
    var isValid = true;

    // Check if questions have been filled
    if (!Q1 || !Q2 || !Q3 || !Q4) {
        displayError('demographics_error', 'Please fill out all fields');
        isValid = false;
    } else {
        hideError('demographics_error');
    }

    // If all sliders are set correctly, submit the form
    if (isValid) {
        document.forms[0].submit();
    }
}

/// Stage 2 instructions quiz validation
function CheckQuizAnswersStg2() {
    var answers = {
        Q1: document.querySelector('select[name="Q1"]').value.trim(),
        Q2: document.querySelector('select[name="Q2"]').value.trim(),
        Q3: document.querySelector('input[name="Q3"]').value.trim(),
        Q4: document.querySelector('input[name="Q4"]').value.trim(),
        Q5: document.querySelector('select[name="Q5"]').value.trim(),
      };
  
      var correctAnswers = {
        Q1: 'True',
        Q2: 'False',
        Q3: '80',
        Q4: '320',
        Q5: 'True',
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
        document.forms[0].submit();
      }
}