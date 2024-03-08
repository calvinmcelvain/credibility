/// sample Decision Button
function DecisionFormsampleinvestor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const Error = document.getElementById("error");
    const ErrorChecked = document.querySelector('input[name="pb_decision"]:checked');

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
            document.getElementById('validation').disabled = true;
            sessionStorage.setItem('IsClicked', 'true');
            liveSend('send');
            document.querySelectorAll('input[type=radio]').forEach(function (radioButton) {
            radioButton.hidden = true
            });
        }
    }
}


// Function to save radio button value to sessionStorage
function saveRadioStateinvestor() {
    const Checked = document.querySelector('input[name="pb_decision"]:checked');

    if (Checked) {
        sessionStorage.setItem('pb_decision', Checked.value);
    }
}


// Function to restore radio button value from sessionStorage
function restoreRadioStateinvestor() {
    const Checkedvalue = sessionStorage.getItem('pb_decision');

    if (Checkedvalue) {
        document.querySelector('input[name="pb_decision"][value="' + Checkedvalue + '"]').checked = true;
    }
}


// Restore radio button values on page load
document.addEventListener("DOMContentLoaded", function() {
    restoreRadioStateinvestor();
});


// Save radio button values before page reload or unload
window.addEventListener("beforeunload", function() {
    saveRadioStateinvestor();
});