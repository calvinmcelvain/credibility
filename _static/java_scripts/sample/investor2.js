/// Decision Button
function DecisionForminvestor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();

    // Handle confirm button click inside the modal
    document.getElementById("confirmButton").onclick = function () {
        confirmationModal.hide();
        document.getElementById('validation').disabled = true;
        document.getElementById('slider').disabled = true;
        document.getElementById('sliderInput').disabled = true;
        sessionStorage.setItem('IsClicked', 'true');
        liveSend('send');
    };
}
