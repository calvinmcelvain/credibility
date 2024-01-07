// Sending Websocket & Adjusting history table width
window.onload = function() {
    const loaded = sessionStorage.getItem('loaded');

    if (loaded !== 'true') {
        liveSend('send');
        sessionStorage.setItem('loaded', 'true');
    }

    // Adjusting History Width
  const headerCells = document.querySelectorAll('.history_header th');
  const dataCells = document.querySelectorAll('#data_table td');

  headerCells.forEach((headerCell, index) => {
      dataCells[index].style.width = headerCell.offsetWidth + 'px';
  });
}


// Websocket to check if all players are ready
function liveRecv(data) {
    if (data === 'all_ready') {
        sessionStorage.setItem('IsClicked', 'false')
        document.forms[0].submit();
    }
}
