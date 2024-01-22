/// Slider design | i.e. Value of outputs and optional input box
window.onload = function() {
    document.getElementById("slider").value = 0;
    document.getElementById("sliderInput").value = 0;
};
function updateInputValue(value) {
    document.getElementById("sliderInput").value = value;
}
function updateSliderFromInput(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider").value = value;
    }
}


/// Slider design for practice
window.onload = function() {
    checkSliders();
  };
  function checkSliders() {
    var slider1Value = document.getElementById('sliderInput1').value;
    var slider2Value = document.getElementById('sliderInput2').value;
    var slider3Value = document.getElementById('sliderInput3').value;

    // Define target values
    var targetValues = {
      slider1: 30,
      slider2: 27,
      slider3: 45
    };

    // Check if all sliders match the target values
    if (
      slider1Value == targetValues.slider1 &&
      slider2Value == targetValues.slider2 &&
      slider3Value == targetValues.slider3
    ) {
      document.querySelector('.button button').disabled = false; // Enable the Continue button
    } else {
      document.querySelector('.button button').disabled = true; // Disable the Continue button
    }
  }
    // Function to update slider from input
  function updateSliderFromInput1(value) {
    document.getElementById('slider1').value = value;
    checkSliders();
  }

  function updateSliderFromInput2(value) {
    document.getElementById('slider2').value = value;
    checkSliders();
  }

  function updateSliderFromInput3(value) {
    document.getElementById('slider3').value = value;
    checkSliders();
  }

// Function to update input from slider
  function updateInputValue1(value) {
    document.getElementById('sliderInput1').value = value;
    checkSliders();
  }

  function updateInputValue2(value) {
    document.getElementById('sliderInput2').value = value;
    checkSliders();
  }

  function updateInputValue3(value) {
    document.getElementById('sliderInput3').value = value;
    checkSliders();
  }