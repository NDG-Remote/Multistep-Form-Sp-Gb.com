var form1 = document.getElementById("form1");
var form2 = document.getElementById("form2");
var form3 = document.getElementById("form3");

var next1 = document.getElementById("next1");
var next2 = document.getElementById("next2");
var back1 = document.getElementById("back1");
var back2 = document.getElementById("back2");

var progress = document.getElementById("progress");

next1.onclick = function () {
  form1.style.left = "-450px";
  form2.style.left = "40px";
  progress.style.width = "240px";
};

back1.onclick = function () {
  form1.style.left = "40px";
  form2.style.left = "450px";
  progress.style.width = "120px";
};

next2.onclick = function () {
  form2.style.left = "-450px";
  form3.style.left = "40px";
  progress.style.width = "360px";
};

back2.onclick = function () {
  form2.style.left = "40px";
  form3.style.left = "450px";
  progress.style.width = "240px";
};

/* Form Validation */
var email = document.getElementById("email");
var password = document.getElementById("password");
var passwordConfirmation = document.getElementById("passwordconfirmation");
var inputValidationMessage = document.getElementById(
  "input-validation-message"
);
var h3 = document.getElementsByClassName("h3");

/* form3.addEventListener("submit", (e) => {
  e.preventDefault();

  validateInputs();
});
*/

/* email.oninput = function () {
  inputValidationMessage.style.color = "green";
  inputValidationMessage.innerText = "Thank you!";
};

email.oninput = function () {
  h3.innerText = email.value;
}; */

/* let setError = (field, string) => {
    field.innerHTML = string
}

let setSuccess = (field) => {
    field.innerHTML = "Thank you!"
}

const validateInputs = () => {
  const emailValue = email.value.trim();
  const passwordValue = password.value.trim();

  if (!isValidEmail(emailValue)) {
    setError(email, "Provide a valid email address");
  } else {
    setSuccess(email);
  }
};

email.oninput.validateInputs(); */


/* Exclamation Mark hover function */
var noteImages = document.querySelectorAll(".note-image, #note-image2");

noteImages.forEach(function (image) {
  image.addEventListener("mouseover", showInfoBox);
  image.addEventListener("mouseout", hideInfoBox);
});

function showInfoBox(event) {
  var infoBox = event.target.parentElement.querySelector(".info-box");
  infoBox.style.display = "block";
}

function hideInfoBox(event) {
  var infoBox = event.target.parentElement.querySelector(".info-box");
  infoBox.style.display = "none";
}
