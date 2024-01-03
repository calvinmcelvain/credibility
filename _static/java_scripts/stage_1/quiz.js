///Instructions Quiz Answer Validation
function checkAnswers() {
    var answers = {
      Q1a: document.querySelector('input[name="Q1a"]').value.trim(),
      Q1b: document.querySelector('input[name="Q1b"]').value.trim(),
      Q1c: document.querySelector('input[name="Q1c"]').value.trim(),
      Q2a: document.querySelector('input[name="Q2a"]').value.trim(),
      Q2b: document.querySelector('input[name="Q2b"]').value.trim(),
      Q2c: document.querySelector('input[name="Q2c"]').value.trim(),
      Q3a: document.querySelector('input[name="Q3a"]:checked') ? document.querySelector('input[name="Q3a"]:checked').value : null,
      Q3b: document.querySelector('input[name="Q3b"]:checked') ? document.querySelector('input[name="Q3b"]:checked').value : null,
      Q3c: document.querySelector('input[name="Q3c"]:checked') ? document.querySelector('input[name="Q3c"]:checked').value : null,
      Q4: document.querySelector('input[name="Q4"]:checked') ? document.querySelector('input[name="Q4"]:checked').value : null,
    };

    var correctAnswers = {
      Q1a: '1',
      Q1b: '12',
      Q1c: '3',
      Q2a: '14',
      Q2b: '12',
      Q2c: '0',
      Q3a: 'True',
      Q3b: 'False',
      Q3c: 'False',
      Q4: 'True',
    };

    var correct = true;

    // Clear previous error messages
    var errorSpans = document.querySelectorAll('[id^="errorQ"]');
    errorSpans.forEach(function (errorSpan) {
      errorSpan.textContent = '';
      errorSpan.style.display = 'none';
    });

    // Check if all answers are correct
    for (var key in answers) {
      if (answers[key] !== correctAnswers[key]) {
        showErrorMessage(key);
        correct = false;
      }
    }

    if (correct) {
      // Submit the form
      document.forms[0].submit();
    }
}


/// Showing error message
function showErrorMessage(question) {
var errorSpan = document.getElementById('error' + question);
errorSpan.textContent = 'Incorrect';
errorSpan.style.display = 'inline';
}