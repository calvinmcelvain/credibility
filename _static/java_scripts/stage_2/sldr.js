/// Slider design | i.e. Value of outputs and optional input box
window.onload = function() {
    const IsClicked = sessionStorage.getItem('IsClicked');
    if (IsClicked === 'true') {
        document.getElementById('validation').disabled = true;
    }
};

// Websocket to check if all players are ready
function liveRecv(data) {
    if (data === 'all_ready') {
        sessionStorage.setItem('IsClicked', 'false')
        document.forms[0].submit();
    }
}


function updateInputValue(value) {
    document.getElementById("sliderInput").value = value;
}
function updateSliderFromInput(value) {
    // Ensure the input value is within the valid range
    if (value >= 0 && value <= 300) {
        document.getElementById("slider").value = value;
    }
}

function checkAndSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    var slider1Value = parseInt(document.getElementById('sliderInput1').value);
    var slider2Value = parseInt(document.getElementById('sliderInput2').value);
    var slider3Value = parseInt(document.getElementById('sliderInput3').value);

    // Define target values
    var targetValues = {
        slider1: 30,
        slider2: 27,
        slider3: 45
    };

    var isValid = true;

    // Check if all sliders match the target values
    if (slider1Value !== targetValues.slider1) {
        displayError('error1', 'Please put slider to indicated value');
        isValid = false;
    } else {
        hideError('error1');
    }

    if (slider2Value !== targetValues.slider2) {
        displayError('error2', 'Please put slider to indicated value');
        isValid = false;
    } else {
        hideError('error2');
    }

    if (slider3Value !== targetValues.slider3) {
        displayError('error3', 'Please put slider to indicated value');
        isValid = false;
    } else {
        hideError('error3');
    }

    // If all sliders are set correctly, submit the form
    if (isValid) {
        sessionStorage.setItem('IsClicked', 'true');
        liveSend('send');
        document.getElementById('validation').disabled = true;
    }
}

function displayError(errorId, message) {
    var errorElement = document.getElementById(errorId);
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}

function hideError(errorId) {
    var errorElement = document.getElementById(errorId);
    errorElement.style.display = 'none';
}


// Function to update slider from input
function updateSliderFromInput1() {
    var value = parseInt(document.getElementById('sliderInput1').value);
    document.getElementById('slider1').value = value;
}
function updateInputValue1(value) {
    document.getElementById("sliderInput1").value = value;
}

function updateSliderFromInput2() {
    var value = parseInt(document.getElementById('sliderInput2').value);
    document.getElementById('slider2').value = value;
}
function updateInputValue2(value) {
    document.getElementById("sliderInput2").value = value;
}

function updateSliderFromInput3() {
    var value = parseInt(document.getElementById('sliderInput3').value);
    document.getElementById('slider3').value = value;
}
function updateInputValue3(value) {
    document.getElementById("sliderInput3").value = value;
}