/// Decision Button
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
