// Checking if button has been clicked & Adjusting History Table Width
window.onload = function () {
  const headerCells = document.querySelectorAll('.history_header th');
  const dataCells = document.querySelectorAll('#data_table td');

  headerCells.forEach((headerCell, index) => {
      dataCells[index].style.width = headerCell.offsetWidth + 'px';
  });
  const IsClicked = sessionStorage.getItem('IsClicked');
    if (IsClicked === 'true') {
        document.getElementById('validation').disabled = true;
    }
}


/// Otree Timeout
document.addEventListener("DOMContentLoaded", function () {
    const timeout_id = document.getElementById("timeout_id");
    setTimeout(function () {
        timeout_id.textContent = "Please Make Your Decision";
        timeout_id.classList.add("flashing-red");
    }, js_vars.timeout);
});


// Websocket to check if all players are ready
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