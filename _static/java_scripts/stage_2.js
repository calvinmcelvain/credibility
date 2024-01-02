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
function DecisionFormadvisor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const lowError = document.getElementById("low_error");
    const highError = document.getElementById("high_error");

    const lowChecked = document.querySelector('input[name="pa_low_advice"]:checked');
    const highChecked = document.querySelector('input[name="pa_high_advice"]:checked');

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
function DecisionForminvestor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();

    // Handle confirm button click inside the modal
    document.getElementById("confirmButton").onclick = function () {
        confirmationModal.hide();
        document.forms[0].submit();
    };
}

/// Slider design | i.e. Value of outputs and optional input box
window.onload = function() {
    document.getElementById("slider").value = 0;
    document.getElementById("sliderInput").value = 0;
};
function updateInputValue(value) {
    document.getElementById("sliderInput").value = value;
}
function updateSliderFromInput(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider").value = value;
    }
}

/// Slider design for practice
window.onload = function() {
    document.getElementById("slider1").value = 0;
    document.getElementById("sliderInput1").value = 0;
};
function updateInputValue1(value) {
    document.getElementById("sliderInput1").value = value;
}
function updateSliderFromInput1(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider1").value = value;
    }
}

window.onload = function() {
    document.getElementById("slider2").value = 0;
    document.getElementById("sliderInput2").value = 0;
};
function updateInputValue2(value) {
    document.getElementById("sliderInput2").value = value;
}
function updateSliderFromInput2(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider2").value = value;
    }
}

window.onload = function() {
    document.getElementById("slider3").value = 0;
    document.getElementById("sliderInput3").value = 0;
};
function updateInputValue3(value) {
    document.getElementById("sliderInput3").value = value;
}
function updateSliderFromInput3(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider3").value = value;
    }
}