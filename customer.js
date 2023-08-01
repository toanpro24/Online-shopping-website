function myFunction() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
}
// Assuming you have the actual password stored in a variable named 'actualPassword'
function hidePassword() {
    document.getElementById("passwordValue").innerText = "************";
  }
  
  // Call the hidePassword function when the page is loaded or when the user clicks on their account information
  document.addEventListener("DOMContentLoaded", function() {
    hidePassword();
  });
  