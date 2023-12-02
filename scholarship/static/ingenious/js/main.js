$(document).ready(function () {
  // Close the dropdown if the user clicks outside of it
  window.onclick = function (event) {
    if (event.target.matches(".menu-toggle")) {
      $(".menu-toggle").toggleClass("active");
      $(".nav-links").toggleClass("active");
      $("nav").toggleClass("active");
      $(".body-wrapper").toggleClass("blur");
    } else {
      $(".menu-toggle").removeClass("active");
      $(".nav-links").removeClass("active");
      $("nav").removeClass("active");
      $(".body-wrapper").removeClass("blur");
    }
  };
});

var navigation = document.getElementsByTagName("nav");
window.addEventListener("scroll", function () {
  if (window.pageYOffset > 0) {
    $(navigation).addClass("gradient");
  } else {
    $(navigation).removeClass("gradient");
  }

  $("form.filter").css("top", window.pageYOffset);
});