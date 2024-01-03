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
    document.getElementById("slider1").value = 0;
    document.getElementById("sliderInput1").value = 0;
};
function updateInputValue1(value) {
    document.getElementById("sliderInput1").value = value;
}
function updateSliderFromInput1(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider1").value = value;
    }
}
window.onload = function() {
    document.getElementById("slider2").value = 0;
    document.getElementById("sliderInput2").value = 0;
};
function updateInputValue2(value) {
    document.getElementById("sliderInput2").value = value;
}
function updateSliderFromInput2(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider2").value = value;
    }
}
window.onload = function() {
    document.getElementById("slider3").value = 0;
    document.getElementById("sliderInput3").value = 0;
};
function updateInputValue3(value) {
    document.getElementById("sliderInput3").value = value;
}
function updateSliderFromInput3(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider3").value = value;
    }
}