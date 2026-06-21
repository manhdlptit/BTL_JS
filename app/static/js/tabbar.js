function openTab(name) {
  let i = 0;
  let x = document.getElementsByClassName("tabbar");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  let buttons = document.querySelectorAll(".button_click_tabbar button");
  buttons.forEach(function (btn) {
    btn.classList.remove("active");
  });
  document.getElementById(name).style.display = "block";
  event.currentTarget.classList.add("active");
}
