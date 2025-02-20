//
// Hunter Jones
//
// Adds login functionality
//


// Grab login form elements
const loginForm = document.getElementById("login-form");
const loginUsernameElement = document.getElementById("login-username-input");
const loginPasswordElement = document.getElementById("login-password-input");

// Check the credentials of a login attempt
function checkCredentials() {
  // Package data in a JSON object
  let form_data = { 'username': loginUsernameElement.value, 'password': loginPasswordElement.value};

  // Send data to server via jQuery.ajax({})
  jQuery.ajax({
    url: "/authenticatelogin",
    data: form_data,
    type: "POST",
    success: function (returned_data) {
      // Parse the returned data into a json object
      returned_data = JSON.parse(returned_data);

      if ('success' in returned_data) {
        // On successful login, redirect users to home page
        window.location.href = "/home";
      } else {
        // Clear the login fields
        loginUsernameElement.value="";
        loginPasswordElement.value="";
      }
    }
  });
}

// Set login form event handler for submitting
loginForm.onsubmit = function(loginFormEvent) {
  // Prevent default behavior
  loginFormEvent.preventDefault();
  checkCredentials();
}