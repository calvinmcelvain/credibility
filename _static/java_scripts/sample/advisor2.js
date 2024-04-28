/// sample Decision Button
function DecisionFormsampleadvisor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const lowError = document.getElementById("low_error");
    const medError = document.getElementById("med_error");

    const lowChecked = document.querySelector('input[name="pa_low_advice"]:checked');
    const medChecked = document.querySelector('input[name="pa_med_advice"]:checked');

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

    // Check if all three are checked before submitting the form
    if (lowChecked && medChecked) {
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        // Handle confirm button click inside the modal
        document.getElementById("confirmButton").onclick = function () {
            confirmationModal.hide();
            document.getElementById('validation').disabled = true;
            sessionStorage.setItem('IsClicked', 'true');
            liveSend('send');
            document.querySelectorAll('input[type=radio]').forEach(function (radioButton) {
            radioButton.hidden = true
            });
        };
    }
}


// Function to save radio button values to sessionStorage
function saveRadioStateadvisor() {
    const lowChecked = document.querySelector('input[name="pa_low_advice"]:checked');
    const medChecked = document.querySelector('input[name="pa_med_advice"]:checked');

    if (lowChecked) {
        sessionStorage.setItem('pa_low_advice', lowChecked.value);
    }
    if (medChecked) {
        sessionStorage.setItem('pa_med_advice', medChecked.value);
    }
}


// Function to restore radio button values from sessionStorage
function restoreRadioStateadvisor() {
    const lowValue = sessionStorage.getItem('pa_low_advice');
    const medValue = sessionStorage.getItem('pa_med_advice');

    if (lowValue) {
        document.querySelector('input[name="pa_low_advice"][value="' + lowValue + '"]').checked = true;
    }
    if (medValue) {
        document.querySelector('input[name="pa_med_advice"][value="' + medValue + '"]').checked = true;
    }
}


// Restore radio button values on page load
document.addEventListener("DOMContentLoaded", function() {
    restoreRadioStateadvisor();
});


// Save radio button values before page reload or unload
window.addEventListener("beforeunload", function() {
    saveRadioStateadvisor();
});
