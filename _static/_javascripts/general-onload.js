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