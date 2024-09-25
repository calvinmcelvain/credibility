// Checking if button has been clicked & disabling all inputs
window.onload = function () {
    const IsClicked = sessionStorage.getItem('IsClicked');
      if (IsClicked === 'true') {
          document.getElementById('validation').disabled = true;
          document.getElementById('slider1').disabled = true;
          document.getElementById('numberInput2').disabled = true;
          document.getElementById('slider3').disabled = true;
          document.getElementById('numberInput3').disabled = true;
      }
}