const showtimeButtons = document.querySelectorAll(".btn_slot");

showtimeButtons.forEach(function (button) {
  button.onclick = function (event) {
    event.stopPropagation();
    const targetUrl = button.getAttribute("data-url");
    window.location.href = targetUrl;
  };
});
