// Sending live method & Adjusting History Table Width
window.onload = function () {
    liveSend('send');

    const headerCells = document.querySelectorAll('.history_header th');
    const dataCells = document.querySelectorAll('#data_table td');
  
    headerCells.forEach((headerCell, index) => {
        dataCells[index].style.width = headerCell.offsetWidth + 'px';
    });
  }