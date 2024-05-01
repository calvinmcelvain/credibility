/// Decision Button
function DecisionFormsampleinvestor(event) {
    event.preventDefault(); // Prevents the form from submitting by default
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();

    // Handle confirm button click inside the modal
    document.getElementById("confirmButton").onclick = function () {
        confirmationModal.hide();
        document.getElementById('validation').disabled = true;
        document.getElementById('slider').hidden = true;
        document.getElementById('sliderInput').hidden = true;
        sessionStorage.setItem('IsClicked', 'true');
        liveSend('send');
    };
}
