// function togglePasswordVisibility(inputId) {
//   const passwordInput = document.getElementById(inputId);
//   const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
//   passwordInput.setAttribute('type', type);
// }

// document.getElementById('signupForm').addEventListener('submit', function (event) {
//   // Add your validation logic here
//   const email = document.getElementById('email').value;
//   const password = document.getElementById('password').value;
//   const confirmPassword = document.getElementById('confirmPassword').value;

//   // Email validation
//   if (!isValidEmail(email)) {
//       document.getElementById('emailWarning').textContent = 'Invalid email address';
//       event.preventDefault();
//   } else {
//       document.getElementById('emailWarning').textContent = '';
//   }

//   // Password length validation
//   if (password.length < 7) {
//       document.getElementById('passwordWarning').textContent = 'Password must be at least 7 characters';
//       event.preventDefault();
//   } else {
//       document.getElementById('passwordWarning').textContent = '';
//   }

//   // Password strength validation
//   // You can implement a more sophisticated password strength check here

//   // Confirm password match
//   if (password !== confirmPassword) {
//       document.getElementById('confirmPasswordWarning').textContent = 'Passwords do not match';
//       event.preventDefault();
//   } else {
//       document.getElementById('confirmPasswordWarning').textContent = '';
//   }
// });

// function isValidEmail(email) {
//   // Implement your email validation logic here
//   // This is a basic example, you may want to use a regular expression for a more thorough check
//   return email.includes('@') && email.includes('.');
// }






const txtPassword1 = document.getElementById("txtPassword1");
const txtPassword2 = document.getElementById("txtPassword2");
const btnToggle1 = document.getElementById("btnToggle1");
const btnToggle2 = document.getElementById("btnToggle2");

btnToggle1.addEventListener("click", function() {
if(txtPassword1.type === "password"){
  txtPassword1.type = "text";f
}else{
  txtPassword1.type="password"
}
});

btnToggle2.addEventListener("click", function() {
if(txtPassword2.type === "password"){
  txtPassword2.type = "text";
}else{
  txtPassword2.type="password"
}
});

function checkinput(){

}

