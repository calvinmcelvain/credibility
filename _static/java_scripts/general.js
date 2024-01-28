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


/// Otree Timer
document.addEventListener("DOMContentLoaded", function (event) {
    $('.otree-timer__time-left').on('update.countdown', function (event) {
        if (event.offset.totalSeconds <= 10) {
            $('.otree-timer').show();
        }
    });
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
function validateForm(event) {
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