AOS.init();
// You can also pass an optional settings object
// below listed default settings
AOS.init({
  
  // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
  offset: 120, // offset (in px) from the original trigger point
  delay: 0, // values from 0 to 3000, with step 50ms
  duration: 700, // values from 0 to 3000, with step 50ms
  easing: 'ease', // default easing for AOS animations
  once: false, // whether animation should happen only once - while scrolling down
  mirror: false, // whether elements should animate out while scrolling past them
  anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation

});

// document.addEventListener("DOMContentLoaded", function() {
//   // Initialize the modal when the page loads
//   var myModal = new bootstrap.Modal(document.getElementById("ConactModal"));

//   // Show the modal when the button is clicked
//   document.getElementById("ContactMeBtn").addEventListener("click", function() {
//       myModal.show();
//   });

// });

document.addEventListener("DOMContentLoaded", function() {
  // Initialize the modal when the page loads
  var myModal = new bootstrap.Modal(document.getElementById("ConactModal"));

  // Check if a flag is set in local storage to determine if the modal should be shown
  var modalShown = localStorage.getItem('modalShown');

  if (modalShown) {
      // If the modal hasn't been shown, show it
      myModal.show();

      // Set a flag in local storage to indicate that the modal has been shown
      localStorage.setItem('modalShown', 'false');
  }

  document.getElementById("ContactMeBtn").addEventListener("click", function() {
      localStorage.setItem('modalShown', 'true');
  });
});